from django.shortcuts import render
from website.models import *

# Create your views here.
def home(request):
    nome = EFA- ENGLISH FOR ALL 
    lema = Formando um futuro melhor
    numero = +55-11-98399-8381
    lista_de_cursos = [
        'Inglês',
        'Informática básica',
        'Francês',
        'Reforço Preparatórios Extra Curricular', 
    ]
    
    context = {
        'nome' = nome,
        'lema' = lema,
        'numero' = numero,
        'cursos' = lista_de_cursos,
    }

    return render(request, home.html, context)

def cursos(request):
    form = CursosForm(request.POST or None)
    if form.is_valid():
        form.save()
        context = {
            'msg' : "Você foi cadastrado com sucesso!!!"
        }
        return render(request, pedido.html, context)
        context = {
            'formulary':form
        }
        return render(request, pedido.html, context)
        