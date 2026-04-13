import tareas
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    tareas = [
        "Estudiar python",
        "Hacer ejercicio",
        "Leer un libro"
    ]

    texto = "<h1>Lista de tareas</h1>"

    for tarea in tareas:
        texto += f"<p>{tarea}</p>"

    return HttpResponse(texto)