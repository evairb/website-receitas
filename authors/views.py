from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages
from .forms import RegisterForm, InformacoesPessoalForm, LoginForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from recipes.models import Recipe


# Create your views here.
def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    context = {
        'form': form,
        'form_action': reverse('authors:create'),
        }
    return render(request, 'authors/pages/register_view.html', context)


def register_create(request):
    if not request.POST:
        raise Http404()
    POST = request.POST
    request.session['register_form_data'] = POST

    form = RegisterForm(POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
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


def login_view(request):
    form = LoginForm()
    context = {
        'form': form,
        'form_action': reverse('authors:login_create')

    }
    return render(request, 'authors/pages/login.html', context=context)


def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)
    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )
        if authenticated_user is not None:
            messages.success(request, 'You are logged in.')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Invalid credentials')
    else:
        messages.error(request, 'Error to validate form data')
    return redirect(reverse('authors:dashboard'))


@login_required(login_url='authors:login', redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        return redirect(reverse('authors:login'))
    logout(request)
    return redirect(reverse('authors:login'))


@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard(request):
    print(request.user)
    recipes = Recipe.objects.filter(
        is_published=False,
        author=request.user
    )
    context = {
        'recipes': recipes
    }
    print(recipes)
    return render(request, 'authors/pages/dashboard.html', context=context)
