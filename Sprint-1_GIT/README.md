# Tarefa para aprender a usar o Github e o Codespace

> Nível de dificuldade: Difícil (por membro do time)

Nessa tarefa, o time irá aprender o uso básico do Git, Github e CodeSpace.
Iremos criar uma calculadora de quatro operações: `+`, `-`, `*` e `/` para exemplificar os diversos passos.

> Essa tarefa deve ser realizada em equipe de 2, 3, 4 ou 5 alunos.

Este guia explica como **vários alunos podem colaborar** em um mesmo projeto no GitHub — no caso, o repositório fictício chamado `ENG4021`.

> Modifique o nome do repositório de acordo com o seu projeto

Antes de implementar essa tarefa, estude um pouco sobre o uso do Github e do Codespace.

Bibliografia recomendada:
- [Hello World - GitHub Docs](https://docs.github.com/en/get-started/start-your-journey/hello-world)
- [Using Git - GitHub Docs](https://docs.github.com/en/get-started/using-git)

Em caso de dúvidas ou problemas, consulte também [GIT](https://github.com/AlexandreMeslin/ENG4021/tree/main/GIT).

O fluxo descrito a seguir usa **forks** (cópias individuais no GitHub) e **GitHub Codespaces** (ambientes de edição online - IDE).

## CENÁRIO GERAL

| Papel | Usuário | Função |
|-------|----------|--------|
| Dono do projeto | `aluno1` | Repositório principal (`ENG4021`) |
| Colaboradores | `aluno2`, `aluno3`, ... | Criam forks e enviam Pull Requests (`PRs`) |

## Todos os alunos

Criar uma conta *PRO* no **GitHub**.
Se você já tem uma conta, transforme a sua conta em [*PRO*](#transformando-a-sua-conta-em-pro).

### Criando a conta (se você já tem uma conta no GitHub, pode pular essa etapa)

- Acesse o site [github.com](https://github.com/).

- Clique em `Sign up` no canto superior direito.

    ![GitHub Signup](img/github-signup.png)

- Preencha os dados necessários.
Use o seu e-mail da PUC para criar uma conta *PRO*.


### Transformando a sua conta em *PRO*

- Na sua *home-page*, clique na sua foto, no canto superior direito.

- Clique em <svg aria-hidden="true" focusable="false" class="octicon octicon-gear" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path></svg> Settings.

- Expanda <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-credit-card" fill='currentColor'><path d="M10.75 9a.75.75 0 0 0 0 1.5h1.5a.75.75 0 0 0 0-1.5h-1.5Z"></path><path d="M0 3.75C0 2.784.784 2 1.75 2h12.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14H1.75A1.75 1.75 0 0 1 0 12.25ZM14.5 6.5h-13v5.75c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25Zm0-2.75a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25V5h13Z"></path></svg> **Billing and licensing**, no menu lateral esquerdo.

- Clique em `Education benefits`.

- Clique no botão verde `Start an application` e siga as instruções.
Use o documento de inscrição fornecido pelo SAU para comprovar que você é aluno da PUC Rio.




## Aluno 1: Criar repositório

- Criar o repositório do time (de preferência, use o mesmo repositório criado como tarefa da `Sprint 1`).
- Usando o **Codespace**, criar um diretório chamado `Calculadora` na raiz do repositório do time.
Esse diretório será utilizado para criar a calculadora.
- Implementar o módulo `calculadora.py` que irá importar os seguintes módulos que estão sendo desevolvidos pelos alunos 1, 2, 3, 4 e 5:
    - `soma.py`
    - `subtrai.py`
    - `multiplica.py`
    - `divide.py`
- No módulo calculadora, realizar a leitura de dois números reais e um operando. Baseado nos valores lidos exibir o resultado da operação usando as seguintes funções definidas nos modulos importados:
    - `soma.somaf`
    - `subtrai.subtraif`
    - `multiplica.multiplicaf`
    - `divide.dividef`
- Aceitar os PRs dos componentes do time e fazer o *merge*.




## Aluno 2, 3, 4 e 5: Criar *fork*

**Criar um `fork` do repositório original.**

Os alunos 2, 3, 4 e 5 devem pegar com o aluno 1 o endereço do repositório do time.
Cada aluno acessa o projeto principal: https://github.com/aluno1/ENG4021 (não clique nesse link, ele **não** existe - use o link do repositório do seu projeto).

![Home do repositório do projeto](./img/Git-TelaInicial.png)

Clicar no botão
<svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked mr-2"><path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z" fill="currentColor"></path></svg> 
**Fork** no canto superior direito da página.

![Botão de fork](./img/GIT-TelaFork.png)

Na página seguinte, basta clicar no botão verde **Create fork**.

O **GitHub** criará uma cópia pessoal do repositório, por exemplo (aluno2, aluno3, ... não existem, vai aparecer a sua conta no Github):

- `https://github.com/aluno2/ENG4021`
- `https://github.com/aluno3/ENG4021`

![Fork na sua conta](./img/GIT-TelaFork2.png)

Verifique se o endereço que aparece no seu navegador agora é um endereço da sua conta do **GitHub**.

Antes de começar a trabalhar, siga sempre essas [dicas](#dicas-muito-úteis-ou-não-só-vai-depender-de-você).




## Aluno 1, 2, 3, 4 e 5: Abrir o repositório `fork` no Codespace

1. No repositório principal (`aluno1/ENG4021`) ou no fork (`aluno2/ENG4021`), conforme o caso, clique em **Code → Codespaces**
    - Se não existir um Codespace: **Create codespace on main**.
    - Se já existir um Codespace, clicar no nome do Codespace.

    ![Criar codespace](./img/GIT-TelaCriarCodespace.png)

    Se já houver algum Codespace criado, apenas clique no link, **não** crie um novo Codespace.

    ![Abrir Codespace](./img/GIT-TelaAbrirCodespace.png)

1. Aguarde o ambiente ser criado.  

   > O Codespace é como um **VS-Code** rodando no navegador.

   > Nesse momento, você tem uma cópia do *fork* que você fez do repositório original, ou seja, uma cópia da cópia.

- Aluno 2:
    - Criar o modulo `soma.py` dentro do diretório `Calculadora`.
    - Criar a função `somaf` que recebe dois números reais e retorna a sua soma.
- Aluno 3:
    - Criar o modulo `subtrai.py` dentro do diretório `Calculadora`.
    - Criar a função `subtraif` que recebe dois números reais e retorna a sua subtração.
- Aluno 4:
    - Criar o modulo `multiplica.py` dentro do diretório `Calculadora`.
    - Criar a função `multiplicaf` que recebe dois números reais e retorna a sua multiplicação.
- Aluno 5:
    - Criar o modulo `divide.py` dentro do diretório `Calculadora`.
    - Criar a função `dividef` que recebe dois números reais e retorna a sua divisão.

Implementar testes no módulo. Você pode usar o segmento de código a seguir para realizar o teste. Esse código exemplifica como realizar o teste para a função `somaf`. 
Modifique-o para a sua função.

```python
def somaf(n1: float, n2: float) -> float:
    '''
    Função que retorna a soma de dois números (inteiros ou reais).

    :param n1: número 1 (int ou float)
    :param n2: número 2 (int ou float)
    :return: soma de n1 e n2 (int ou float)
    
    Exemplo:
    >>> somaf(2, 3)
    5
    >>> somaf(2.5, 3.7)
    6.2
    '''
    return n1 + n2

def main():
    '''
    Função principal para testar a função somaf.
    1. Testa a soma de dois números inteiros.
    2. Testa a soma de dois números reais.
    3. Testa a soma de um número negativo e um positivo.
    4. Testa a soma de zero com um número positivo.
    5. Testa a soma de um número positivo com zero.
    6. Testa a soma de dois números reais iguais.
    7. Imprime uma mensagem de sucesso se todos os testes passarem.
    8. Retorna None.

    :return: None
    
    Exemplo:
    >>> main()
    Todos os testes passaram com sucesso!
    None
    '''
    assert somaf(2, 3) == 5, "Erro: 2 + 3 deveria ser 5"
    assert somaf(2.5, 3.7) == 6.2, "Erro: 2.5 + 3.7 deveria ser 6.2"
    assert somaf(-1.5, 4.5) == 3.0, "Erro: -1.5 + 4.5 deveria ser 3.0"
    assert somaf(0, 5) == 5, "Erro: 0 + 5 deveria ser 5"
    assert somaf(5, 0) == 5, "Erro: 5 + 0 deveria ser 5"
    assert somaf(1.1, 1.1) == 2.2, "Erro: 1.1 + 1.1 deveria ser 2.2"
    print("Todos os testes passaram com sucesso!")
    return
    
if __name__ == "__main__":
    '''
    Executa a função main se o script for executado diretamente.
    1. Chama a função main.
    2. Retorna None.
    '''
    main()
```

## Fazer commit e push no fork

> Aqui você vai atualizar o seu repositório clonado, aquele que você fez o *fork*. Você **não** vai atualizar o repositório do seu projeto. Isso vai ser feito mais abaixo.

Na barra de ícones localizada no lado esquerdo, note que o ícone 
<svg aria-hidden="true" focusable="false" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg>
**Source Control** (provalvemente) deve estar sendo exibido com um número dentro de um círculo azul.

![Source Control](img/github-source-control-30.png)

Clique no ícone do <svg aria-hidden="true" focusable="false" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg> **Source Control** ou digite `Ctrl+Shift+G`.

> Antes de fazer qualquer `Commit`, verifique sempre se você está com a versão atual do repositório clicando nos ícones com as setas para baixo, da esquerda para a direita. Veja a figura a seguir:

![Codespace fetch pull push](img/codespace-fetch-pull-push.png)

Se tudo correr bem, escreva um texto na caixa acima do botão verde descrevendo em poucas palavras as modificações que você implementou recentemente (nesse *commit*).
Clique em `Commit` e depois em `Sync Changes`.

Agora o seu repositório está atualizado e o seu trabalho definitivamente salvo.
Antes disso, ele apenas exitia no *container* criado para o seu Codespace.
Ou seja, se o seu Codespace fosse apagado ou destruído, o seu trabalho iria junto!




## Criar um Pull Request (PR)

No GitHub (aluno2/ENG4021):

1. Clique no botão <svg aria-hidden="true" focusable="false" class="octicon octicon-git-pull-request" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path></svg> Contribute e depois no botão verde `Open pull request`.

    ![Abrir um PR](./img/GIT-TelaCriarPR.png)

1. Verifique:

    ```
    base repository: aluno1/ENG4021     ← destino (repositório principal)
    head repository: aluno2/ENG4021     ← origem (seu fork)
    ```

1. Adicione um título e uma descrição das mudanças.

    ![Abrir um PR](./img/GIT-TelaCriarPR2.png)

1. Clique em `Create pull request`.

    ![Abrir um PR](./img/GIT-TelaCriarPR3.png)




## Revisão pelo dono do repositório

O aluno1 verá o PR em:

```bash
https://github.com/aluno1/ENG4021/pulls
```

O **PR** também pode ser visto pela interface Web observando o link <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline" fill='currentColor'><path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path></svg> **Pull requests**. No seu lado direito, você verá a quantidade de PRs pendentes.

![Aceitar PR](./img/GIT-TelaAceitarPR.png)

Ele pode:

- Analisar o código modificado.
- Comentar ou solicitar alterações.
- Fazer o merge quando estiver tudo certo.

Quando o merge é feito, as mudanças entram no repositório principal.

1. Clique no link <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline" fill='currentColor'><path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path></svg> **Pull requests**.

    ![Aceitar PR](./img/GIT-TelaAceitarPR2.png)

1. Clique no **PR** que você deseja realizar o *merge*:

    ![Aceitar PR](./img/GIT-TelaAceitarPR3.png)

1. Se não houver problemas, clique em `Merge pull request` e depois em `Confirm merge` para confirmar o *merge* .

    ![Aceitar PR](./img/GIT-TelaAceitarPR4.png)




## Atualizar o fork com o repositório principal

Quando aluno1 aceita um PR ou alterar algo diretamente, os outros *forks* ficam desatualizados.
Cada aluno deve sincronizar o *fork* com o original antes de novas modificações.
Para isso, basta clicar no botão <svg aria-hidden="true" focusable="false" class="octicon octicon-sync" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.705 8.005a.75.75 0 0 1 .834.656 5.5 5.5 0 0 0 9.592 2.97l-1.204-1.204a.25.25 0 0 1 .177-.427h3.646a.25.25 0 0 1 .25.25v3.646a.25.25 0 0 1-.427.177l-1.38-1.38A7.002 7.002 0 0 1 1.05 8.84a.75.75 0 0 1 .656-.834ZM8 2.5a5.487 5.487 0 0 0-4.131 1.869l1.204 1.204A.25.25 0 0 1 4.896 6H1.25A.25.25 0 0 1 1 5.75V2.104a.25.25 0 0 1 .427-.177l1.38 1.38A7.002 7.002 0 0 1 14.95 7.16a.75.75 0 0 1-1.49.178A5.5 5.5 0 0 0 8 2.5Z"></path></svg> **Sync fork** e depois no botão verde `Update branch`.

![Sync fork - Update branch](img/GIT-TelaSyncFork2.png)

> Na próxima vez que você for usar o Codespace, lembre-se de clicar nos botões com a seta para baixo, da esquerda para a direita, do <svg aria-hidden="true" focusable="false" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg> **Source Control**.




## Todos os alunos

- Testar o funcionamento da calculadora usando o Codespace
- Criar um card no Kanban. No card:
    - Incluir um *print* da calculadora funcionando.
    - Incluir um *print* do diretório `Calculadora` como evidência de que a tarefa foi concluída.





# Dicas (muito úteis ou não, só vai depender de você)

- [Relação do seu *branch* com o original](#relação-do-seu-branch-com-o-original)




## Relação do seu *branch* com o original

> O texto a seguir considera que você já sincronizou o seu Codespace com o seu repositório.

O seu *branch* pode estar em um desses quatro estados com relação ao repostório original.
Verifique sempre a mensagem no topo da página.

1. `up to date`: nada a fazer, pode começar a trabalhar!
        ![up to date](img/github-up-to-date.png)

1. `ahead`: nesse caso, você pode continuar a trabalhar, ou, se você já terminou a sua parte, você pode fazer um `pull request` (popularmente conhecido como `PR`).
    ![branch ahead](img/github-ahead.png)

1. <a id="behind"></a>`behind`: se for esse o seu caso, basta clicar em 
    <svg aria-hidden="true" focusable="false" class="octicon octicon-sync" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.705 8.005a.75.75 0 0 1 .834.656 5.5 5.5 0 0 0 9.592 2.97l-1.204-1.204a.25.25 0 0 1 .177-.427h3.646a.25.25 0 0 1 .25.25v3.646a.25.25 0 0 1-.427.177l-1.38-1.38A7.002 7.002 0 0 1 1.05 8.84a.75.75 0 0 1 .656-.834ZM8 2.5a5.487 5.487 0 0 0-4.131 1.869l1.204 1.204A.25.25 0 0 1 4.896 6H1.25A.25.25 0 0 1 1 5.75V2.104a.25.25 0 0 1 .427-.177l1.38 1.38A7.002 7.002 0 0 1 14.95 7.16a.75.75 0 0 1-1.49.178A5.5 5.5 0 0 0 8 2.5Z"></path></svg> Sync fork <svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg>, depois no botão verde `Update branch`.
        ![branch behind](img/github-behind.png)

1. `ahead and behind`: isso significa que você fez algumas modificações no seu branch e que aconteceram modificações no repositório original.

    ![branch ahead & behind](img/git-ahead-behind.png)

    Para resolver a situação, comece atualizando o seu branch, clicando no botão
    <svg aria-hidden="true" focusable="false" class="octicon octicon-sync" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.705 8.005a.75.75 0 0 1 .834.656 5.5 5.5 0 0 0 9.592 2.97l-1.204-1.204a.25.25 0 0 1 .177-.427h3.646a.25.25 0 0 1 .25.25v3.646a.25.25 0 0 1-.427.177l-1.38-1.38A7.002 7.002 0 0 1 1.05 8.84a.75.75 0 0 1 .656-.834ZM8 2.5a5.487 5.487 0 0 0-4.131 1.869l1.204 1.204A.25.25 0 0 1 4.896 6H1.25A.25.25 0 0 1 1 5.75V2.104a.25.25 0 0 1 .427-.177l1.38 1.38A7.002 7.002 0 0 1 14.95 7.16a.75.75 0 0 1-1.49.178A5.5 5.5 0 0 0 8 2.5Z"></path></svg> **Sync fork**, e depois no botão verde, `Update branch`.
    Agora você está no estado `behind` listado [aqui](#behind).
