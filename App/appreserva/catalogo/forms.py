from django import forms
from .models import PersonaNaturalItem


class PersonaNaturalForm(forms.ModelForm):
    class Meta:
        model = PersonaNaturalItem

        fields = [
            "NumDocumento",
            "Nombres",
            "ApellidoPaterno",
            "ApellidoMaterno",
            "FechaNacimiento",
            "Direccion",
            "Correo",
            "Telefono",
        ]

    widgets = {
        "NumDocumento": forms.TextInput(attrs={"type": "text"}),
        "Nombres": forms.TextInput(attrs={"type": "text"}),
        "ApellidoPaterno": forms.TextInput(attrs={"type": "text"}),
        "ApellidoMaterno": forms.TextInput(attrs={"type": "text"}),
        "FechaNacimiento": forms.DateInput(attrs={"type": "date"}),
        "Direccion": forms.TextInput(attrs={"type": "text"}),
        "Correo": forms.EmailInput(attrs={"type": "email"}),
        "Telefono": forms.TextInput(attrs={"type": "tel"}),
    }

    labels = {
        "NumDocumento": "Número de Documento",
        "Nombres": "Nombres",
        "ApellidoPaterno": "Apellido Paterno",
        "ApellidoMaterno": "Apellido Materno",
        "FechaNacimiento": "Fecha de Nacimiento",
        "Direccion": "Dirección",
        "Correo": "Correo Electrónico",
        "Telefono": "Teléfono",
    }
