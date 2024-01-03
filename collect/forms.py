from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

CustomUser = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email")
        labels = {"username": "ユーザーネーム", "email": "メールアドレス"}


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "password")
        labels = {"username": "ユーザーネーム", "password": "パスワード"}


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "profile",
            "avatar",
            "display_name",
            "links",
            "location",
            "birth_date",
            "company",
        )
        labels = {
            "username": "ユーザーネーム",
            "email": "メールアドレス",
            "profile": "プロフィール",
            "avatar": "アバター",
            "display_name": "表示名",
            "links": "リンク",
            "location": "場所",
            "birth_date": "誕生日",
            "company": "会社",
        }
        widgets = {
            "display_name": forms.TextInput(attrs={"placeholder": "表示名"}),
            "avatar": forms.ClearableFileInput(attrs={"multiple": False}),
            "birth_date": forms.DateInput(attrs={"type": "date"}),
        }
