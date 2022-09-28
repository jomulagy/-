from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.conf import settings
from account.forms import UserForm
from account.models import myUser
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import chromedriver_autoinstaller
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import string
import random
import time
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

img_urls=[]
page_urls=[]

def loading(request):
    return render(request,'loading.html')

def load_img(request):

    options = webdriver.ChromeOptions() # 크롬 옵션 객체 생성
    options.add_argument('headless') # headless 모드 설정
    options.add_argument("window-size=1920x1080") # 화면크기(전체화면)
    # options.add_argument("disable-gpu") 
    # options.add_argument("disable-infobars")
    # options.add_argument("--disable-extensions")

    # # 속도 향상을 위한 옵션 해제
    # prefs = {'profile.default_content_setting_values': {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}   
    # options.add_experimental_option('prefs', prefs)


    chromedriver_autoinstaller.install()

    driver = webdriver.Chrome(options = options)

    driver.implicitly_wait(1)
    
    driver.get('https://www.hiver.co.kr/')
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='adaptive']/div/div/button[2]")))
    driver.find_element(By.XPATH,"//*[@id='adaptive']/div/div/button[2]").click()
    for i in range(3,8):
        img = driver.find_element(By.XPATH,"//*[@id='adaptive']/div/ul/li["+str(i)+"]/img")
        while img.get_dom_attribute("src") == None:
            img = driver.find_element(By.XPATH,"//*[@id='adaptive']/div/ul/li["+str(i)+"]/img")
        img_urls.append(img.get_attribute("src"))
        driver.find_element(By.XPATH,"//*[@id='adaptive']/div").click()
        page_urls.append(driver.current_url)
        time.sleep(1)
        driver.back()

        driver.find_element(By.XPATH,"//*[@id='adaptive']/div/button[2]").click()
        time.sleep(1)
    driver.quit()
    
    return redirect(home)


def load(request):
    return redirect('login')

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.email = new_user.username
            new_user.save()

            return redirect('login')
    else:
        form = UserForm()
        return render(request, "register/register.html", {'form': form})

def login(request):
    return render(request,"login/login.html")

def home(request):
    index_urls = list(zip(img_urls, page_urls))
    context = {
        "urls" : index_urls,
    }
    return render(request, 'index.html',context)

def forgot_password(request):
    context = {}
    if request.method=='POST':
        email = request.POST.get('email')
        try :
            user = myUser.objects.get(email=email)

            if user is not None:
                new_pw_len = 10 # 새 비밀번호 길이

                pw_candidate = string.ascii_letters + string.digits + string.punctuation 
                
                new_pw = ""
                for i in range(new_pw_len):
                    new_pw += random.choice(pw_candidate)
                
                user.set_password(new_pw)
                user.save()
                template = render_to_string('login/email_template.html',{'name':myUser.get_full_name(user),'password':new_pw})
                method_email = EmailMessage(
                    'Your ID is in the email',
                    template,
                    to = [email],
                )
                method_email.send(fail_silently=False)
                return render(request, 'login/email_sent.html',context)
        except:
            messages.info(request, 'There is no username along with the email')
    context = {}
    return render(request, "login/forgot_password.html",context)

def setting(request):
    return render(request, 'register/settings.html')

@csrf_exempt
def change_img(request):
    if request.method == "POST":
        
        if (myUser.objects.filter(id=request.POST["id"]).exists()):
            user = myUser.objects.get(id=request.POST["id"])
            user.image = request.FILES["image"]
            user.save()
            is_changed = True
        else:
            is_changed = False
    context = {
        "is_changed": is_changed,
    }
    return JsonResponse(context)
    

