from django.shortcuts import render, redirect
from account.models import myUser
from clothe.models import clothe
from .forms import clotheForm

def search(request):
    clothes = []
    if request.method=='POST':
        userid = request.POST.get('username')
        keyward = request.POST.get('keyward')
        
        if keyward == '':
            return render(request, 'list/search.html',{'userid':userid,'keyward':keyward, 'clothes':clothes})
        
        datas = clothe.objects.filter(user_id = userid, name__contains = keyward)
        
        for data in datas:
            clothes.append(data.image.url)
        return render(request, 'list/search.html',{'userid':userid,'keyward':keyward, 'clothes':clothes})

def add(request):
    
    if request.method == "POST":
        form = clotheForm(request.POST)
        if form.is_valid():
            new_clothe = form.save(commit=False)
            new_clothe.image = request.FILES['image']
            new_clothe.user = myUser.objects.get(id=request.user.id)
        
            new_clothe.save()

            return redirect('home')

    return render(request,'clothe/add.html')

def list(request, view_for):
    img_urls = []
    clothe_ids = []
    datas = []

    userid = request.user.id
    if view_for == 'all':
        datas = clothe.objects.filter(user_id = userid)
    elif 'parent_category' in view_for:
        parent_category = view_for[view_for.find('?=')+2:]
        datas = clothe.objects.filter(user_id = userid,parent_category = parent_category)
    elif 'child_category' in view_for:
        child_category = view_for[view_for.find('?=')+2:]
        datas = clothe.objects.filter(user_id = userid,child_category = child_category)
    elif 'season' in view_for:
        season = view_for[view_for.find('?=')+2:]
        datas = clothe.objects.filter(user_id = userid,season = season)
    elif 'style' in view_for:
        style = view_for[view_for.find('?=')+2:]
        datas = clothe.objects.filter(user_id = userid,style = style)
    elif 'color' in view_for:
        color = view_for[view_for.find('?=')+2:]
        datas = clothe.objects.filter(user_id = userid,color = color)
    for data in datas:
        img_urls.append(data.image.url)
        clothe_ids.append(data.id)
    context = {
        'img_urls':img_urls,
        'clothe_ids':clothe_ids
    }
    return render(request,'list/views.html',context)

def mylooks(request):
    return render(request,'looks/main.html')

def favorite(request):
    clothes = []

    userid = request.user.id
    datas = clothe.objects.filter(user_id = userid,favorite=True)
    for data in datas:
        clothes.append(data.image.url)
    return render(request,'list/favorite.html',{'userid':userid, 'clothes':clothes})

def weather(request):
    return render(request,'looks/weather.html')

def detail(request, clothe_id):
    data = clothe.objects.get(id = clothe_id)
    context = {
        "clothe" : data
    }
    return render(request,'clothe/detail.html',context)