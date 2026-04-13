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

    return render(request, "inicio.html", {"tareas": tareas})