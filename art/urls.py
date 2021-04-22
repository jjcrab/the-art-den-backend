from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtworkViewSet, StudentViewSet, StudentuserViewSet


router = DefaultRouter()
router.register(r'artworks', ArtworkViewSet, basename='artwork')
router.register(r'students', StudentViewSet, basename='student')
router.register(r'studentartworks', StudentuserViewSet,
                basename='studentartworks')

urlpatterns = router.urls
