from ssl import ALERT_DESCRIPTION_PROTOCOL_VERSION
from unicodedata import category
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def index(request):
    return render(request, 'index.html')
def new(request):
    if request.method == 'POST':
        print(request.POST)
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            cartegory = request.POST['cartegory'],
        )
        return redirect('list')

    return render(request, 'new.html')

def cartegory(request):
    hobby = len(Article.objects.filter(cartegory='hobby'))
    food = len(Article.objects.filter(cartegory='food'))
    programming = len(Article.objects.filter(cartegory='programming'))
    return render(request, 'cartegory.html', {
        'hobby' : hobby, 
        'food' : food, 
        'programming' : programming}
    )

def list(request, cartegory):
    articles = Article.objects.filter(cartegory__contains=cartegory)
    cartegory_name = cartegory
    return render(request, 'list.html', {'articles' : articles, 'cartegory' : cartegory_name})

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'detail.html', {'article' : article})