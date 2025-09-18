from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import GarcomViewSet, GerenteViewSet

router = DefaultRouter()

router.register(r'garcom', GarcomViewSet)
router.register(r'gerente', GerenteViewSet)


urlpatterns = router.urls