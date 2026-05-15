from django.shortcuts import render

def home(request):
    '''
    View function for home page of site.
    Renders the home.html template.
    '''
    return render(request, 'MeuSite/home.html')