from django.shortcuts import render, get_object_or_404
from .models import Obra

def index(request):
    obras = Obra.objects.all()
    context = {
        "obras": obras,
    }

    return render(
        request,
        "catalogo/index.html",
        context
    )


def detalhes(request, id):

    obra = get_object_or_404(Obra , id=id   )

    context = {
        "obra": obra,
    }

    return render(
        request,
        "catalogo/detalhes.html",
        context
    )