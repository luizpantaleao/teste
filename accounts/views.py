from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .models import FormContato


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Você fez login com sucesso')
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    return redirect('index')


def cadastro(request):

    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
        messages.error(request, 'Nenhum campo pode estar vazio')
        return render(request, 'accounts/cadastro.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'EMAIL INVÁLIDO')
        return render(request, 'accounts/cadastro.html')

    if len(senha) < 6:
        messages.error(request, 'Senha deve ter pelo menos 6 caracteres')
        return render(request, 'accounts/cadastro.html')

    if len(usuario) < 6:
        messages.error(request, 'Usuário deve ter pelo menos 6 caracteres')
        return render(request, 'accounts/cadastro.html')

    if senha != senha2:
        messages.error(request, 'Senhas não batem')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuario ja existe')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Senhas não batem')
        return render(request, 'accounts/cadastro.html')

    messages.success(request, 'Usuario registraso. Faça o login abaixo')
    user = User(username=usuario, email=email, first_name=nome, last_name=sobrenome, password=senha)
    user.save()
    return redirect('login')


@login_required
def dashboard(request):
    if request.method != 'POST':
        form = FormContato
        return render(request, 'accounts/dashboard.html', {'form': form})

    form = FormContato(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar formulário')
        form = FormContato
        return render(request, 'accounts/dashboard.html', {'form': form})

    form.save()
    messages.success(request, f'Contato {request.POST.get("nome")} inserido com sucesso')
    return redirect('dashboard')
