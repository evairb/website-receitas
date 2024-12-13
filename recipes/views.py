from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    context = {'nome':'Evair'}
    return render(request, 'recipes/home.html', context=context)

# Create your views here.
def sobre(request):
    return HttpResponse('sobre')


