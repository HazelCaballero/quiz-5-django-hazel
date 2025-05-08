from django import forms
from .models import Pacientes

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = '__all__'

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if len(telefono) < 10:
            raise forms.ValidationError("El número de teléfono debe tener al menos 10 dígitos.")
        return telefono