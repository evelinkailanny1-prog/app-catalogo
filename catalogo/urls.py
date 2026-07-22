from django.urls import path
from . import views

app_name = "catalogo"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/", views.detalhes, name="detalhes"),
    path("cadastrar/", views.cadastrar_obra, name="cadastrar_obra")
]