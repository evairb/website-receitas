from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages
from .forms import RegisterForm, InformacoesPessoalForm


# Create your views here.
def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    context = {'form': form}
    return render(request, 'authors/pages/register_view.html', context)


def register_create(request):
    if not request.POST:
        raise Http404()
    POST = request.POST
    request.session['register_form_data'] = POST

    form = RegisterForm(POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your user is created, please log in')

        del (request.session['register_form_data'])

    return redirect('authors:register')



# Create your views here.
def formulario_intra(request):
    fomulario_intra = request.session.get('fomulario_intra', None)
    form = InformacoesPessoalForm(fomulario_intra)
    context = {'form': form}
    return render(request, 'authors/pages/intranet_form.html', context)


def formulario_intra_create(request):
    if not request.POST:
        raise Http404()
    POST = request.POST
    request.session['fomulario_intra'] = POST

    form = InformacoesPessoalForm(POST)
    if form.is_valid():
        form_data = form.cleaned_data
    
        # Imprimir os dados do formulário
        print(form_data)

    #     messages.success(request, 'Your user is created, please log in')

    #     del (request.session['fomulario_intra'])

    return redirect('authors:intranet')