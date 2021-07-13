from django import forms
from django.contrib.auth import get_user_model
from .models import Product

User = get_user_model()


class RegistrationForm:
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=40)
    password1 = forms.CharField(max_length=20, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput)

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
        pass1 = self.cleaned_data.get("password1")
        pass2 = self.cleaned_data.get("password2")
        if pass1 != pass2:
            raise forms.ValidationError("Password don't match")
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)


class AuctionForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
