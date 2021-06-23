from django.conf.urls import url
from .views import TiendaListView,SearchListView,CheckoutTemplateView
from django.shortcuts import render
from django.urls import path

urlpatterns=[
    path('',TiendaListView.as_view(),name='shop'),
    path('search/',SearchListView.as_view(),name='search_result'),
    path('checkout/<int:pk>/',CheckoutTemplateView.as_view(),name='checkout'),
]