from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from .forms import RegisterForm, LoginForm

User = get_user_model()

