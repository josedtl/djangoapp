from django.shortcuts import render, redirect
from .forms import PersonaNatural
import requests


def mi_vista(request):
    if request.method == "POST":
        formulario = PersonaNatural(request.POST)

        print(formulario)
        if formulario.is_valid():
            # Procesa los datos del formulario aquí
            # Por ejemplo, guarda los datos en la base de datos
            datos = formulario
            print(datos.NumDocumento)
            api_url = "http://127.0.0.1:3000/apirest/personas/"
            data_to_send = {
                "PersonaNaturalId": 0,
                "NumDocumento": datos.NumDocumento,
                "Nombres": datos.Nombres,
                "ApellidoPaterno": datos.ApellidoPaterno,
                "ApellidoMaterno": datos.ApellidoMaterno,
                "FechaNacimiento": datos.FechaNacimiento,
                "Direccion": datos.Direccion,
                "Correo": datos.Correo,
                "Telefono": datos.Telefono,
                # Agregar otros campos si es necesario
            }
            response = requests.post(api_url, json=data_to_send)
            if (
                response.status_code == 200
            ):  # Cambia el código de estado según la respuesta esperada
                return redirect("exito")  # Redirige a una página de éxito
            else:
                return redirect("error")  # Redirige a una página de éxito
    else:
        formulario = PersonaNatural()

    return render(request, "mi_template.html", {"formulario": formulario})
