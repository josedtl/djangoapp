from django.shortcuts import render, redirect, get_object_or_404
from .models import PersonaNaturalItem
from .forms import PersonaNaturalForm


def listar_personas_naturales(request):
    personas = PersonaNaturalItem.objects.all()
    if personas.count == 0:
        personas = []
    return render(request, "listar_personas_naturales.html", {"personas": personas})


def crear_persona_natural(request):
    if request.method == "POST":
        form = PersonaNaturalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_personas_naturales")
    else:
        form = PersonaNaturalForm()
    return render(request, "crear_persona_natural.html", {"form": form})


def editar_persona_natural(request, persona_id):
    persona = get_object_or_404(PersonaNaturalItem, PersonaNaturalId=persona_id)
    if request.method == "POST":
        form = PersonaNaturalForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect("listar_personas_naturales")
    else:
        form = PersonaNaturalForm(instance=persona)
    return render(request, "editar_persona_natural.html", {"form": form})


def eliminar_persona_natural(request, persona_id):
    persona = get_object_or_404(PersonaNaturalItem, PersonaNaturalId=persona_id)
    persona.delete()
    return redirect("listar_personas_naturales")
