from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms
from .models import Taller

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email') 

class TallerPropuestoForm(forms.ModelForm):
    class Meta:
        model = Taller
        fields = ['titulo', 'fecha', 'duracion_horas', 'profesor', 'lugar', 'categoria']