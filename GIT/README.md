# Índice

- [Links úteis](#links-%C3%BAteis)
- [Uso do Github](#uso-do-github)
- [Problemas conhecidos e suas "soluções"](#problemas-conhecidos-e-suas-solu%C3%A7%C3%B5es)
- [Comandos utilizados](#comandos-utilizados)

---

# Links úteis

- https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
- https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers

---

# Uso do Github

Este guia explica como **vários alunos podem colaborar** em um mesmo projeto no GitHub — no caso, o repositório fictício chamado `ENG4021`.

> [!IMPORTANT]\
> Modifique o nome do repositório de acordo com o seu projeto

O fluxo descrito abaixo usa **forks** (cópias individuais no GitHub) e **GitHub Codespaces** (ambientes de edição online - IDE).

## CENÁRIO GERAL

| Papel | Usuário | Função |
|-------|----------|--------|
| Dono do projeto | `aluno1` | Repositório principal (`ENG4021`) |
| Colaboradores | `aluno2`, `aluno3`, ... | Criam forks e enviam Pull Requests (`PRs`) |

## Fazer o *fork* do repositório

Cada aluno acessa o projeto principal: https://github.com/aluno1/ENG4021 (não clique nesse link, ele **não** existe - use o link do repositório do seu projeto).

![Home do repositório do projeto](./img/Git-TelaInicial.png)

E clica em **Fork** (no canto superior direito da tela).

![Botão de fork](./img/GIT-TelaFork.png)

Depois clique em **Create fork**.

O GitHub criará uma cópia pessoal do repositório, por exemplo (aluno2, aluno3, ... não existem, vai aparecer a sua conta no Github):

- `https://github.com/aluno2/ENG4021`
- `https://github.com/aluno3/ENG4021`

![Fork na sua conta](./img/GIT-TelaFork2.png)

## Abrir o repositório fork no Codespace

1. No fork (`aluno2/ENG4021`), clique em **Code → Codespaces → Create codespace on main**.

    ![Criar codespace](./img/GIT-TelaCriarCodespace.png)

    Se já houver algum Codespace criado, apenas clique no link, **não** crie um novo Codespace.

    ![Abrir Codespace](./img/GIT-TelaAbrirCodespace.png)

1. Aguarde o ambiente ser criado.  

   > O Codespace é como um **VS-Code** rodando no navegador.

   > Nesse momento, você tem uma cópia do *fork* que você fez do repositório original, ou seja, uma cópia da cópia.


## Fazer modificações

Edite normalmente os arquivos no Codespace. 
Por exemplo, altere `src/main.c` e `README.md`.

Para verificar mudanças:

```bash
git status
```

Saída esperada:

```text
modified: src/main.c
modified: README.md
```

Ou se você tiver criado (não apenas modificado) algum arquivo, a saída esperada pode ser outra:

```text
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        GIT/

no changes added to commit (use "git add" and/or "git commit -a")
```

## Fazer commit e push no fork

> Aqui você vai atualizar o seu repositório clonado, aquele que você fez o *fork*. Você **não** vai atualizar o repositório do seu projeto. Isso vai ser feito mais abaixo.

Após editar, no terminal, digite:

```bash
git add .
git commit -m "Atualiza função principal e README"
git push origin main
```

Agora suas alterações estão no seu fork (aluno2/ENG4021).


## Criar um Pull Request (PR)

No GitHub (aluno2/ENG4021):

1. Clique em `Contribute` → `Open pull request`.

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

O **PR** também pode ser visto pela interface Web observando o link `Pull request`. No seu lado direito, você verá a quantidade de PRs pendentes.

![Aceitar PR](./img/GIT-TelaAceitarPR.png)

Ele pode:

- Analisar o código modificado.
- Comentar ou solicitar alterações.
- Fazer o merge quando estiver tudo certo.

Quando o merge é feito, as mudanças entram no repositório principal.

1. Clique no link `Pull requests`

    ![Aceitar PR](./img/GIT-TelaAceitarPR2.png)

1. Clique no PR que você deseja realizar o merge:

    ![Aceitar PR](./img/GIT-TelaAceitarPR3.png)

1. Se não houver problemas, clique em `Merge pull request` e depois em `Confirm merge` para confirmar o *merge* .

    ![Aceitar PR](./img/GIT-TelaAceitarPR4.png)

## Atualizar o fork com o repositório principal

Quando aluno1 aceita um PR ou alterar algo diretamente, os outros forks ficam desatualizados.
Cada aluno deve sincronizar o fork com o original antes de novas modificações:

```bash
# Adicionar o repositório principal (de aluno1)
git remote add upstream https://github.com/aluno1/ENG4021.git

# Buscar as atualizações
git fetch upstream

# Mesclar com sua branch principal
git checkout main
git merge upstream/main

# Atualizar o fork remoto
git push origin main
```

## Comandos essenciais
```bash
# Ver status dos arquivos
git status

# Adicionar todos os arquivos modificados
git add .

# Fazer commit com mensagem
git commit -m "Descrição da modificação"

# Enviar commit para o fork
git push origin main

# Atualizar fork com repositório original
git remote add upstream https://github.com/aluno1/ENG4021.git
git fetch upstream
git merge upstream/main
git push origin main
```

## Dicas úteis

- Faça commits pequenos e frequentes, com mensagens claras.
- Antes de editar, sempre atualize seu fork com git fetch upstream.
- No PR, descreva bem as alterações e a motivação.
- O `aluno1` pode usar a aba Pull Requests para revisar e comentar.

---

# Problemas conhecidos e suas "soluções"

- [Usuário não conhecido no repositório local](#usuário-não-conhecido-no-repositório-local)
- [Desistir de um commit porque não consegue fazer push](#desistir-de-um-commit-porque-n%C3%A3o-consegue-fazer-push)
- [Origem e local divergem](#origem-e-local-divergem)
- [O mesmo arquivo editado na origem e no clone](#o-mesmo-arquivo-editado-na-origem-e-no-clone)
- [Alterações locais não commitadas](#altera%C3%A7%C3%B5es-locais-n%C3%A3o-commitadas)
- [O push vai tornar público um e-mail privado](#o-push-vai-tornar-p%C3%BAblico-um-e-mail-privado)
- [O branch do PR tem conflitos com o conteúdo do repositório origem](#o-branch-do-pr-tem-conflitos-com-o-conte%C3%BAdo-do-reposit%C3%B3rio-origem)

## Usuário não conhecido no repositório local

### Descrição

O Git não consegue encontrar as credenciais locais para fazer login no repositório remoto ou as credenciais que ele encontrou estão erradas ou desatualizadas.

### Sintoma

```
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.
```

### Solução 1

Faça login de forma global.
Vai afetar todos os seus repositórios locais.
> (as aspas fazem parte do comando)

```bash
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

### Solução 2

Faça login apenas no repositório corrente.
> (as aspas fazem parte do comando)

```bash
git config user.name "Seu Nome"
git config user.email "seu_email@dominio.com"
```

---

## Desistir de um commit porque não consegue fazer push

### Descrição

Você criou um *commit*, não fez, não quer fazer ou não consegue fazer um *push* e deseja desfazer o *commit* por algum motivo.

### Sintoma

```
error: Pulling is not possible because you have unmerged files.
hint: Fix them up in the work tree, and then use 'git add/rm <files>
hint: as appropriate to mark resolution and make a commit.
fatal: Exiting because of an unresolved conflict.
```

### Solução

**Tentativa 1**: Desfazer o commit, mas manter as alterações no diretório de trabalho:

```bash
git reset --soft HEAD~1
```
> Not que HEAD~1 usa o sinal de til e não um traço!

Se não funcionar...

**Tentativa 2**: Desfazer o commit e deixar as mudanças como “unstaged”:

```bash
git reset --mixed HEAD~1
```

Tente sincronizar agora com a origem (se quiser, pode usar agora a interface gráfica).

(Matheus, obrigado!)

---

## Origem e local divergem

### Descrição

Os repositórios remoto e local divergem em um ou mais arquivos.
Ou seja, alguns arquivos no repositório remoto estão mais atualizados do que no repositório local e vice-versa.

### Sintoma

```ascii
From https://github.com/AlexandreMeslin/ENG4021
 * branch            main       -> FETCH_HEAD
hint: You have divergent branches and need to specify how to reconcile them.
hint: You can do so by running one of the following commands sometime before
hint: your next pull:
hint:
hint:   git config pull.rebase false  # merge
hint:   git config pull.rebase true   # rebase
hint:   git config pull.ff only       # fast-forward only
hint:
hint: You can replace "git config" with "git config --global" to set a default
hint: preference for all repositories. You can also pass --rebase, --no-rebase,
hint: or --ff-only on the command line to override the configured default per
hint: invocation.
fatal: Need to specify how to reconcile divergent branches.
```

### Solução (mais conservadora)

```bash
git pull --tags origin main --no-rebase
```

Resultado esperado:

```ascii
From https://github.com/AlexandreMeslin/ENG4021
 * branch            main       -> FETCH_HEAD
Merge made by the 'ort' strategy.
 GIT/img/GIT-TelaSyncFork.png | Bin 0 -> 154035 bytes
 README.md                    |   4 ++--
 2 files changed, 2 insertions(+), 2 deletions(-)
 create mode 100644 GIT/img/GIT-TelaSyncFork.png
```

---

## O mesmo arquivo editado na origem e no clone

## Descrição

O mesmo arquivo foi modificado em dois locais diferentes.

### Sintoma

Ao tentar fazer o `push`, o Github informa o conflito:

```txt
This branch has conflicts that must be resolved

Discard 1 commit to make this branch match the upstream repository. 1 commit will be removed from this branch.

You can resolve merge conflicts using the command line and a text editor.
```

![Branch out-of-date](./img/GIT-ConflitoDetectado.png)

### Solução

Vá para o terminal do Codespace.

1. Verifique se você está na branch `main`:

    ```bash
    git status
    ```

    Resultado esperado

    ```
    On branch main
    Your branch is up to date with 'origin/main'.

    nothing to commit, working tree clean
    ```

1. Verifique se o repositório original está como `upstream`:

    ```bash
    git remote -v
    ```

    Resultado esperado:

    ```ascii
    origin  https://github.com/alexandre-att/ENG4021 (fetch)
    origin  https://github.com/alexandre-att/ENG4021 (push)
    upstream        https://github.com/AlexandreMeslin/ENG4021.git (fetch)
    upstream        https://github.com/AlexandreMeslin/ENG4021.git (push)
    ```

1. Atualize o seu repositório clonado:

    ```bash
    git fetch upstream
    ```

    Resultado esperado:

    ```
    remote: Enumerating objects: 7, done.
    remote: Counting objects: 100% (7/7), done.
    remote: Compressing objects: 100% (3/3), done.
    remote: Total 4 (delta 1), reused 4 (delta 1), pack-reused 0 (from 0)
    Unpacking objects: 100% (4/4), 466 bytes | 466.00 KiB/s, done.
    From https://github.com/AlexandreMeslin/ENG4021
       9243ba8..b7f24d6  main       -> upstream/main
    ```

1. Faça o merge do conteúdo atualizado na sua branch

    ```bash
    git merge upstream/main
    ```

    Resultado esperado:

    ```
    Auto-merging GIT/arq1.txt
    CONFLICT (content): Merge conflict in GIT/arq1.txt
    Automatic merge failed; fix conflicts and then commit the result.
    ```

1. Se vira para resolver os conflitos

    Edite o(s) arquivo(s) com conflitos.
    O resultado da edição será o conteúdo final do arquivo no seu projeto original.

    O Git adiciona esses marcadores especiais:
    
    | Marcador | Significado |
    |---|---|
    | <<<<<<< HEAD | Seu conteúdo local (no fork, ou branch atual) |
    | ======= | Separador entre as duas versões |
    | >>>>>>> upstream/main | Conteúdo vindo do repositório original |

    Remova as linhas com `<<<<<<<`, `=======`, e `>>>>>>>`.

    ![Editor de conflitos](./img/GIT-EditorDeConflito.png)

1. Depois de corrigir todos os conflitos de todos os arquivos, no terminal do Codespace:

    ```bash
    git add .
    git commit
    git push origin main
    ```

1. Faça novamente o procedimento para realizar o PR na interface Web do Github.

---

## O push vai tornar público um e-mail privado

### Descrição

Você configurou o dispositivo de segurança para não revelar o seu e-mail.
Mas ao realizar um PR, um e-mail deve ser informado.
Opcionalmente você pode usar um *alias* de e-mail criado pelo GitHub para esconder o seu e-mail.

### Sintoma:

```
> git push -u origin codespace-fantastic-space-zebra-vp7p7jpxw69hp9v4
remote: error: GH007: Your push would publish a private email address.        
remote: You can make your email public or disable this protection by visiting:        
remote: https://github.com/settings/emails        
To https://github.com/AlexandreMeslin/ENG4021
 ! [remote rejected] codespace-fantastic-space-zebra-vp7p7jpxw69hp9v4 -> codespace-fantastic-space-zebra-vp7p7jpxw69hp9v4 (push declined due to email privacy restrictions)
error: failed to push some refs to 'https://github.com/AlexandreMeslin/ENG4021'
```

### Solução

Usar o e‑mail *no‑reply* do GitHub (lembre-se de substituir `SEU_ID` e `SEU_USERNAME` pelo seu ID e seu username corretos, respectivamente):

```bash
git config user.email "SEU_ID+SEU_USERNAME@users.noreply.github.com"
```

No meu caso, o comando ficaria assim (veja mais abaixo como obter o seu `user ID` - e espero que você saiba o seu `username`):

```bash
git config user.email "27902382+AlexandreMeslin@users.noreply.github.com"
```

Você consegue obter o seu ID com o seguinte comando:

```bash
curl -s https://api.github.com/users/SEU_USERNAME | grep '"id"'
```

---

## O *branch* do PR tem conflitos com o conteúdo do repositório origem

### Descrição

Existem um ou mais conflitos que o Git não consegue resolver automaticamente.
Uma intervenção manual (sua) é necessária.

### Sintoma:

Ao tentar fazer o *merge* você se depara com a seguinte mensagem de erro: 
**This branch has conflicts that must be resolved**.

### Solução:

- Você recebeu um **Pull Request** (PR):

![Pull request](img/GIT-merge1.png)

- Você está pronto para aceitar o *merge*:

![Lista de PR](img/GIT-merge2.png)

- Mas você se depara com a seguinte mensagem de erro:

![Mensagem de erro](img/GIT-merge3.png)

- Clique em `Resolve conflicts`:
- Resolva os conflitos clicando em 
    - `Accept current change`
    - `Accept incoming change`
    - `Accept both changes`

![Solução de conflitos](img/GIT-merge4.png)

> Opcionalmente você pode apenas resolver o conflito removendo as linhas com `<<<`, `===` e `>>>` e editando o conflito.

- Use `Prev` e `Next` para navegar entre os conflitos.
- Quanto todos os conflitos estiverem resolvidos, clique no botão `Mark as resolved`:

![Resolvido](img/GIT-merge5.png)

- Resolva todos os conflitos e todos os arquivos. Ao terminar, clique em `Commit merge`:

![Commit](img/GIT-merge6.png)

- Agora você está pronto para realizar o *merge* do *pull request* . Clique no botão `Merge pull request* :

![Merge](img/GIT-merge7.png)

- Confirme o *merge* clicando no botão `Confirm merge`:

![Confirma o merge](img/GIT-merge8.png)

---

## Repositórios fora de sincronismo

### Descrição

Existe algum arquivo no repositório remoto que não está no repositório local.

### Sintoma

```bash
$ git push origin HEAD:master
To https://github.com/meslin8752/RegionAlert.git
 ! [rejected]        HEAD -> master (fetch first)
error: failed to push some refs to 'https://github.com/meslin8752/RegionAlert.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

### Solução

```bash
git pull origin master --allow-unrelated-histories
```

---


## Merge não terminado

### Descrição

O **Git** iniciou um *merge* anteriormente e ele não foi finalizado, por isso existe o arquivo interno `MERGE_HEAD`.
Enquanto isso não for resolvido, nenhum git pull ou novo merge é permitido.

### Sintoma

```
> git pull --tags origin main
error: You have not concluded your merge (MERGE_HEAD exists).
hint: Please, commit your changes before merging.
fatal: Exiting because of unfinished merge.
```

### Solução

Verifique se você já resolveu todos os conflitos com o comando:

```bash
git status
```

Saída esperada no caso de não haver mais conflitos

```bash
git status
On branch main
Your branch and 'origin/main' have diverged,
and have 1 and 6 different commits each, respectively.
  (use "git pull" if you want to integrate the remote branch with yours)

All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   ../AI1-HTML/README.md
        modified:   ../Sprint-1_GIT/README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        ../Sprint-1_GIT/img/git-ahead-behind.png
```

Se você ainda não resolveu todos os conflitos, verifique quais arquivos ainda devem ser analisados e resolva todos os conflitos.

Termine o merge com os seguintes comandos (leia atentamente o que cada um comando está precisando que você execute):

```bash
git commit
git pull --tags origin main
```

Saída esperada:

```bash
git commit
[main c4d0aaf] Merge branch 'main' of https://github.com/AlexandreMeslin/ENG4021
@AlexandreMeslin ➜ /workspaces/ENG4021/GIT (main) $ git pull --tags origin main
From https://github.com/AlexandreMeslin/ENG4021
 * branch            main       -> FETCH_HEAD
Already up to date.
```

---

# Comandos utilizados

```bash
    git add .
    git checkout main
    git commit
    git commit -m "Atualiza função principal e README"
    git fetch upstream
    git merge upstream/main
    git pull --tags origin main --no-rebase
    git push origin main
    git remote -v
    git remote add upstream https://github.com/aluno1/ENG4021.git
    git status
```

## Para criar uma tag:

```bash
git tag -a v2025.2 -m "Release version 2025.2"
git push origin --tags
```

Resultado esperado:

```
Enumerating objects: 1, done.
Counting objects: 100% (1/1), done.
Writing objects: 100% (1/1), 173 bytes | 173.00 KiB/s, done.
Total 1 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/AlexandreMeslin/INF1018
 * [new tag]         v2025.2 -> v2025.2
```
