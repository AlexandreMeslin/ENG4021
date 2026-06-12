# Autenticando e autorizando um usuário

### Atividade Individual 4

Nessa atividade, você vai implemnetar autenticação e autorização de usuários, implementando:

- Sistema de login de usuário
- Proteção de páginas
- Sistema para trocar senha de usuário
- Sistema para recuperação de senha de usuário

## Passos iniciais

Para você desenvolver essa atividade, você deve completar a [atividade individual 2](../AI2-MeuProjeto/).

> Você vai desenvolver essa atividade no seu repositório privado. **NÃO** use o repositório do time!

- Vá para o diretório do seu projeto:

```bash
cd MeuProjeto
```

Se você estiver no lugar correto, você verá uma saída semelhante à seguinte ao usar o comando `ls -l` no terminal:

```bash
$ ls -l
total 20
drwxrwxrwx+ 5 codespace codespace 4096 May 30 14:33 MeuSite
-rw-r--r--  1 codespace codespace    0 May 30 14:26 db.sqlite3
-rwxr-xr-x  1 codespace codespace  663 May 30 14:22 manage.py
-rw-rw-rw-  1 codespace codespace    6 May 30 14:17 requirements.txt
drwxrwxrwx+ 5 codespace codespace 4096 May 30 14:18 venv
    ```

- Crie um ambiente virtual, se ele não existir.

> [!TIP]
> Você pode saber se o ambiente virtual já foi criado verificando se o diretório `venv` está presente.

```bash
python -m venv venv
```

1. Ative o ambiente virtual:

> [!TIP]
> Você pode saber se o ambiente virtual já está ativado verificando se o *prompt* inicia por `(venv)`.

```bash
source venv/bin/activate
```

> [!IMPORTANT]
> Tenha certeza que o ambiente virtual está ativo conferindo o texto `(venv)` no início do *prompt*.

- Entre no diretório do seu site com o comando a seguir:

```bash
cd MeuSite
```

- Provavelmente você já migrou o seu banco de dados, mas se não tiver migrado ainda, essa é uma boa hora:

```bash
python manage.py migrate
```

- Aproveite para criar um usuário, caso ainda não tenha criado.
Se você está em dúvida, crie um novo usuário e está resolvido.

```bash
python manage.py createsuperuser
```

- Uma boa ideia seria você testar para ver se o seu site está no funcionando. Coloque o site no ar e use o seu navegador para testar:

```bash
python manage.py runserver 0.0.0.0:8000
```

## Criando o login

### Rotas

No arquivo `MeuProjeto/MeuSite/urls.py`, inclua a seguinte rota na lista de rotas:

```python
from django.urls.conf import include

urlpatterns = [
    # aqui pode haver mais linhas
    # inclua a linha abaixo no final da lista
    path('accounts/', include('django.contrib.auth.urls')),  # Include authentication URLs
]
```

> [!IMPORTANT]
> Não se esqueça de importar o módulo `include` no seu módulo `urls.py` como mostrado logo acima.

Ao incluir essa path, o Django vai criar para você as seguintes URLs. Entre colchetes você encontra o nome do endpoint para usar como link:

```
accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']
```

### Configuração

- Edite o arquivo `MeuProjeto/MeuSite/settings.py` e inclua as seguintes linhas para criar as variáveis de configuração do *login* :

```python
LOGOUT_REDIRECT_URL = '/accounts/login/'  # Para onde vai após logout
LOGIN_URL = '/accounts/login/'       # URL de login (padrão)
# ATENÇÃO!!! Troque o valor da variável abaixo para que ela seja uma das rotas
# válidas no seu arquivo MeuSite/curriculo/urls.py
LOGIN_REDIRECT_URL = '/spiff/'   # Para onde vai após login
```

Para evitar problemas de *CSRF* (*Cross-Site Request Forgery* - Falsificação de Solicitação entre Sites) e *CORS* (*Cross-Origin Resource Sharing* - Compartilhamento de recursos de origens diferentes), inclua as seguintes linhas no seu arquivo `settings.py`

```python
CORS_ALLOW_ALL_ORIGINS = True
CSRF_TRUSTED_ORIGINS = [
    'https://localhost:8000', 
    'http://localhost:8000',
]
```

### Página de login

Em `MeuProjeto/MeuSite/templates/`, crie o diretório `registration`. 
Dentro desse diretório, crie o arquivo `login.html`.

> [!NOTE]
> Certifique-se que dentro de `templates`, você visualiza os dois diretórios no mesmo nível: `curriculo` e `registration`.

Use esse modelo como conteúdo da sua página de *login*.
Modifique o modelo para ajustar às suas preferências.

```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4Q6Gf2aSP4eDXB8Miphtr37CMZZQ5oXLH2yaXMJ2w8e2ZtHTl7GptT4jmndRuHDT" crossorigin="anonymous">
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

Na sua *home-page*, inclua uma rota para o *login* editando o arquivo `MeuProjeto/MeuSite/templates/home.html`.
A rota pode ser parecida com essa:

```html
<a href="{% url 'login' %}">Login</a>
```

O exemplo a seguir inclui um *link* para o *login* e outro para o *logout* na *home-page*:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home Page</title>
</head>
<body>
    <h1>Home Page do MeuSite</h1>

    <h2>Links para os currículos</h2>
    <ul>
        <li><a href="{% url 'curriculo_spiff' %}">Currículo do Spiff</a></li>
        <li><a href="{% url 'curriculo_spiff_v2' %}">Currículo responsivo do Spiff</a></li>
    </ul>

    <h2>Área de controle de acesso</h2>
    <ul>
        <li><a href="{% url 'login' %}">Login</a></li>
        <li><form method='POST' action="{% url 'logout' %}">{% csrf_token %}<button type='submit'>Logout</button></form></li>
    </ul>
</body>
</html>
```

Teste a sua página de *login*!

### Proteção da página

> [!CAUTION]
> NÃO CONTINUE SE VOCÊ NÃO TIVER TESTADO COMPLETAMENTE A SUA PÁGINA DE LOGIN E LOGOUT.

Se você implementou totalmente A AI2, a sua aplicação deve ter, no mínimo, dois views. Vamos proteger um deles.

Edite o arquivo `MeuProjeto/MeuSite/views.py`.
Importe o seguinte decorador:

```python
from django.contrib.auth.decorators import login_required
```

Anote todos (pelo menos um) os `views` que você gostaria de proteger com:

```python
@login_required
```

O seu `view` deve estar parecido com esse (veja o *import* e a anotação na função): 

```python
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

def home(request):
    '''
    View function for home page of site.
    Renders the home.html template.
    '''
    return render(request, 'home.html')

@login_required
def curriculo_spiff(request):
    '''
    View function for the astronaut Spiff's resume page.
    Renders the curriculo-v1.html template.
    This will display the resume page when the corresponding URL is accessed
    The curriculo_spiff view is responsible for displaying the content of the resume page
    It is a simple function-based view
    It takes a request object as a parameter
    It returns a rendered HTML response
    @param request: The HTTP request object
    @return: Rendered HTML response with resume page content
    '''
    return render(request, 'curriculo-v1.html')

@login_required
def curriculo_spiff_v2(request):
    '''
    View function for the astronaut Spiff's resume page version 2.
    A responsive version of the resume page.
    Renders the curriculo-v2.html template.
    This will display the resume page version 2 when the corresponding URL is accessed
    The curriculo_spiff_v2 view is responsible for displaying the content of the resume page version 2
    It is a simple function-based view
    It takes a request object as a parameter
    It returns a rendered HTML response
    @param request: The HTTP request object
    @return: Rendered HTML response with resume page version 2 content
    '''
    return render(request, 'curriculo-v2.html')
```

### Testando tudo

1. Acesse a sua *home-page*.

1. Faça login.

1. Visite ambas as páginas: a liberada e a protegida (copie o endereço das páginas - principalmente a protegida).

1. Volte para a sua *home-page*.

1. Faça *logout*.

1. Tente visitar as páginas, principalmente a protegida. Você será encaminhado para a página de *login*, mas conseguirá visitar a página liberada.

### Trocar senha

Crie um *link* na sua *home-page* para permitir que o usuário troque a senha. 
No *link*, lembre ao usuário que ele deve estar *logado* para poder trocar sua senha.

```python
<a href="{% url 'password_change' %}">Trocar senha (somente para usuários logados)</a>
```

> [!CAUTION]
> O *link* não deveria estar na *home-page*, mas não temos muitas páginas nessa atividade, então...

Teste a troca da senha.

> Observe que você está usando um *template* criado pelo **Django** para realizar a troca da senha. Se você quiser, veja como usar o seu *template*.
