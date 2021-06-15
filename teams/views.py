from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Equipo,Estadio,Extra
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse, request
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render,reverse

class HomeListView(ListView):
    model = Equipo
    template_name = 'home.html'
    context_object_name = 'team'
    permission_required = ('teams.add_team')

class EstadiosListView(ListView):
    model = Estadio
    template_name = 'estadios.html'
    context_object_name = 'estadios'

class CalendarioListView(LoginRequiredMixin,ListView):
    model = Extra
    template_name = 'schedule.html'
    context_object_name = 'calendario'


class EquipoCreateView(LoginRequiredMixin,CreateView):
    model = Equipo
    template_name = "agregar.html"
    fields = '__all__'
    success_url = reverse_lazy('home')
    permission_required = ('teams.add_team')

class EquipoUpdateView(LoginRequiredMixin,UpdateView):
    model = Equipo
    template_name = "editar.html"
    fields = '__all__'
    success_url = reverse_lazy('home')

class EquipoDeleteView(LoginRequiredMixin,DeleteView):
    model = Equipo
    template_name = 'borrar.html'
    context_object_name = 'team'
    success_url = reverse_lazy('home')

