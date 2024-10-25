from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WardrobeItemViewSet

router = DefaultRouter()
router.register(r'items', WardrobeItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]