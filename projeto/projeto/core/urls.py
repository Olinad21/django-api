from rest_framework import routers
from django.urls import path,include
from .api.viewsets import DadosViewSet,DispositivoViewSet
from . import views

router = routers.DefaultRouter()
app_name='core'
router = routers.DefaultRouter()
router.register(r'dados', DadosViewSet)
router.register(r'dispositivos', DispositivoViewSet)

urlpatterns = [
   path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
