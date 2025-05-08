Se le ha encargado realizar el desarrollo de una API para un sistema de gestión
hospitalaria utilizando Django REST Framework. El objetivo de este quiz es
implementar un backend funcional que gestione distintos recursos del sistema
hospitalario asi como potenciar sus habilidades para la creación de un API, este quiz le
ayudara como practica para su proyecto final.
Requisitos del sistema:
1. Crear cinco modelos (tablas):
o Pacientes: Información básica de los pacientes (nombre, edad, etc.)
o Doctores: Datos de los doctores (nombre, años de experiencia, etc.)
o Especialidades: Listado de Especialidades médicas (Cardiología,
Pediatría, etc.)
o Citas: Representa una cita médica entre un paciente y un doctor. Debe
tener campos como fecha, hora y motivo.
o DoctoresEspecialidades: Tabla intermedia personalizada que relacione
doctores con sus Especialidades.

2. Relaciones esperadas:
o Un doctor puede tener múltiples Especialidades y una Especialidades puede
tener varios doctores (ManyToMany con tabla intermedia).
o Una cita debe relacionar a un doctor y a un paciente (ForeignKey en
ambos casos).

3. Serializers:
o Crear serializers para cada modelo, incluyendo relaciones anidadas
cuando sea necesario.
o Realizar validaciones de los datos usando raise
4. Vistas:
o Implementar vistas para cada modelo usando las clases genéricas
ListCreateAPIView y RetrieveUpdateDestroyAPIView.

5. URLs:
o Configurar las rutas para acceder a cada uno de los endpoints.

6. Pruebas en Postman , Insomia:
o Realizar pruebas de los endpoints para verificar que se puede hacer:
 GET (listar y obtener elementos)
 POST (crear registros)
 PUT/PATCH (actualizar registros)
 DELETE (eliminar registros)

Objetivo:
Al finalizar, se debe contar con una API REST funcional capaz de gestionar la
información del hospital, permitiendo CRUD completo para todos los modelos y
relaciones correctamente implementadas.