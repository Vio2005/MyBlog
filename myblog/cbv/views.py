from django.shortcuts import render
from django.views.generic import TemplateView



# Create your views here.
class Myview(TemplateView):
    template_name='bloglist.html'