from django.shortcuts import render, HttpResponse
from .forms import FormularioContacto
from .models import Contacto



# Create your views here.
def home(request):
    return render(request, "AppFinal/home.html")

def tarifario(request):
    return render(request, "AppFinal/tarifario.html")

def cobertura(request):
    return render(request, "AppFinal/cobertura.html")

def busqueda(request):
    return render(request,"AppFinal/busqueda.html")

def contacto(request):
    data={
        'form': FormularioContacto
    }
    if request.method=="POST":

        miFormulario=FormularioContacto(data=request.POST)

        if miFormulario.is_valid():
            miFormulario.save()
            data["mensaje"] = "Sus datos fueron enviados con éxito"
        else:
            data["form"] = miFormulario

    return render(request, "AppFinal/contacto.html", data)


def buscar(request):
    
    if request.GET["nombre"]:
        nombre=request.GET['nombre']
        contactos=Contacto.objects.filter(nombre__icontains=nombre)

        return render(request, "AppFinal/resultadoBusqueda.html", {"contactos": contactos, "nombre": nombre})
    else:

        respuesta="No enviaste datos"
    return HttpResponse(respuesta)