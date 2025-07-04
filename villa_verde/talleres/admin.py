from django.contrib import admin
from .models import Usuario, Lugar, Categoria, Profesor, Taller
from django.contrib.auth.admin import UserAdmin

admin.site.register(Usuario, UserAdmin)
admin.site.register(Lugar)
admin.site.register(Categoria)
admin.site.register(Profesor)
admin.site.register(Taller)
