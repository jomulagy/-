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
            clothes.append(({"url" : data.image.url,"id" : data.id,"name":data.name}))
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

def edit(request, pk):
    
    if request.method == "POST":
        form = clotheForm(request.POST)
        if form.is_valid():
            target = clothe.objects.get(id = pk)
            target.name = request.POST.get('name')
            if request.POST.get('favorite'):
                target.favorite = True
            else:
                target.favorite = False
            target.parent_category = request.POST.get('parent_category')
            target.child_category = request.POST.get('child_category')
            target.season = request.POST.get('season')
            if request.FILES:
                target.image = request.FILES['image']
            target.style = request.POST.get('style')
            target.color = request.POST.get('color')
            target.memo = request.POST.get('memo')

            target.save()

            return redirect('home')

    return redirect('clothe_detail',pk)

def delete(request, pk):
    target = clothe.objects.get(id = pk)
    target.delete()
    return redirect('home')

def list(request, view_for):
    img_urls = []
    clothe_ids = []
    datas = []
    userid = request.user.id
    print(view_for)
    if view_for == 'all':
        datas = clothe.objects.filter(user_id = userid)
    elif 'parent_category' in view_for:
        parent_category = view_for[view_for.find('?=')+2:]
        datas = clothe.objects.filter(user_id = userid,parent_category = parent_category)
    elif 'child_category' in view_for:
        child_category = view_for[view_for.find('?=')+2:]
        print(child_category)
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
    else:
        print("error")
    print(datas)
    for data in datas:
        img_urls.append(data.image.url)
        clothe_ids.append(data.id)
    print(img_urls)
    context = {
        'img_urls':img_urls,
        'clothe_ids':clothe_ids
    }
    return render(request,'list/views.html',context)

def mylooks(request):
    return render(request,'looks/main.html')

def mylooks_form(request):
    return render(request,'looks/add.html')
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