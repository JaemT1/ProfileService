# profiles/urls.py
from rest_framework.routers import DefaultRouter
from .views import PerfilViewSet
from django.urls import path
from .views import PerfilViewSet
from .views import custom_health_check
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiles', PerfilViewSet, basename='profile')
urlpatterns = [
    path('health/', custom_health_check, name='health'),  # Ruta personalizada para el health check
]

# Incluimos las rutas del router para los métodos CRUD de Perfil
urlpatterns += router.urls