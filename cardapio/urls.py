from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MesaViewSet, CardapioViewSet, ItemViewSet, CategoriaViewSet

router = DefaultRouter()
router.register(r'cardapio', CardapioViewSet)
router.register(r'mesa', MesaViewSet)
router.register(r'item', ItemViewSet)
router.register(r'categoria', CategoriaViewSet)


urlpatterns = router.urls