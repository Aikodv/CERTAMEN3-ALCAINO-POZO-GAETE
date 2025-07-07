from django.urls import path
from . import views
from . import api_views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('proponer/', views.proponer_taller_view, name='proponer_taller'),
    path('talleres/', api_views.listar_talleres_api, name='listar_talleres_api'),
    
]
