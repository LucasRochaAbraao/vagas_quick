from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from django.views.generic import TemplateView
from rest_framework.views import APIView
from django.core import serializers
from vagas_app.serializers import VagaSerializer

from vagas_app.models import Vaga
import json


class VagasApi(APIView):
    """
    Um view para listar todas vagas ativas no DB.
    """
    def get(self, request, format='json'):
        vagas = Vaga.objects.filter(ativo=True).values()

        #return JsonResponse(vagas_response, safe=False)

        serializer = VagaSerializer(vagas, many=True)
        return Response(serializer.data)

class CustomLoginView(LoginView):
    template_name = 'vagas_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('vagas')

class VagaList(LoginRequiredMixin, ListView):
    model = Vaga
    context_object_name = 'vagas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ativos'] = context['vagas'].filter(ativo=True).count()
        context['inativos'] = context['vagas'].filter(ativo=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['vagas'] = context['vagas'].filter(
                titulo__contains=search_input)

        context['search_input'] = search_input

        return context


class VagaDetail(LoginRequiredMixin, DetailView):
    model = Vaga
    context_object_name = 'vaga'
    template_name = 'vagas_app/vaga.html'


class VagaCreate(LoginRequiredMixin, CreateView):
    model = Vaga
    fields = ['titulo', 'atividades', 'requisitos', 'destaques', 'ativo']
    success_url = reverse_lazy('vagas')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(VagaCreate, self).form_valid(form)


class VagaUpdate(LoginRequiredMixin, UpdateView):
    model = Vaga
    fields = ['titulo', 'atividades', 'requisitos', 'destaques', 'ativo']
    success_url = reverse_lazy('vagas')


class CustomDeleteView(LoginRequiredMixin, DeleteView):
    model = Vaga
    context_object_name = 'vaga'
    success_url = reverse_lazy('vagas')
