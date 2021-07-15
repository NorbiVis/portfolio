from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from .models import Post
from .forms import PostForm
from django.http import Http404
import secrets


def home_page(request):
    posts = Post.objects.all()
    return render(request, 'wiki/index.html', {
        'posts': posts
    })


def new_page(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        title = obj.title
        titles_qs = Post.objects.filter(title__iexact=title)
        if titles_qs.exists():
            return Http404
        else:
            obj.save()
            return HttpResponseRedirect(reverse('wiki:pages', kwargs={'title': title}))
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


def search_pages(request):
    search_inp = request.GET.get('search')
    qs = Post.objects.filter(title__iexact=search_inp)
    if qs.exists():
        return HttpResponseRedirect(reverse("wiki:pages", kwargs={'title': search_inp}))
    else:
        search = Post.objects.filter(title__icontains=search_inp)
    return render(request, 'wiki/index.html', {
        "search": search
    })


def edit_post(request, title):
    form = PostForm(request.POST or None)
    post = Post.objects.get(title=title)
    form.fields['title'].initial = title
    form.fields['description'].initial = post.description
    title = request.POST.get("title")
    description = request.POST.get("description")
    if form.is_valid():
        obj = post
        obj.title = title
        obj.description = description
        obj.save()
        return HttpResponseRedirect(reverse('wiki:pages', kwargs={'title': title}))
    return render(request, 'wiki/edit_post.html', {
        'form': form
    })


def random(request):
    posts = Post.objects.all()
    random_post = secrets.choice(posts)
    title = random_post.title
    return HttpResponseRedirect(reverse('wiki:pages', kwargs={'title': title}))
