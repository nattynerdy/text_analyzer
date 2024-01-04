from django import forms
from images.models import ImageUpload

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = ('image',)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput,
    )