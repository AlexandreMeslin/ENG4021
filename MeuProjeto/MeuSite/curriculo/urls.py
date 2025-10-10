from django.urls import path
from . import views

app_name = 'curriculo'

urlpatterns = [
    # essa rota pode ser acessada em /curriculo/spiff/
    # ou seja, /curriculo/ + spiff/
    # o link para essa rota pode ser criado usando o nome 'curriculo_spiff'
    # Exemplo: {% url 'curriculo:curriculo_spiff' %}
    path('spiff/', views.curriculo_spiff, name='curriculo_spiff'),
    # essa rota pode ser acessada em /curriculo/spiff/v2/
    path('spiff/v2/', views.curriculo_spiff_v2, name='curriculo_spiff_v2'),
]
