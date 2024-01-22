from django.shortcuts import render
from .models import Task
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import * 
from .forms import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# Create your views here.



# Create your views here.



@login_required
def index(request):
    # template = loader.get_template("app/index.html")
    db_data = Task.objects.all()
    context = {
        "db_data": db_data[::-1],
        "update": None
    }
    # return HttpResponse(template.render(context, request))
    return render(request, "app/index.html", context)


def insert(request):
    try:
        task_subject = request.POST["subject"]
        task_description = request.POST["description"]
        if task_subject == "" or task_description == "":
            raise ValueError("El texto no puede estar en vacio.")
        db_data = Task(subject=task_subject, description=task_description)
        db_data.save()
        return HttpResponseRedirect(reverse("index")) 
    except ValueError as err:
        print(err)
        return HttpResponseRedirect(reverse("index")) 


def update(request):
    task_id = request.POST["id"]
    task_subject = request.POST["subject"]
    task_description = request.POST["description"]
    db_data = Task.objects.get(pk=task_id)
    db_data.subject = task_subject
    db_data.description = task_description
    db_data.save()
    return HttpResponseRedirect(reverse("index")) 


def update_form(request, task_id):
    db_data = Task.objects.all()
    db_data_only = Task.objects.get(pk=task_id)
    print(db_data_only)
    context = {
        "db_data": db_data[::-1],
        "update": db_data_only
    }
    return render(request, "app/index.html", context)


def delete(request, task_id):
    db_data = Task.objects.filter(id=task_id)
    db_data.delete()
    return HttpResponseRedirect(reverse("index")) 

def registrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Guardar el nuevo usuario y autenticarlo
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = UserCreationForm()
    
    # Contexto para renderizar la plantilla de registro de usuario
    return render(request, 'registration/registrar_usuario.html', {'form': form})
def ingresar(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Credenciales incorrectas. Por favor, intenta de nuevo.')
        else:
            messages.error(request, 'Credenciales incorrectas. Por favor, intenta de nuevo.')
    else:
        form = AuthenticationForm()

    # Contexto para renderizar la plantilla de inicio de sesión
    return render(request, 'registration/login.html', {'form': form})
