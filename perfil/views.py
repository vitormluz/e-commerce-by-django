from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse


class Criar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Perfil: Criar')


class Atualizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Perfil: Atualizar')


class Login(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Perfil: Login')


class Logout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Perfil: Logout')
