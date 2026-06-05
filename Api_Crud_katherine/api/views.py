from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Evento
from api.mixins import SoftDeleteMixin
from .serializers import EventoSerializer
from .permissions import SoloAdministrador

from .models import (
    Sede,
    Organizador,
    Evento,
    Asistente,
    Inscripcion,
    Pago,
    Conferencia,
    Patrocinador,
)

from .serializers import (
    SedeSerializer,
    OrganizadorSerializer,
    EventoSerializer,
    AsistenteSerializer,
    InscripcionSerializer,
    PagoSerializer,
    ConferenciaSerializer,
    PatrocinadorSerializer,
)

# Crud de tabla Sede (GET, POST, PUT, DELETE)
class SedeViewSet(
    SoftDeleteMixin,
    viewsets.ModelViewSet
):
    queryset = Sede.objects.filter(activo=True)
    serializer_class = SedeSerializer

# Crud de tabla Organizador (GET, POST, PUT, DELETE)
class OrganizadorViewSet(
    SoftDeleteMixin,
    viewsets.ModelViewSet
):
    queryset = Organizador.objects.filter(activo=True)
    serializer_class = OrganizadorSerializer
# Crud de tabla Evento (GET, POST, PUT, DELETE)
class EventoViewSet(
    SoftDeleteMixin,
    viewsets.ModelViewSet
):
    queryset = Evento.objects.filter(activo=True)
    serializer_class = EventoSerializer
    permission_classes = [SoloAdministrador]  # Requiere autenticación para acceder a los endpoints de Evento

# Crud de tabla Asistente (GET, POST, PUT, DELETE)
class AsistenteViewSet(
    SoftDeleteMixin,
    viewsets.ModelViewSet
):
    queryset = Asistente.objects.filter(activo=True)
    serializer_class = AsistenteSerializer
    permission_classes = [SoloAdministrador]  # Requiere autenticación para acceder a los endpoints de Asistente

# Crud de tabla Inscripcion (GET, POST, PUT, DELETE)
class InscripcionViewSet(
    SoftDeleteMixin,
    viewsets.ModelViewSet
):
    queryset = Inscripcion.objects.filter(activo=True)
    serializer_class = InscripcionSerializer
    permission_classes = [SoloAdministrador]  # Requiere autenticación para acceder a los endpoints de Inscripcion

# Crud de tabla Pago (GET, POST, PUT, DELETE)
class PagoViewSet(
    SoftDeleteMixin,
    viewsets.ModelViewSet
):
    queryset = Pago.objects.filter(activo=True)
    serializer_class = PagoSerializer
    permission_classes = [SoloAdministrador]  # Requiere autenticación para acceder a los endpoints de Pago

# Crud de tabla Conferencia (GET, POST, PUT, DELETE)
class ConferenciaViewSet(
    SoftDeleteMixin,
    viewsets.ModelViewSet
):
    queryset = Conferencia.objects.filter(activo=True)
    serializer_class = ConferenciaSerializer
    permission_classes = [SoloAdministrador]  # Requiere autenticación para acceder a los endpoints de Conferencia

# Crud de tabla Patrocinador (GET, POST, PUT, DELETE)
class PatrocinadorViewSet(
    SoftDeleteMixin,
    viewsets.ModelViewSet
):
    queryset = Patrocinador.objects.filter(activo=True)
    serializer_class = PatrocinadorSerializer
    permission_classes = [SoloAdministrador]  # Requiere autenticación para acceder a los endpoints de Patrocinador
