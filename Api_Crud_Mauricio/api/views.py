from rest_framework import viewsets

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
from .responses import StandardResponseMixin

# Crud de tabla Sede (GET, POST, PUT, DELETE)
class SedeViewSet(StandardResponseMixin, viewsets.ModelViewSet):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer


# Crud de tabla Organizador (GET, POST, PUT, DELETE)
class OrganizadorViewSet(StandardResponseMixin, viewsets.ModelViewSet):
    queryset = Organizador.objects.all()
    serializer_class = OrganizadorSerializer


# Crud de tabla Evento (GET, POST, PUT, DELETE)
class EventoViewSet(StandardResponseMixin, viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer


# Crud de tabla Asistente (GET, POST, PUT, DELETE)
class AsistenteViewSet(StandardResponseMixin, viewsets.ModelViewSet):
    queryset = Asistente.objects.all()
    serializer_class = AsistenteSerializer


# Crud de tabla Inscripcion (GET, POST, PUT, DELETE)
class InscripcionViewSet(StandardResponseMixin, viewsets.ModelViewSet):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer


# Crud de tabla Pago (GET, POST, PUT, DELETE)
class PagoViewSet(StandardResponseMixin, viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer


# Crud de tabla Conferencia (GET, POST, PUT, DELETE)
class ConferenciaViewSet(StandardResponseMixin, viewsets.ModelViewSet):
    queryset = Conferencia.objects.all()
    serializer_class = ConferenciaSerializer


# Crud de tabla Patrocinador (GET, POST, PUT, DELETE)
class PatrocinadorViewSet(StandardResponseMixin, viewsets.ModelViewSet):
    queryset = Patrocinador.objects.all()
    serializer_class = PatrocinadorSerializer
