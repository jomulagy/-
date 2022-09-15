from django.shortcuts import render, redirect
from .forms import PostForm
from account.models import myUser
from .models import Post
from datetime import datetime,timedelta
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def time():
    datas = Post.objects.all().order_by('-time')[0:6]
    return list(datas)

def hot():
    datas = Post.objects.all().order_by('-likes')[0:6]
    return list(datas)
def main(request):
    
    context = {
        'time' : time(),
        'hot' : hot(),
    }
    return render(request, 'post/main.html',context)



def postFormInput(request,type):
    context = {
        'title' : type,
        'time' : time(),
        'hot' : hot(),
        
    }
    return render(request,"post/add.html",context)

def add(request,type):
    context = {
        'title' : type,
        'time' : time(),
        'hot' : hot(),

    }
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.views = 0
            new_post.annonymous = True if request.POST.getlist("annonymous[]") else False
            if request.FILES.get('image'):
                new_post.image = request.FILES['image']
            new_post.user = myUser.objects.get(id=request.user.id)

            new_post.save()
    
            return redirect('/community/'+type+'/',context)
    
    return render(request, 'post/add.html',context)
    
def boards(request,type):
    datas = Post.objects.filter(board=type)
    posts = list(datas)

    context = {
        'title' : type,
        'time' : time(),
        'hot' : hot(),
        'posts' : posts
    }
    return render(request,'post/board.html',context)

def my_post(request,type):
    posts = []
    if type == '내가쓴글':
        datas = Post.objects.filter(user_id = request.user.id)
    # elif type == '댓글단글':
    #     datas = Post.objects.filter(user_id = request.user.id)
    if datas:    
        posts = list(datas)

    context = {
        'title' : type,
        'time' : time(),
        'hot' : hot(),
        'posts' : posts
    }
    return render(request,'post/my_post.html',context)

def detail(request,type,post_id):
    post = Post.objects.get(id = post_id)
    post.views+=1
    post.save()
    context = {
        'title' : type,
        'time' : time(),
        'hot' : hot(),
        'post' : post,
    }
    return render(request,'post/detail.html',context)

@csrf_exempt
def increase_like(request):

    if request.method == 'POST':
        post_id = request.POST.get('post_id')

        post = Post.objects.get(pk=post_id)
        post.likes += 1
        post.save()
           
        return HttpResponse()
