from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    '''
    View function for home page of site.
    Renders the home.html template.
    '''
    return render(request, 'MeuSite/home.html')

@login_required
def secreta(request):
    '''
    View para renderizar a página secreta que é o template secreta.html
    Esse view é básico para renderizar páginas
    Apenas tenho que trocar o nome da função e o nome do template
    '''
    return render(request, 'MeuSite/secreta.html')
