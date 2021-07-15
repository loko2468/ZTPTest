from django import forms
from .models import File

class upload_form(forms.ModelForm):
    class Meta:
        model = File
        fields = ('xlsx',)