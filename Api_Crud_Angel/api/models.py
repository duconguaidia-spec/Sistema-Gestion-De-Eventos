from django.db import models

# Create your models here.
class Sede(models.Model):
    id_sede = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)
    ciudad = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=150, null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'sedes'


class Organizador(models.Model):
    id_organizador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    empresa = models.CharField(max_length=200, null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = 'organizadores'


class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=300)
    descripcion = models.TextField(null=True, blank=True)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    capacidad_maxima = models.IntegerField()
    id_sede = models.IntegerField()
    id_organizador = models.IntegerField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'eventos'


class Asistente(models.Model):
    id_asistente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    documento_identidad = models.CharField(max_length=50, null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = 'asistentes'


class Inscripcion(models.Model):
    id_inscripcion = models.AutoField(primary_key=True)
    id_evento = models.IntegerField()
    id_asistente = models.IntegerField()
    estado = models.CharField(max_length=20, default='Pendiente')
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Inscripcion {self.id_inscripcion}"

    class Meta:
        db_table = 'inscripciones'


class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    id_inscripcion = models.IntegerField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50, null=True, blank=True)
    estado = models.CharField(max_length=20, default='Pendiente')
    referencia = models.CharField(max_length=100, null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pago {self.id_pago}"

    class Meta:
        db_table = 'pagos'


class Conferencia(models.Model):
    id_conferencia = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=300)
    descripcion = models.TextField(null=True, blank=True)
    ponente = models.CharField(max_length=200, null=True, blank=True)
    sala = models.CharField(max_length=100, null=True, blank=True)
    fecha_hora_inicio = models.DateTimeField(null=True, blank=True)
    duracion_minutos = models.IntegerField(null=True, blank=True)
    id_evento = models.IntegerField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'conferencias'


class Patrocinador(models.Model):
    id_patrocinador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    logo = models.CharField(max_length=255, null=True, blank=True)
    sitio_web = models.CharField(max_length=255, null=True, blank=True)
    contacto = models.CharField(max_length=200, null=True, blank=True)
    email_contacto = models.CharField(max_length=150, null=True, blank=True)
    nivel = models.CharField(max_length=20, null=True, blank=True)
    monto_aporte = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    id_evento = models.IntegerField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'patrocinadores'