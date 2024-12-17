from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    context = {'nome':'Evair'}
    return render(request, 'recipes/pages/home.html', context=context)

def recipe(request, id):
    context = {'nome':'Evair'}
    return render(request, 'recipes/pages/recipe-view.html', context=context)
