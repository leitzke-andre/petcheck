from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render

from pets.models import Pet, PetWeight


# Create your views here.
class PetListView(generic.ListView):
    model = Pet
    context_object_name = 'pets'
    queryset = Pet.objects.all()


class PetDetailView(generic.DetailView):
    model = Pet

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pet = self.object
        weights = PetWeight.objects.filter(pet=pet)
        context['weights'] = weights
        return context
