from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "address")


class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = (
            "last_name",
            "first_name",
            "email",
            "address",
        )
        labels = {
            "last_name": "성 (Last_name)",
            "first_name": "이름 (First_name)",
            "email": "E-mail 주소",
        }
