from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'registerInput',
        'name': 'username',
        'placeholder': " ",
    }))
    email = forms.EmailField(max_length=40, widget=forms.EmailInput(attrs={
        'class': 'registerInput',
        'name': 'email',
        'placeholder': " "
    }))
    password_one = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={
        'class': 'registerInput',
        'name': 'password_one',
        'placeholder': " ",
    }))
    password_two = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={
        'class': 'registerInput',
        'name': 'password_two',
        'placeholder': " "
    }))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError("This username is reserved!")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email is reserved!")
        return email

    def clean(self):
        cleaned_data = super().clean()
        pass1 = self.cleaned_data.get("password_one")
        pass2 = self.cleaned_data.get("password_two")
        if pass1 != pass2:
            raise forms.ValidationError("Password don't match")
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'registerInput',
        'name': 'username',
        'placeholder': " ",
    }))
    password_one = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={
        'class': 'registerInput',
        'name': 'password_one',
        'placeholder': " ",
    }))