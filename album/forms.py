from django import forms
from .models import Track
from artist.models import Artist
from django.forms import modelformset_factory, CheckboxInput

class TrackCreationForm(forms.ModelForm):
    required_css_class = "required"
    class Meta:
        model = Track
        fields = ("name", "position", "featured_artist", "lyrics", "track")

        widgets = {
            "name" : forms.TextInput(attrs={"class": "form-control"}),
            "position" : forms.NumberInput(attrs={"class": "form-control"}),
            "featured_artist" : forms.SelectMultiple(attrs={"class": "form-select featured-artist-select", "rows" : "5", "multiple": True}),
            "lyrics": forms.Textarea(attrs={"class": "form-control", "rows" : "5"}),            
            "track" : forms.FileInput(attrs={"class": "form-control", "accept": ".mp3,audio/mpeg"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].required = True
        # Queryselector generated using ChatGPT
        self.fields["featured_artist"].queryset = Artist.objects.order_by("name")


# Formset generated using ChatGPT
TrackFormSet = modelformset_factory(
    Track,
    form=TrackCreationForm,
    extra=12,
    max_num=12
)

class UpdateTrackForm(forms.ModelForm):
    required_css_class = "required"
    class Meta:
        model = Track
        fields = ("name", "position", "featured_artist", "lyrics", "track")

        widgets = {
            "name" : forms.TextInput(attrs={"class": "form-control"}),
            "position" : forms.NumberInput(attrs={"class": "form-control"}),
            "featured_artist" : forms.SelectMultiple(attrs={"class": "form-select featured-artist-select", "rows" : "5", "multiple": True}),
            "lyrics": forms.Textarea(attrs={"class": "form-control", "rows" : "5"}),            
            "track" : forms.FileInput(attrs={"class": "form-control", "accept": ".mp3,audio/mpeg"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].required = True
        # Queryselector generated using ChatGPT
        self.fields["featured_artist"].queryset = Artist.objects.order_by("name")

UpdateTrackFormSet = modelformset_factory(
    Track,
    form=UpdateTrackForm,
    extra=12,
    max_num=12,
    can_delete=True,
)