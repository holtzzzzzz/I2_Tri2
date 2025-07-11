# veiculos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Automovel
from .forms import AutomovelForm
from django.http import HttpResponse


def automovel_lista(request):
    automoveis = Automovel.objects.all().order_by('marca')
    return render(request,
                  'veiculos/automovel_lista.html',
                  {'automoveis': automoveis})


def automovel_criar(request):
    if request.method == 'POST':
        form = AutomovelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('veiculos:automovel_lista')
    else:
        form = AutomovelForm()

    return render(request,
                  'veiculos/adicionar_automovel.html',
                  {'form': form,
                   'titulo_pagina': 'Adicionar Veículo'})


def automovel_detalhe(request, pk):
    automovel = get_object_or_404(Automovel, pk=pk)
    return render(request,
                  'veiculos/automovel_detalhe.html',
                  {'automovel': automovel})


def automovel_teste(request):
    return HttpResponse('<h1>Sistema de Locadora - Teste</h1>')