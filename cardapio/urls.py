from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ComandaViewSet

router = DefaultRouter()
router.register(r'comandas', ComandaViewSet)
router.register(r'mesas', ComandaViewSet, basename='mesa')


urlpatterns = router.urls