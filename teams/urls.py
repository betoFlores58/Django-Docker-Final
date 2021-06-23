from django.conf.urls import url
from .views import HomeListView,EstadiosListView,EquipoCreateView,EquipoUpdateView,EquipoDeleteView, CalendarioListView, ComentarioCreateView
from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns=[
    path('', HomeListView.as_view(), name='home'),
    path('estadios/', EstadiosListView.as_view(), name='estadios'),
    path('calendario/', CalendarioListView.as_view(), name='calendario'),
    path('equipo_nuevo/', EquipoCreateView.as_view(), name='nuevo'),
    path('equipo/<int:pk>/editar', EquipoUpdateView.as_view(), name='editar'),
    path('delete/<int:pk>/', EquipoDeleteView.as_view(), name = 'eliminar'),
    path('<int:pk>/comment_nuevo/', ComentarioCreateView.as_view(), name='nuevo_com'),
    path('search_results/', views.search_results, name = 'search_results'),
]