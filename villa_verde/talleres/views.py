from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Taller, Categoria
from django.utils import timezone
from .forms import CustomUserCreationForm
from .forms import TallerPropuestoForm
def home(request):
    categoria_id = request.GET.get('categoria')
    talleres = Taller.objects.filter(
        estado='aceptado',
        fecha__gte=timezone.now()
    )
    if categoria_id:
        talleres = talleres.filter(categoria_id=categoria_id)
    categorias = Categoria.objects.all()
    return render(request, 'talleres/home.html', {
        'talleres': talleres,
        'categorias': categorias,
        'categoria_actual': categoria_id
    })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'talleres/login.html', {'form': form})

@login_required
def proponer_taller_view(request):
    if request.user.tipo != 'junta':
        return redirect('home')  # o mostrar un error

    if request.method == 'POST':
        form = TallerPropuestoForm(request.POST)
        if form.is_valid():
            taller = form.save(commit=False)
            taller.estado = 'pendiente'
            taller.save()
            return redirect('home')
    else:
        form = TallerPropuestoForm()
    return render(request, 'talleres/proponer_taller.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'talleres/register.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile_view(request):
    return render(request, 'talleres/profile.html')