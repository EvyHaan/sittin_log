from django.urls import path
from .views import PetListView, PetDetailView, PetCreateView, PetUpdateView, PetDeleteView, FamilyListView, FamilyDetailView, FamilyCreateView, FamilyDeleteView, FamilyUpdateView

urlpatterns = [
    path('', PetListView.as_view(), name='pet_list'),
    path('pet/<int:pk>',PetDetailView.as_view(), name='pet_detail'),
    path('pet/create', PetCreateView.as_view(), name='pet_create'),
    path('pet/<int:pk>/remove', PetDeleteView.as_view(), name='pet_delete'),
    path('pet/<int:pk>/edit/', PetUpdateView.as_view(), name='pet_edit'),

    path('families', FamilyListView.as_view(), name='family_list'),
    path('family/<int:pk>',FamilyDetailView.as_view(), name='family_detail'),
    path('family/create', FamilyCreateView.as_view(), name='family_create'),
    path('family/<int:pk>/remove', FamilyDeleteView.as_view(), name='family_delete'),
    path('family/<int:pk>/edit/', FamilyUpdateView.as_view(), name='family_edit'),
]