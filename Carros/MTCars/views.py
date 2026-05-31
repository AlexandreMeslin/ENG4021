from django.shortcuts import render
from MTCars.models import MTCars

# Create your views here.

def searchf(request):
    if request.method == 'GET':
        carros = MTCars.objects.all()  # Aqui você pode obter todos os carros ou aplicar algum filtro inicial
        return render(request, 'home.html', {'carros': carros})
    else:
        search_query = request.POST.get('search')
        # Aqui você pode adicionar a lógica para filtrar os carros com base na pesquisa
        carros = MTCars.objects.filter(name__icontains=search_query)
        # contexto é uma variável do tipo dicionário 
        # que armazena os dados a serem enviados para o template.
        # No template, você pode acessar esses dados usando as chaves do dicionário.
        contexto = {
            'search_query': search_query,   # o texto pesquisado
            'carros': carros                # os resultados da pesquisa
        }
        # No meu caso, eu mostro a mesma página,
        # mas você pode usar outro template para mostrar uma página diferente.
        # Basta trocar o nome do arquivo HTML no parâmetro da função render a seguir.
        return render(request, 'home.html', contexto)

def detalhes(request, carro_id):
    carro = MTCars.objects.get(id=carro_id)
    # Ao criar uma entrada no dicionário contexto com o nome carro (string constante),
    # você vai criar uma variável carro no template associado pela função render.
    # Essa variável é um objeto carro, com todas as suas propriedades.
    contexto = {
        'carro': carro
    }
    return render(request, 'detalhes.html', contexto)
