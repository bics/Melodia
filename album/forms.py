from django import forms
from .models import Track
from artist.models import Artist

class TrackCreationForm(forms.ModelForm):
    required_css_class = "required"
    class Meta:
        model = Track
        fields = ("name", "position", "featured_artist", "lyrics")

        widgets = {
            "name" : forms.TextInput(attrs={"class": "form-control"}),
            "position" : forms.NumberInput(attrs={"class": "form-control"}),
            "featured_artist" : forms.SelectMultiple(attrs={"class": "form-control", "rows" : "5"}),
            "lyrics": forms.Textarea(attrs={"class": "form-control", "rows" : "5"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].required = True
        # Queryselector generated using ChatGPT
        self.fields["featured_artist"].queryset = Artist.objects.order_by("name")