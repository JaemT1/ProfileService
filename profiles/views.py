# perfiles/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Perfil
from .Serializers import ProfileSerializer
from django.http import JsonResponse
from health_check.views import MainView
from datetime import datetime
from .responses import ApiError, ApiSuccess

class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [AllowAny]  # Permitir acceso sin autenticación

    def create(self, request, *args, **kwargs):
        id_usuario = request.data.get('id_usuario')
        if not id_usuario:
            return Response({"detail": "id_usuario es requerido"}, status=status.HTTP_400_BAD_REQUEST)

        perfil, created = Perfil.objects.get_or_create(id_usuario=id_usuario)
        serializer = ProfileSerializer(perfil, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return ApiSuccess(
                status=status.HTTP_201_CREATED,
                success="CREATED",
                message="Perfil creado exitosamente",
                path=request.path
            )
        return ApiError(
            status=status.HTTP_400_BAD_REQUEST,
            error="BAD_REQUEST",
            message="Error al crear el perfil",
            path=request.path
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return ApiSuccess(
                status=status.HTTP_200_OK,
                success="UPDATED",
                message="Perfil actualizado exitosamente",
                path=request.path
            )
        return ApiError(
            status=status.HTTP_400_BAD_REQUEST,
            error="BAD_REQUEST",
            message="Error al actualizar el perfil",
            path=request.path
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return ApiSuccess(
            status=status.HTTP_200_OK,
            success="DELETED",
            message="Perfil eliminado exitosamente",
            path=request.path
        )


def custom_health_check(request):
    # Captura la respuesta del health check
    response = MainView.as_view()(request)

    # Crea un diccionario de respuesta JSON con estado y timestamps
    current_time = datetime.now().isoformat()
    response_data = {
        "checks": {
            "readiness": {
                "from": current_time,
                "status": "READY" if response.status_code == 200 else "NOT_READY"
            },
            "liveness": {
                "from": current_time,
                "status": "ALIVE" if response.status_code == 200 else "DOWN"
            }
        },
        "status": "UP" if response.status_code == 200 else "DOWN"
    }
    # Retorna la respuesta como JSON
    return JsonResponse(response_data)