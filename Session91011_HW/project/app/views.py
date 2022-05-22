from ftplib import error_perm
from django.shortcuts import render, redirect
from .models import Post, Comment
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request) :
    posts = Post.objects.all()

    return render(request, 'home.html', {'posts':posts})

@login_required(login_url='/registration/login')
def new(request) :
    if request.method == 'POST' :
        title = request.POST['title']
        content = request.POST['content']

        new_post = Post.objects.create(
            title=title,
            content=content,            
            pub_date = timezone.now(),
            author = request.user
        )
        return redirect('detail', new_post.pk)
    return render(request, 'new.html')

@login_required(login_url='/registration/login')
def detail(request, post_pk) :
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        content = request.POST['content']
        Comment.objects.create(
            post=post,
            content=content,
            author = request.user
        )
        return redirect('detail', post_pk)
    return render(request, 'detail.html', {'post':post})

def edit(request, post_pk) :
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST' :
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.filter(pk=post_pk).update(
            title = title,
            content = content
            )
        return redirect('detail', post_pk)
    return render(request, 'edit.html', {'post':post})

def delete(request, post_pk) :
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('home')

def delete_comment(request, post_pk, comment_pk) : 
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', post_pk)

def signup(request) : 
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        found_user = User.objects.filter(username=username)
        if len(found_user):
            error = "중복된 아이디입니다!"
            return render(request, "signup.html", {"error": error})
        new_user = User.objects.create_user(username=username, password=password)
        auth.login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect("home")
    return render(request, 'signup.html')

def login(request) : 
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect(request.GET.get("next","/"))
        error = "아이디 또는 비밀번호가 일치하지 않습니다."
        return render(request, "login.html", {"error": error})
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect("home")

