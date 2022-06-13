from django.urls import path
from AppFinal import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Home"),
    path('tarifario', views.tarifario, name="tarifario"),
    path('cobertura', views.cobertura, name="cobertura"),
    path('contacto', views.contacto, name="Contacto"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

