from django.urls import path

from . import views

urlpatterns = [
    path('', views.PetListView.as_view(), name='pets_index'),
    path('<int:pk>/', views.PetDetailView.as_view(), name='pet_detail'),
]