from django.shortcuts import render

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