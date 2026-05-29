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
    View que eu criei para renderizar a minha página secreta.
    Esse view é semelhante ao view home, 
    apenas modifique o nome da função (!) e o nome do template.
    '''
    return render(request, 'MeuSite/secreta.html')