from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.list import ListView

class ListaProdutos(ListView):
    def get(self, *args, **kwargs):
        return HttpResponse('Produto: ListaProdutos')


class DetalheProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Produto: DetalheProduto')


class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Produto: AdicionarAoCarrinho')


class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Produto: RemoverDoCarrinho')

class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Produto: Carrinho')


class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Produto: Finalizar')
