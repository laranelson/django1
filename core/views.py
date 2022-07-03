from django.shortcuts import render, get_object_or_404
from .models import Produto, Cliente

from django.http import HttpResponse
from django.template import loader

def index(request):
    produtos = Produto.objects.all()

    clientes = Cliente.objects.all()

    context = {
        'curso': "Curso de Django",
        'outro': "É muito massa!",
        'produtos': produtos,
        'clientes': clientes
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def product(request, pk):
    #prod = Produto.objects.get(id=pk) >>> A LINHA ABAIXO FAZ A MESMA COISA, SÓ QUE EM CASO DE ERRO ELA VAI DIRECIONAR PARA ERRO 404
    prod = get_object_or_404(Produto, id=pk)

    context = {
        'produto': prod
    }
    return render(request, 'product.html', context)


def client(request, pk):
    cli = Cliente.objects.get(id=pk)

    context = {
        'cliente': cli
    }
    return render(request, 'client.html', context)


def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)


