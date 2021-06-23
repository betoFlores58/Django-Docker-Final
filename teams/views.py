from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .models import Equipo,Estadio,Extra,Comment
from .mixins import ValidatePermissionRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse, request
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render,reverse
from .forms import CommentForm

def search_results(request):
    if request.method == 'POST':
        search = request.POST['search']
        results = Equipo.objects.filter(
            Q(nombre__contains=search)|Q(nombre__icontains=search)
        )
        return render(request,'search_results.html',{'search':search,'results':results})
    else:
        return render(request,'search_results.html',{})

class HomeListView(ListView):
    model = Equipo
    template_name = 'home.html'
    context_object_name = 'team'
    permission_required = ('teams.view_team')

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

class ComentarioCreateView(LoginRequiredMixin,CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "agregar_comentario.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.name = self.request.user.username
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

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

