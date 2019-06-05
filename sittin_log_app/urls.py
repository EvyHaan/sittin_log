from django.urls import path
from .views import PetListView, FamilyListView

urlpatterns = [
    path('', PetListView.as_view(), name='pet_list'),
    path('families/', FamilyListView.as_view(), name='family_list'),
]