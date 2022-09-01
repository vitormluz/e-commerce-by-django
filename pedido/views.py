from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.http import HttpResponse


class Pagar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Pedido: Pagar')


class FecharPedido(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Pedido: FecharPedido')


class Detalhe(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Pedido: Detalhe')
