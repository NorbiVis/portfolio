from django.urls import path, include
from .views import home_page, new_page, random, pages, search_pages, edit_post

app_name = 'wiki'

urlpatterns = [
    path('', home_page, name="home_page"),
    path('new_page', new_page, name='new_page'),
    path('title/<str:title>', pages, name='pages'),
    path('random_page', random, name='random'),
    path('search', search_pages, name="search"),
    path('<str:title>/edit', edit_post, name='edit_post')
]
