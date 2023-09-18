from django import forms

class PersonaNatural(forms.Form):
    NumDocumento = forms.CharField(max_length=20, label='Número de Documento')
    Nombres = forms.CharField(max_length=100, label='Nombres')
    ApellidoPaterno = forms.CharField(max_length=100, label='Apellido Paterno')
    ApellidoMaterno = forms.CharField(max_length=100, label='Apellido Materno')
    FechaNacimiento = forms.DateField(
        label='Fecha de Nacimiento',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    Direccion = forms.CharField(max_length=200, label='Dirección')
    Correo = forms.EmailField(label='Correo Electrónico')
    Telefono = forms.CharField(max_length=15, label='Teléfono')
