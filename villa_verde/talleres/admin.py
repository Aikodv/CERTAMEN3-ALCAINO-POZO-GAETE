from django.contrib import admin
from .models import Usuario, Lugar, Categoria, Profesor, Taller
from django.contrib.auth.admin import UserAdmin


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'email', 'tipo', 'is_staff', 'is_superuser')
    list_filter = ('tipo', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')


@admin.register(Lugar)
class LugarAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion')
    search_fields = ('nombre',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)


@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo',)
    search_fields = ('nombre_completo',)


@admin.register(Taller)
class TallerAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'duracion_horas', 'estado', 'profesor', 'lugar', 'categoria')
    list_filter = ('estado', 'fecha', 'categoria')
    search_fields = ('titulo', 'profesor__nombre_completo')
    ordering = ('fecha',)
