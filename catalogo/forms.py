<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div class="container">
        <h1>Cadastrar Obra</h1>
        <form method="post">
           {% csrf_token %}
           {% form.as_p %}
           <button class="bnt" type="submit">Salvar,</button>
        </form>
        <a href="{% url 'catalogo:index' %}">Volta para o catálogo</a>
    </div>
    
</body>
</html>

dentro do forms: 



from django import forms
from .models import Obra

class ObraForm(forms.ModelForm):
    class Meta:
        model: Obra
        fields: ["titulo", "tipo", "ano", "genero", "descricao"]



dentro das views:


def cadastrar_obra(request):

    if request.method == "POST":
        form = ObraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("catalogo.html")
    else:
        form = ObraForm()

    context = {"form": form}
    return render(request, "catalogo/cadastro.html". context)