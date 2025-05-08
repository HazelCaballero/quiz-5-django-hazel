from django.db import models

class Pacientes(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=100, null=False)
    sexo = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino')], null=False)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField(null=False)
    cedula = models.CharField(max_length=15, unique=True, null=False)
    
    def __str__(self):
        return self.nombre 

class Especialidades(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre
    
class Doctores(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=100, null=False)
    anios_experiencia = models.IntegerField()
    telefono = models.CharField(max_length=15, null=False)
    direccion = models.CharField(max_length=255, null=False)
    email = models.EmailField()
    fecha_nacimiento = models.DateField(null=False)
    cedula = models.CharField(max_length=15, unique=True, null=False)
    Especialidades = models.ManyToManyField('Especialidades', through="DoctoresEspecialidadeses")  # Corrige el nombre del modelo intermedio
    
    def __str__(self):
        return f" {self.nombre} {self.anios_experiencia} "

class Citas(models.Model):
    paciente = models.ForeignKey('Pacientes', on_delete=models.CASCADE)
    doctor = models.ForeignKey('Doctores', on_delete=models.CASCADE)
    fecha = models.DateField(null=False)
    hora = models.TimeField(null=False)
    motivo = models.TextField(null=False)
    estado = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('Confirmada', 'Confirmada'), ('Cancelada', 'Cancelada')], default='Pendiente')
    observaciones = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"Cita de {self.paciente} con {self.doctor}"

class DoctoresEspecialidadeses(models.Model):
    doctor = models.ForeignKey('Doctores', on_delete=models.CASCADE)
    Especialidades = models.ForeignKey(Especialidades, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.doctor} - {self.Especialidades}"

