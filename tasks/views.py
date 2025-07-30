from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.db import IntegrityError


# Aquí se definen las vistas de la aplicación "tasks"


def home(request):
    # Renderiza la plantilla "home.html" cuando se accede a la página principal
    return render(request, "home.html")


def signup(request):
    # Vista para el registro de nuevos usuarios

    if request.method == "GET":
        # Si la petición es GET, muestra el formulario de registro vacío
        return render(request, "signup.html",
                      {
                          "form": UserCreationForm
                      })
    else:
        # Si la petición es POST, procesa los datos enviados por el usuario
        if request.POST["password1"] == request.POST["password2"]:
            # Verifica que las contraseñas coincidan
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],

                )
                user.save()
                # Inicia sesión automáticamente al registrarse
                login(request, user)
                return redirect("tasks")  # Redirige a la página de tareas
            except IntegrityError:
                # Si las contraseñas no coinciden, muestra un mensaje de error
                render(
                    request,
                    "signup.html",
                    {
                        "form": UserCreationForm,
                        "error": "El nombre de usuario ya está en uso"
                    })
        return render(
            request,
            "signup.html",
            {
                "form": UserCreationForm,
                "error": "La contraseña no coincide"
            })


def tasks(request):
    # Renderiza la plantilla "tasks.html" para mostrar las tareas del usuario
    return render(request, "tasks.html")
