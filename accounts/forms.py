from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from .models import User, Profile


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="이름",
        widget=forms.TextInput(attrs={
            "placeholder": "사용자 이름",
        })  
    )

    password1 = forms.CharField(
        label="비밀번호 설정",
        widget=forms.PasswordInput(attrs={
            "placeholder": "비밀번호(8자 이상)",
        })
    )
    
    password2 = forms.CharField(
        label="비밀번호 확인",
        widget=forms.PasswordInput(attrs={
            "placeholder": "비밀번호 확인",
        })
    )

    phone_number = forms.CharField(
        label="전화번호",
        widget=forms.TextInput(attrs={
            "placeholder": "ex) 010-1234-5678",
        })
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'age', 'gender', 'email', 'phone_number', 'self_introduce',)


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('username', 'age', 'gender', 'email', 'phone_number', 'self_introduce',)


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "사용자 이름",
        })   
    )

    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            "placeholder": "비밀번호(8자 이상)",
        })
    )


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']