from django import forms
from .models import *



class PostModelForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title','photo1','photo2','photo3','post_body']

