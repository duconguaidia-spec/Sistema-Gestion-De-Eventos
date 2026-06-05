from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    SedeViewSet,
    OrganizadorViewSet,
    EventoViewSet,
    AsistenteViewSet,
    InscripcionViewSet,
    PagoViewSet,
    ConferenciaViewSet,
    PatrocinadorViewSet,
)
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = DefaultRouter()

# Registro de endpoints del api
router.register(r'sedes', SedeViewSet)
router.register(r'organizadores', OrganizadorViewSet)
router.register(r'eventos', EventoViewSet)
router.register(r'asistentes', AsistenteViewSet)
router.register(r'inscripciones', InscripcionViewSet)
router.register(r'pagos', PagoViewSet)
router.register(r'conferencias', ConferenciaViewSet)
router.register(r'patrocinadores', PatrocinadorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]