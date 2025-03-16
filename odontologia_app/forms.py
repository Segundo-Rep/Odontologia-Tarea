from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import *

class RepresentanteForm(forms.ModelForm):
    class Meta:
        model = Representante
        fields = ['cedula', 'nombre']

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nombre = forms.CharField(max_length=100, required=True)

    class Meta:
        model = get_user_model()
        fields = ['email', 'nombre', 'password1', 'password2']
class HistoriaMedicaForm(forms.ModelForm):
    class Meta:
        model = HistoriaMedica
        fields = ['paciente']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['paciente'].label_from_instance = lambda obj: f"{obj.nombre} (Cédula: {obj.cedula})"
class LoginForm(forms.Form):
    email = forms.EmailField(label="Correo Electrónico")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

class AnamnesisForm(forms.ModelForm):
    class Meta:
        model = Anamnesis
        fields = ['diabetes', 'tbc', 'hipertension', 'artritis', 'alergias', 
                  'neuralgias', 'hemorragias', 'hepatitis', 'sinusitis', 
                  'trastornos_mentales', 'enfermedades_eruptivas', 
                  'enfermedades_renales', 'parotiditis']


class AntecedentesFamiliaresForm(forms.ModelForm):
    class Meta:
        model = AntecedentesFamiliares
        fields = ['tipo', 'descripcion']


class HabitosForm(forms.ModelForm):
    class Meta:
        model = Habitos
        fields = ['descripcion']
