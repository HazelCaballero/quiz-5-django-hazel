from .models import Pacientes, Especialidades, Doctores, Citas, DoctoresEspecialidadeses
from rest_framework import serializers
from datetime import date

class PacientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = '__all__'

    def validate_nombre(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return value

    def validate_apellido(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("El apellido debe tener al menos 3 caracteres.")
        return value

class EspecialidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidades
        fields = '__all__'

    def validate_descripcion(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("La descripción debe tener al menos 5 caracteres.")
        return value

class DoctoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctores
        fields = '__all__'

    def validate_nombre(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return value

    def validate_apellido(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("El apellido debe tener al menos 3 caracteres.")
        return value

    def validate_anios_experiencia(self, value):
        if value < 0:
            raise serializers.ValidationError("Los años de experiencia deben ser igual o mayor a 0.")
        return value

class CitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citas
        fields = '__all__'

    def validate_fecha(self, value):
        if value < date.today():
            raise serializers.ValidationError("La fecha de la cita no puede ser un día anterior a la fecha actual.")
        return value

class DoctoresEspecialidadesesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctoresEspecialidadeses
        fields = '__all__'
