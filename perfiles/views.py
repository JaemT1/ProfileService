# perfiles/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Perfil
from .serializers import PerfilSerializer


class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    permission_classes = [AllowAny]  # Permitir acceso sin autenticación

    def create(self, request, *args, **kwargs):
        usuario_id = request.data.get('usuario_id')
        if not usuario_id:
            return Response({"detail": "usuario_id es requerido"}, status=status.HTTP_400_BAD_REQUEST)

        perfil, created = Perfil.objects.get_or_create(usuario_id=usuario_id)
        serializer = PerfilSerializer(perfil, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
