# perfiles/serializers.py
from rest_framework import serializers
from .models import Perfil

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = [

            'id','pagina_personal', 'apodo', 'informacion_publica',
            'direccion', 'biografia', 'organizacion',
            'pais_residencia', 'redes_sociales'
        ]