from rest_framework import filters, viewsets

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
from .logging_mixins import OperationLoggingMixin
from .responses import StandardResponseMixin


class BaseApiViewSet(OperationLoggingMixin, StandardResponseMixin, viewsets.ModelViewSet):
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    ordering = ['-fecha_creacion']


# Crud de tabla Sede (GET, POST, PUT, DELETE)
class SedeViewSet(BaseApiViewSet):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer


# Crud de tabla Organizador (GET, POST, PUT, DELETE)
class OrganizadorViewSet(BaseApiViewSet):
    queryset = Organizador.objects.all()
    serializer_class = OrganizadorSerializer


# Crud de tabla Evento (GET, POST, PUT, DELETE)
class EventoViewSet(BaseApiViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer


# Crud de tabla Asistente (GET, POST, PUT, DELETE)
class AsistenteViewSet(BaseApiViewSet):
    queryset = Asistente.objects.all()
    serializer_class = AsistenteSerializer


# Crud de tabla Inscripcion (GET, POST, PUT, DELETE)
class InscripcionViewSet(BaseApiViewSet):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer


# Crud de tabla Pago (GET, POST, PUT, DELETE)
class PagoViewSet(BaseApiViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer


# Crud de tabla Conferencia (GET, POST, PUT, DELETE)
class ConferenciaViewSet(BaseApiViewSet):
    queryset = Conferencia.objects.all()
    serializer_class = ConferenciaSerializer


# Crud de tabla Patrocinador (GET, POST, PUT, DELETE)
class PatrocinadorViewSet(BaseApiViewSet):
    queryset = Patrocinador.objects.all()
    serializer_class = PatrocinadorSerializer
