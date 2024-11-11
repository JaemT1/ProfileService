# perfiles/models.py
# perfiles/models.py
from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil", null=True, blank=True)
    pagina_personal = models.URLField(max_length=255, blank=True, null=True)
    apodo = models.CharField(max_length=50, blank=True, null=True)
    informacion_publica = models.BooleanField(default=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    organizacion = models.CharField(max_length=100, blank=True, null=True)
    pais_residencia = models.CharField(max_length=100, blank=True, null=True)
    redes_sociales = models.JSONField(default=dict, blank=True)


    def __str__(self):
        return f"Perfil de {self.usuario.username}"