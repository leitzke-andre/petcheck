from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render

from pets.models import Pet


# Create your views here.
class PetListView(generic.ListView):
    model = Pet
    context_object_name = 'pets'
    queryset = Pet.objects.all()


class PetDetailView(generic.DetailView):
    model = Pet
