from django.contrib import admin
from django.urls import path, include
from cardapio.urls import router as router_cardapio
from pedido.urls import router as router_pedido
from usuario.urls import router as router_usuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_cardapio.urls)),
    path('api/', include(router_pedido.urls)),
    path('api/', include(router_usuario.urls)),
]
