from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from sittin_log_app.models import Pet, Family
from sittin_log_app.forms import PetForm, FamilyForm


# Pet Views
class PetListView(LoginRequiredMixin, ListView):

    template_name = './pet_list.html'
    model = Pet
    context_object_name = 'pets'
    login_url = reverse_lazy('login')
    pk_url_kwarg = 'id'

    def get_queryset(self):
        return Pet.objects.filter(family__user_id=self.request.user.id)


class PetDetailView(LoginRequiredMixin, DetailView):

    template_name = './pet_detail.html'
    model = Pet
    context_object_name = 'pet'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Pet.objects.filter(id=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pet'] = Pet.objects.get(pk=self.kwargs['pk'])
        return context


class PetCreateView(LoginRequiredMixin, CreateView):

    template_name = './pet_create.html'
    model = Pet
    form_class = PetForm
    success_url = reverse_lazy('pet_list')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PetUpdateView(LoginRequiredMixin, UpdateView):

    template_name = './pet_create.html'
    model = Pet
    form_class = PetForm
    success_url = reverse_lazy('pet_list')
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Pet.objects.filter(id=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pet'] = Pet.objects.get(pk=self.kwargs['pk'])
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PetDeleteView(LoginRequiredMixin, DeleteView):

    template_name = './pet_delete.html'
    model = Pet
    context_object_name = 'pet'
    success_url = reverse_lazy('pet_list')


# Family Views
class FamilyListView(LoginRequiredMixin, ListView):

    template_name = './family_list.html'
    model = Family
    context_object_name = 'families'
    login_url = reverse_lazy('login')
    pk_url_kwarg = 'id'

    def get_queryset(self):
        return Family.objects.filter(user_id=self.request.user.id)


class FamilyDetailView(LoginRequiredMixin, DetailView):

    template_name = './family_detail.html'
    model = Family
    context_object_name = 'family'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Family.objects.filter(id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['family'] = Family.objects.get(pk=self.kwargs['pk'])
        return context


class FamilyCreateView(LoginRequiredMixin, CreateView):

    template_name = './family_create.html'
    model = Family
    form_class = FamilyForm
    success_url = reverse_lazy('family_list')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class FamilyUpdateView(LoginRequiredMixin, UpdateView):

    template_name = './family_create.html'
    model = Family
    form_class = FamilyForm
    success_url = reverse_lazy('family_list')
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Family.objects.filter(id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['family'] = Family.objects.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class FamilyDeleteView(LoginRequiredMixin, DeleteView):

    template_name = './family_delete.html'
    model = Family
    context_object_name = 'family'
    success_url = reverse_lazy('family_list')