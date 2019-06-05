from django.urls import path
from .views import PetListView, PetDetailView, FamilyListView

urlpatterns = [
    path('', PetListView.as_view(), name='pet_list'),
    path('pet/<int:pk>',PetDetailView.as_view(), name='pet_detail'),
    path('families/', FamilyListView.as_view(), name='family_list'),
]