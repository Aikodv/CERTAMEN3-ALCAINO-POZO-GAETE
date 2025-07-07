from django.contrib import admin
from .models import Usuario, Lugar, Categoria, Profesor, Taller
from django.contrib.auth.admin import UserAdmin

@admin.register(Usuario)
class CustomUsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ('username', 'email', 'tipo', 'is_staff', 'is_superuser')
    list_filter = ('tipo', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('tipo',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('tipo',)}),
    )

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
    list_display = ('titulo', 'fecha', 'estado', 'profesor', 'lugar', 'categoria')
    list_filter = ('estado', 'fecha', 'categoria')
    search_fields = ('titulo', 'profesor__nombre_completo')
    ordering = ('fecha',)
    actions = ['marcar_aceptado', 'marcar_rechazado']

    @admin.action(description='Marcar como Aceptado')
    def marcar_aceptado(self, request, queryset):
        updated = queryset.update(estado='aceptado')
        self.message_user(request, f"{updated} taller(es) marcados como aceptado.")

    @admin.action(description='Marcar como Rechazado')
    def marcar_rechazado(self, request, queryset):
        updated = queryset.update(estado='rechazado')
        self.message_user(request, f"{updated} taller(es) marcados como rechazado.")
