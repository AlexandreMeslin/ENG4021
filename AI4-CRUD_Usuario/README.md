# Autenticando e autorizando um usuário

### Atividade Individual 4

Nessa atividade, você vai implementar autenticação e autorização de usuários, implementando:

- Sistema de login de usuário
- Proteção de páginas
- Sistema para trocar senha de usuário
- Sistema para recuperação de senha de usuário

## Passos iniciais

Para você desenvolver essa atividade, você deve completar a [atividade individual 2](../AI2-MeuProjeto/).

> Você vai desenvolver essa atividade no seu repositório privado. 
> **NÃO** use o repositório do time!

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

Se você ainda não instalou os requisitos, criou requisitos novos ou não se lembra se instalou ou não, instale agora os requisitos:

```bash
pip install -r requirements.txt
```

- Provavelmente você já migrou o seu banco de dados, mas se não tiver migrado ainda, essa é uma boa hora:

```bash
python manage.py migrate
```

O Django fornece um objeto `User` (`models.User`) com os seguintes campos, propriedades ou atributos:

| Propriedades | Descrição |
|---|---|
| username | nome do usuário |
| first_name | primeiro nome |
| last_name | último nome |
| email | e-mail
| password | senha |
| groups | grupos aos quais o usuário pertence |
| user_permissions | permissões do usuário |
| is_staff | se é parte do staff |
| is_active | se está ativo |
| is_superuser | se é super usuário |
| last_login | data do último login |
| date_joined | data de entrada |
| is_authenticated | se está autenticado |
| is_anonymous | se está como anonymous |

Além das propriedades listadas acima, os seguintes métodos também fazem parte da classe `User`. 
Os parâmetros, quando existirem, são informados dentro dos parêntesis. 
Parâmetros opcionais com o valor default são exibidos no formato `parâmetro=valor_default`.

| Método | Descrição |
|---|---|
| get_full_name() | retorna o nome completo do usuário |
| get_short_name() | retorna o primeiro nome |
| set_password(raw_password) | configura a senha |
| check_password(raw_password) | verifica se a senha está correta |
| set_unusable_password() | cria uma senha que não pode ser digitada |
| has_usable_password() | verifica se a senha não pode ser digitada |
| get_group_permissions(obj=None) | retorna as permissões que o usuário herdou do seu grupo |
| get_all_permissions(obj=None) | retorna todas as permissões do usuário |
| has_perm(perm, obj=None) | verifica se o usuário tem determinada permissão |
| has_perms(perm_list, obj=None) | verifica se o usuário tem determinadas permissões |
| has_module_perms(package_name) | verifica se o usuário tem permissão de acessar determinado módulo |
| email_user(subject, message, from_email=None, **kwargs) | envia um e-mail para o usuário |


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
<a href="{% url 'login' %}">
    Login
</a>
```

Para fazer *logout*, devemos enviar o pedido via método *POST*, o que requer o uso de um formulário (ou de um *script* em JavaScript).
Veja como podemos criar um botão simples para criar o *login*:

```html
<form method='POST' action="{% url 'logout' %}">
    {% csrf_token %}
    <button type='submit'>Logout</button>
</form>
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

> [!TIP]
> Se você quiser que o seu botão de *logout* se pareça com um *link*, inclua o *link* para o Bootstrap na seção `<head>` da sua página e coloque o botão *submit*  nas classes `btn` e `btn-link`.

*Link* para o Bootstrap:

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
```

Exemplo de *logout* com formato de *link*:

```html
<div style="display: inline-block;">
    <form method='POST' action="{% url 'logout' %}">
        {% csrf_token %}
        <button type='submit' class="btn btn-link">Logout</button>
    </form>
</div>
```

Teste a sua página de *login*!

### Proteção da página

> [!CAUTION]
> NÃO CONTINUE SE VOCÊ NÃO TIVER TESTADO COMPLETAMENTE A SUA PÁGINA DE LOGIN E LOGOUT.

Se você implementou totalmente A AI2, a sua aplicação deve ter, no mínimo, dois views.
Vamos proteger um deles.

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

1. Faça *login*.

1. Visite ambas as páginas: a liberada e a protegida (copie o endereço das páginas - principalmente a protegida).

1. Volte para a sua *home-page*.

1. Faça *logout*.

1. Tente visitar as páginas, principalmente a protegida. Você será encaminhado para a página de *login*, mas conseguirá visitar a página liberada.

### Trocar senha

Crie um *link* na sua *home-page* para permitir que o usuário troque a senha. 
No *link*, lembre ao usuário que ele deve estar *logado* para poder trocar sua senha.

```html
<a href="{% url 'password_change' %}">Trocar senha (somente para usuários logados)</a>
```

> [!CAUTION]
> O *link* não deveria estar na *home-page*, mas não temos muitas páginas nessa atividade, então...

Teste a troca da senha.

> Observe que você está usando um *template* criado pelo **Django** para realizar a troca da senha. 
> Se você quiser, veja como usar o seu *template*.

### Trocar senha com páginas personalizadas

No diretório `templates/registration` crie os seguintes arquivos (preserve os nomes exatamente!):

- Arquivo `password_change_form.html`:

```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Trocar senha</title>
</head>
<body>
    <h1>Trocar senha</h1>

    <form method="post">
        {% csrf_token %}

        {{ form.as_p }}

        <button type="submit">Alterar senha</button>
    </form>

    <p>
        <a href="/">Voltar à página inicial</a>
    </p>
</body>
</html>
```

- Arquivo `password_change_done.html`:

```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Senha alterada</title>
</head>
<body>
    <h1>Senha alterada com sucesso!</h1>

    <p>Sua senha foi atualizada.</p>

    <p>
        <a href="/">Voltar à página inicial</a>
    </p>
</body>
</html>
```

No arquivo `settings.py`, configure o diretório de *templates*.
Modifique **APENAS** a chave `DIRS` do dicionário `TEMPLATES`:

```python

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'MeuSite' / 'templates'],   # <== modifique apenas esta linha!!!
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

Inclua o link para troca de senha na página desejada (no nosso caso, na home-page).
Edite o arquivo `templates/home.html` e inclua o seguinte link:

```html
<a href="{% url 'password_change' %}">Trocar senha (somente para usuários logados)</a>
```
