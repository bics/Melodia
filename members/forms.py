# Imports taken from previous CoffeeHouse project
from django import forms
from allauth.account.forms import (
    SignupForm,
    LoginForm,
    ResetPasswordForm,
    ResetPasswordKeyForm,
)
from .models import MelodiaUser
from artist.models import Artist

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

class CreateArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ("name", "image", "description", "bornOn", "socials")

        widgets = {
            "name" : forms.TextInput(attrs={"class": "form-control"}),
            "image" : forms.FileInput(attrs={"class": "form-control", "accept": "image/png, image/jpeg, image/jpg"}),
            "description" : forms.Textarea(attrs={"class": "form-control", "rows" : "5"}),
            "socials" : forms.Textarea(attrs={"class": "form-control", "rows" : "5"}),
        }

        # Snippet taken from previous CoffeeHouse project
        help_texts = {
            "image": "Optional. Your image will be stored securely using Cloudinary to display your profile picture.",
            "socials" : "Enter each social on a new line."
        }
