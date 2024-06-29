from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User
import logging

logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'core/home.html')

def signup(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']

            # Criar um novo usuário
            user = User.objects.create(username=username, email=email, password=password)
            
            # Mensagem de sucesso e redirecionamento para o login
            messages.success(request, "Cadastro realizado com sucesso.")
            return redirect('signin')

        except Exception as e:
            # Se ocorrer um erro, registrar no log e mostrar página de erro
            messages.error(request, f"Erro durante o cadastro: {e}")
            logger.error(f"Erro durante o cadastro: {e}")
            return render(request, 'core/error.html')

    return render(request, 'core/signUp.html')

def signIn(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            password = request.POST['password']

            # Autenticar o usuário
            user = authenticate(request, email=email, password=password)

            if user is not None:
                # Login bem-sucedido
                login(request, user)
                messages.success(request, "Login realizado com sucesso.")
                return redirect('home')
            else:
                # Login falhou
                messages.error(request, "Usuário ou senha inválidos.")
                return render(request, 'core/signIn.html')

        except Exception as e:
            # Se ocorrer um erro, registrar no log e mostrar página de erro
            messages.error(request, f"Erro durante o login: {e}")
            logger.error(f"Erro durante o login: {e}")
            return render(request, 'core/error.html')

    return render(request, 'core/signIn.html')
