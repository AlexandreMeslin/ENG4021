from django.shortcuts import render
from .forms import MTCarsForm
from django.http import HttpResponse
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    return render(request, "nomeRelativoAoMeuTema/home.html")

def insereCarro(request):
    if request.method == 'GET':
        # If the request method is GET, render the form
        contexto = { "form": MTCarsForm(), }
        return render(request, "nomeRelativoAoMeuTema/insereCarro.html", contexto)
    else:
        # If the request method is POST, process the form
        form = MTCarsForm(request.POST)
        if form.is_valid():
            form.save()
            # coloque aqui o nome do link para o qual você quer redirecionar em caso de sucesso
            return HttpResponseRedirect(reverse_lazy('nomeRelativoAoMeuTema:home'))
        else:
            # em caso de erro, renderize o formulário novamente com os erros
            return render(request, "nomeRelativoAoMeuTema/insereCarro.html", {"form": form})
