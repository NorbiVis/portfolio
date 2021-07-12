from django.shortcuts import render, HttpResponse
from .models import Post
from .forms import PostForm
from django.http import Http404


def home_page(request):
    posts = Post.objects.all()
    return render(request, 'wiki/index.html', {
        'posts': posts
    })


def new_page(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
    return render(request, 'wiki/new_page.html', {

    })


def pages(request, title):
    try:
        posts = Post.objects.get(title__iexact=title)
    except:
        raise Http404
    return render(request, 'wiki/pages.html', {
        'posts': posts
    })


def random_page(request):
    return render(request, 'wiki/random_page.html', {

    })
