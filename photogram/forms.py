from django import forms
from .models import Photo,Profile
class NewPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['user', 'likes','comments']
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']