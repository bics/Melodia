from django import forms
from album.models import Album

class AlbumCreationForm(forms.ModelForm):
    required_css_class = "required"
    class Meta:
        model = Album
        fields = ("name", "image", "description", "released")

        labels = {
            "image": "Cover"
        }

        widgets = {
            "name" : forms.TextInput(attrs={"class": "form-control"}),
            "image" : forms.FileInput(attrs={"class": "form-control", "accept": "image/png, image/jpeg, image/jpg"}),
            "description" : forms.Textarea(attrs={"class": "form-control", "rows" : "5"}),
            "released": forms.DateInput(attrs={"class": "form-control","type": "date"}),
        }

        help_texts = {
            "image": "Optional. Your image will be stored securely using Cloudinary to display your image.",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].required = True
        self.fields["released"].required = True