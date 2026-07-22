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

<<<<<<< HEAD
    obra = get_object_or_404(Obra, id=id)
=======
    obra = get_object_or_404(Obra , id=id   )
>>>>>>> 801b4adecbe425b0fa867953bf92ad593bd6ce9e

    context = {
        "obra": obra,
    }

    return render(
        request,
        "catalogo/detalhes.html",
        context
    )