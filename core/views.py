from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def home(request):
    # Se o usuário estiver autenticado, obtenha o nome de usuário
    username = request.user.username if request.user.is_authenticated else "Seja bem-vindo"
    
    # Adicione o nome de usuário (ou saudação) ao contexto
    context = {'username': username}
    return render(request, 'core/home.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core/signUp.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'core/signIn.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')
