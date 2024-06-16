from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render


# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'home/index.html'