# Imports taken from previous CoffeeHouse project
from django import forms
from allauth.account.forms import (
    SignupForm,
    LoginForm,
    ResetPasswordForm,
    ResetPasswordKeyForm,
)
from .models import MelodiaUser

# Form taken from previous CoffeeHouse project
class AllauthLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["login"].widget.attrs.update({"class": "form-control"})
        self.fields["password"].widget.attrs.update({"class": "form-control"})

# Form taken from previous CoffeeHouse project
class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = MelodiaUser
        fields = ("username", "email")

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control mb-2"}),
            "email": forms.EmailInput(attrs={"class": "form-control mb-2"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].required = True
        self.fields["email"].required = True
        # Snippet taken from ChatGPT
        self.fields["username"].help_text = ""
