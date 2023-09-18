from django.shortcuts import render, redirect
from .forms import MiFormulario

def mi_vista(request):
    if request.method == 'POST':
        formulario = MiFormulario(request.POST)
        if formulario.is_valid():
            # Procesa los datos del formulario aquí
            # Por ejemplo, guarda los datos en la base de datos
            formulario.save()
            return redirect('exito')  # Redirige a una página de éxito
    else:
        formulario = MiFormulario()
    
    return render(request, 'mi_template.html', {'formulario': formulario})
