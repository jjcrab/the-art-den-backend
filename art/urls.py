from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtworkViewSet, StudentViewSet

router = DefaultRouter()
router.register(r'artworks', ArtworkViewSet, basename='artwork')
router.register(r'students', StudentViewSet, basename='student')

urlpatterns = router.urls
