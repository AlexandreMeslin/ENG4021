# Roteiro CRUD-2

# Atividade Individual 3

> Toda atividade descrita nesse roteiro deve ser desenvolvida usando o seu repositório individual. **NÃO** use o repositório do seu time.

# Objetivo

Desenvolver um site usando o banco de carros `MTCars` para permitir uma consulta com filtro

## Passos

Abra o `Codespace` no seu repositório individual.

### Criar um projeto baseado no framework Django

Na raiz do seu repositório, crie um diretório chamado `Carros` e desça para esse diretório:

```bash
mkdir Carros
cd Carros
```

Crie o arquivo `requirements.txt` no diretório `Carros` e inclua os requisitos iniciais (apenas `django`)
Para realizar esse passo, você pode usar a interface gráfica do Codespace.

Crie e ative o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate
```

Resultado esperado: certifique-se de que o texto `(venv)` está no início do seu prompt.

Instale os requisitos:

```bash
pip install -r requirements.txt
```

Crie o projeto MTCars:

```bash
django-admin startproject MTCars
```

### Teste inicial

Desça para o diretório `MTCars` e migre o banco de dados:

```bash
cd MTCars/
python manage.py migrate
```

Crie um superusuário:

```bash
python manage.py createsuperuser
```

Certifique-se de que o superusuário foi criado corretamente: `Superuser created successfully.`.

Inclua as seguintes linhas no arquivo `MTCars.settings.py` para permitir acesso de qualquer lugar ao site e evitar erros relacionados a *CORS*:

```python
CORS_ALLOW_ALL_ORIGINS = True
CSRF_TRUSTED_ORIGINS = [
    'https://localhost:8000', 
    'http://localhost:8000',
]
```

Coloque o site no ar:

```bash
python manage.py runserver
```

Coloque as portas como publicas.
Use a aba ports para obter o endereço do seu site.
Use a interface adminitrativa para examinar o seu banco de dados, incluindo o caminho `/admin/` no final da URL do seu site.
Use as credenciais do superusuário que você acabou de criar.

### Criando uma aplicação dentro do seu site

> Se necessário, interrompa o servidor Django digitando `Ctrl+C` no terminal.

Utilizando o terminal, crie uma aplicação chamada `CarsApp`:

```bash
python manage.py startapp CarsApp
```

Registre as suas aplicações no arquivo `settings.py`:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'MTCars',   # acrescente essa linha
    'CarsApp',  # e essa linha também
]
```

Crie o modelo de dados para o nosso banco de dados de carros.
No diretório `CarsApp`, crie o arquivo `models.py` e inclua a seguinte classe para representar a nossa base de dados de carros:

```python
from django.db import models

# Create your models here.

class MTCars(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(db_column='NAME') # Field name made 
    mpg = models.FloatField(db_column='MPG') # Field name made 
    cyl = models.IntegerField(db_column='CYL') # Field name 
    disp = models.FloatField(db_column='DISP') # Field name 
    hp = models.IntegerField(db_column='HP') # Field name made 
    wt = models.FloatField(db_column='WT') # Field name made 
    qsec = models.FloatField(db_column='QSEC') # Field name 
    vs = models.IntegerField(db_column='VS') # Field name made 
    am = models.IntegerField(db_column='AM') # Field name made 
    gear = models.IntegerField(db_column='GEAR') # Field name 
    
    class Meta:
        managed = True
        db_table = 'MTCars'
        ordering = ['id']

    def __str__(self):
        '''
        Retorna a representação em string do objeto MTCars.
        Por exemplo, o que vai ser listado na 
        interface de admin.
        '''
        return "Modelo: " + self.name
```

Copie os arquivos `MTCars.sqlite3` e `CopiaBaseDados.py` para o diretório onde está o arquivo `db.sqlite3`.
Os arquivos estão disponíveis no nosso repositório, no mesmo lugar onde você achou esse arquivo que você está lendo agora.

Migre novamente a base de dados, mas dessa vez, crie um novo conjunto de migrações porque você criou um novo modelo:

> Sempre que você modificar algum arquivo `models.py`, você vai ter que realizar esse passo.

```bash
python manage.py makemigrations
python manage.py migrate
```

Certifique-se de que ambos os comandos executaram com sucesso.

Execute o comando a seguir para copiar os dados do banco de dados `MTCars.sqlite3` (que não vamos mais usar) para o bando de dados `db.sqlite3`:

> Esse passo não faz parte necessariamente da criação do banco de dados.
> Ele foi necessário porque os dados dos carros estão em outro arquivo.
> Nós estamos apenas passando os dados de um arquivo para o outro.
> Você poderia fazer a mesma coisa usando a interface administrativa do seu site, ou seja, acrescentando `/admin/` no final da *URL* do seu *site*.

```bash
python CopiaBaseDados.py
```

Resultado esperado:

```
--- INICIANDO CÓPIA DE DADOS MTCars ---
Conectando ao banco de origem: mtcars.sqlite3...
Leitura concluída. 32 registros lidos.
Conectando ao banco de destino: db.sqlite3...
Inserção concluída! 32 registros copiados para 'db.sqlite3'.
--- PROCESSO CONCLUÍDO ---
```

### Criando o template

Crie o diretório `templates/CarsApp` dentro do diretório `CarsApp`.
Crie o arquivo `home.html` no diretório `templates/CarsApp`.
Use o seguinte conteúdo:

```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista de Carros</title>
    <link rel="stylesheet" href="{% static 'CarsApp/css/estilo.css' %}">
</head>
<body>

    <h1>Lista de Carros</h1>

    <!-- 
    Esse é o formulário básico para busca.
    Você deve usar a tag form e colocar os campos referentes a busca dentro dela.
    Lembre-se de usar o atributo method para enviar o formulário como POST.
    Para o Django aceitar de volta o formulário, você tem que incluir o comando {% csrf_token %}
    Veja que o formulário deve ter um botão de envio também.
    Modifique os campos input e button para obter o aspecto que você quer.
    -->
    <form action="" method="post">
        {% csrf_token %}
        <input type="text" name="search" placeholder="Buscar carro..." value="{{ search_query }}">
        <button type="submit">Buscar</button>
    </form>

    <table border="1">
        <thead>
            <tr>
                <th>Nome</th>
                <th>MPG</th>
                <th>Cilindros</th>
                <th>Disposição</th>
                <th>Potência</th>
                <th>Peso</th>
                <th>Aceleração</th>
                <th>Câmbio</th>
                <th>Marchas</th>
            </tr>
        </thead>
        <tbody>
            {% for carro in carros %}
            <tr>
                <td>{{ carro.name }}</td>
                <td>{{ carro.mpg }}</td>
                <td>{{ carro.cyl }}</td>
                <td>{{ carro.disp }}</td>
                <td>{{ carro.hp }}</td>
                <td>{{ carro.wt }}</td>
                <td>{{ carro.qsec }}</td>
                <td>{{ carro.am }}</td>
                <td>{{ carro.gear }}</td>
            </tr>
            {% empty %}
            <tr>
                <td colspan="9">Nenhum carro encontrado.</td>
            </tr>
            {% endfor %}
        </tbody>

</body>
</html>
```

Crie um view para renderizar essa página.
Edite o arquivo `CarsApp.views.py` e inclua a função `searchf`:

```python
from django.shortcuts import render
from CarsApp.models import MTCars

# Create your views here.

def searchf(request):
    if request.method == 'GET':
        return render(request, 'CarsApp/home.html')
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
        return render(request, 'CarsApp/home.html', contexto)
```

Crie o arquivo `CarsApp.urls.py` e inclua uma rota para esse `view`:

```python
from django.contrib import admin
from django.urls import path
from CarsApp import views

app_name = "CarsApp"

urlpatterns = [
    path("", views.searchf, name="home"),
]
```

No arquivo de rotas principais (`MTCars.urls.py`), inclua esse arquivo de rotas que você acabou de criar:

```python
"""
URL configuration for MTCars project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.urls import include # inclua essa linha

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("CarsApp.urls")),  # inclua essa linha
]
```

Teste a sua aplicação:

```bash
python manage.py runserver
```

## Usando a **Interface Administrativa**

Para poder usar a interface administrativa para examinar o banco de dados, registre o como como adminitrável editando o arquivo `CarsApp.admin.py`:

```python
from django.contrib import admin

# Register your models here.

from CarsApp.models import MTCars

admin.site.register(MTCars)
```

## Bônus

Se tudo funcionou até agora, tente dar um pouco mais de estilo à sua página.

Modifique o arquivo `settings.py`:

```python
STATIC_URL = "/static/" # inclua a / antes de static
```

Inclua, no cabeçalho do template, um link para um arquivo de estilo:

```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista de Carros</title>
    <link rel="stylesheet" href="{% static 'CarsApp/css/estilo.css' %}">
</head>
```

No diretório `CarsApp`, crie o diretório `static/CarsApp/css`. Crie o arquivo `estilo.css` e divirta-se com ele. 
A seguir, apenas uma sugestão (que o Copilot nos deu):

```css
input {
    border-radius: 5px;
    padding: 10px;
    border: 1px solid #ccc;
}
button {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}
button:hover {
    background-color: #45a049;
}
table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}
th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}
th {
    background-color: #f2f2f2;
}
```

## Dica Especial

Se você quiser exibir os dados de apenas um carro em uma página diferente do que você já criou, vamos modificar o template para criar um link para um carro em particular.

Transforme o nome do carro em um link. Antes você tinha esse código no arquivo `templates/CarsApp/home.html`:

```html
<td>{{ carro.name }}</td>
```
Modifique para esse código para incluir um link com o `id` do carro:

```html
<td><a href="{% url 'CarsApp:detalhes' carro.id %}">{{ carro.name }}</a></td>
```

Crie uma nova view para exibir os detalhes do carro.
Edite o arquivo `CarsApp/views.py` e inclua a seguinte `view`:

```python
def detalhes(request, carro_id):
    carro = MTCars.objects.get(id=carro_id)
    # Ao criar uma entrada no dicionário contexto com o nome carro (string constante),
    # você vai criar uma variável carro no template associado pela função render.
    # Essa variável é um objeto carro, com todas as suas propriedades.
    contexto = {
        'carro': carro
    }
    return render(request, 'CarsApp/detalhes.html', contexto)
```

Crie o arquivo `CarsApp/templates/CarsApp/detalhes.html` com o seguinte conteúdo:

```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Detalhes do Carro</title>
    <link rel="stylesheet" href="{% static 'CarsApp/css/estilo.css' %}">
</head>
<body>
    <!--
    Aqui vamos usar a variável carro criada no view.
    Essa variável é um objeto carro e tem as propriedades de um carro.
    -->
    <h1>Detalhes do Carro: {{ carro.name }}</h1>
    <ul>
        <li><strong>MPG:</strong> {{ carro.mpg }}</li>
        <li><strong>Cilindros:</strong> {{ carro.cyl }}</li>
        <li><strong>Disposição:</strong> {{ carro.disp }}</li>
        <li><strong>Potência:</strong> {{ carro.hp }}</li>
        <li><strong>Peso:</strong> {{ carro.wt }}</li>
        <li><strong>Aceleração:</strong> {{ carro.qsec }}</li>
        <li><strong>Câmbio:</strong> {{ carro.am }}</li>
        <li><strong>Marchas:</strong> {{ carro.gear }}</li>
    </ul>
    <a href="{% url 'CarsApp:home' %}">Voltar à lista de carros</a>
</body>
</html>
```

Registre a nova rota no arquivo `CarsApp/urls.py`.
Inclua a seguinte entrada na lista `urlpatterns`:

```python
urlpatterns = [
    # já deve ter alguma coisa aqui
    # apenas inclua a rota abaixo
    path("detalhes/<int:carro_id>/", views.detalhes, name="detalhes"),  # nova rota
]
```
