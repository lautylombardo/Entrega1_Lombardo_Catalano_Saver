from django.shortcuts import render, HttpResponse



# Create your views here.
def home(request):
    return render(request, "AppFinal/home.html")

def tarifario(request):
    return render(request, "AppFinal/tarifario.html")

def cobertura(request):
    return render(request, "AppFinal/cobertura.html")

def contacto(request):
    return render(request, "AppFinal/contacto.html")