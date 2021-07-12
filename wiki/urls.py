from django.urls import path, include
from .views import home_page, new_page, random_page, pages

app_name = 'wiki'

urlpatterns = [
    path('', home_page, name="home_page"),
    path('new_page', new_page, name='new_page'),
    path('wiki/<str:title>', pages, name='pages'),
    path('random_page', random_page, name='random_page'),
]
