from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PedidoViewSet, ComandaViewSet

router = DefaultRouter()

router.register(r'pedido', PedidoViewSet)
router.register(r'comanda', ComandaViewSet)

urlpatterns = router.urls