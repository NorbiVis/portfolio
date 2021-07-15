from django.urls import path, include
from .views import register_view, login_view

app_name = 'user'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login_view')
]


