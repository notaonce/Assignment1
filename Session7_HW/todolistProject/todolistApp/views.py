from django.shortcuts import render, redirect
from .models import Post
import imp

# Create your views here.

def index(request) :
    return render(request, 'index.html')


def home(request) : 
    posts = Post.objects.all().order_by('d_day')
    return render(request, 'home.html', {'posts' : posts, })

def new(request):
    if request.method == 'POST' :
        new_post = Post.objects.create(
            title = request.POST['title'],
            detail = request.POST['detail'],
            d_day = request.POST['d_day'],
        )
        return redirect('detail', new_post.pk)
    return render(request, 'new.html')

def detail(request, post_pk) :
    post = Post.objects.get(pk=post_pk)
    
    return render(request, 'detail.html', {'post' : post})


def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST' :
        Post.objects.filter(pk=post_pk).update(
            title = request.POST['title'],
            detail = request.POST['detail'],
            d_day = request.POST['d_day']
        )
        return redirect('detail', post_pk)

    return render(request, 'edit.html', {'post' : post})



def delete(request, post_pk) :
    post = Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('home')