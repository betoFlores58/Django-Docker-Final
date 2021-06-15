from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tienda
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse, request
from django.contrib.auth.models import User
from django.db.models import Q

class TiendaListView(ListView):
    model = Tienda
    template_name = 'tienda/shop.html'
    context_object_name = "productos"

class CheckoutTemplateView(TemplateView):
    model=Tienda
    context_object_name = 'prods'
    template_name = 'tienda/checkout.html'

class SearchListView(ListView):
    model=Tienda
    context_object_name = 'articulos'
    template_name = 'tienda/search_results.html'
