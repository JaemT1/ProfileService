# profiles/urls.py
from rest_framework.routers import DefaultRouter
from .views import PerfilViewSet

router = DefaultRouter()
router.register(r'profiles', PerfilViewSet, basename='profile')

urlpatterns = router.urls
