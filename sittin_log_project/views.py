from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.urls import reverse_lazy
from sittin_log_app.models import Pet

# def home_view(request):
#     """Home Route."""

#     return render(request, 'generic/home.html')


class PetListView(LoginRequiredMixin, ListView):

    template_name = './home.html'
    model = Pet
    context_object_name = 'pets'
    login_url = reverse_lazy('login')
    pk_url_kwarg = 'id'

    def get_queryset(self):
        return Pet.objects.all()
