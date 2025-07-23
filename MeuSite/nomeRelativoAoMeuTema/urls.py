from django.urls.conf import path
from nomeRelativoAoMeuTema import views

app_name = "nomeRelativoAoMeuTema"

urlpatterns = [
    path("home/", views.home, name='homepage'),
    path("insereCarro/", views.insereCarro, name='insereCarro'),
]
