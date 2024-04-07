from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from .models import Product

def store(request):
    my_store = Product.objects.all().values()
    template = loader.get_template('all_store.html')
    context = {
        'my_store': my_store,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    my_store = Product.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'my_store': my_store,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())