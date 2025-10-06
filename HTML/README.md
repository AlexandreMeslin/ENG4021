# Roteiro de HTML/CSS

# HTML

1. Crie um repositório - não use o mesmo repositório do seu projeto com o seu time. Ao criar o repositório, inclua o arquivo `README.md` e o arquivo `.gitignore` para `Python`.

1. Abra o Codespace do seu repositório.

1. Crie uma pasta chamada `HTML` para os arquivos HTML. Dentro dessa pasta, crie uma pasta chamada `css` e outra chamada `img` para você armazenar as folhas de estilo e as imagens, respectivamente.

1. Crie um arquivo chamado `index.html` na pasta `HTML`.

1. Insira o seguinte código (basta digitar `html` e selecionar a opção `HTML 5`):
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        
    </body>
    </html>
    ```

1. Troque o idioma para português do Brasil e inclua um título para a aba do navegador.

1. Coloque o conteúdo desse [arquivo](./conteudo.txt) entre as tags `<body>` e `</body>`.

1. Instale o *plugin* `Live Preview` da **Microsoft** e depois digite `Ctrl+K` `V` para abrir a visualização.

    ![imagem do plugin a ser instalado](imagens/LivePreview.png)

    Utilize o plugin para visualizar cada uma das modificações que você fizer no documento. Para ativar o Live Preview, você pode digitar Ctrl+K` `V` ou clicar no ícone com uma janela dividida verticalmente e uma lupa (![ícone para ativar o Live Preview](imagens/live_preview_icon.png)) localizado do lado direito das abas junto às abas (o ícone somente aparece quando um arquivo HTML está selecionado para edição).

    > Se der erro na exibição da página HTML, clique na aba `Ports`. Clique em com o botão direito do mouse em cada uma das `Visibilty` das portas que estejam com o status de `Private`, selecione `Port Visibility` no menu suspenso que irá aparecer e troque a visibilidade para `Public`. Feche a aba de visualização HTML que deu erro e tente novamente clicando no ícone de visualização.
    !(Aba ![Aba Ports](imagens/aba_ports.png)
    Se a aba `Ports` não estiver visível, pressione Ctrl+Shift+P e digite `View: Toggle Ports` e clique no item para exibir a aba `Ports`
    

1. Formate o título principal com a tag `<h1>`.

    > A marcação da tag começa com a tag e termina com barra-tag. Por exemplo:
    >```html
    > <h1>Astronauta Spiff</h1>
    >```

1. Formate os títulos secundários com a tag `<h2>`. Exemplo de títulos secundários:
    - Resumo
    - Experiência Profissional
    - Habilidades Técnicas Espaciais
    - Habilidades Pessoais
    - Educação (Auto-Didata e Experiencial)
    - Idiomas

1. Coloque o texto abaixo em `<h3>`:
    - Astronauta Intergalático e Comandante de Missão Solo

1. Coloque os seguintes parágrafos dentro das tags `<p>`:
    - Um intrépido e imaginativo astronauta com vasta experiência em exploração espacial solo e em missões críticas a planetas inóspitos.
                Proficiente em pilotagem de naves espaciais de construção própria,
                análise de fenômenos alienígenas e resolução criativa de problemas em ambientes extraterrestres.
                Possui um histórico comprovado de descobertas notáveis e encontros (nem sempre amigáveis) com formas de vida alienígenas diversas.
    - Várias Expedições (Contínuo)

1. Copie essa [figura](Spiff/img/spiff.jpeg) para a pasta `img`

1. Inclua a figura na sua página usando a tag `img` como mostrado a seguir: 
    ```html
    <img src='img/spiff.jpeg' alt='Foto do astronauta Spiff em ação'>
    ```
    > O texto no atributo `alt` é muito importante para tornar o seu site inclusivo. Ele facilita o entendimento do contexto da figura para aplicativos que fazem leitura de página para usuários com deficiência visual.

1. Crie uma lista numerada usando a tag `<ol></ol>` envolvendo todos os elementos da lista. Envolva individualmente cada um dos elementos da lista com a tag `<li></li>`. Use o seguinte texto:
    - Doutorado em Exploração Interdimensional e Defesa Contra Alienígenas Malignos (Honras Imaginárias)
    - Mestrado em Viagem Hiperespacial (com honras)
    - Universidade Estelar de Calvin — Ciências da Galáxia
    - Academia Estelar de Calvin — Diploma em Engenharia Espacial e Aventuras
    - Currículo incluiu estudos avançados em:

1. Em outra parte do texto, crie uma lista não-numerada (com *bullets*). Uma lista não numerada é construída de forma exatamente igual a uma lista numerada, apenas substituindo a tag `<ol>` pela tag `<ul>`. Crie a seguinte lista não numerada dentro da lista numerada criada anteriormente (fora do `<li>` mas ainda dentro do `<ol>`):
    - Teoria da Propulsão a Jato de Papelão
    - Linguística Alienígena Intuitiva
    - Táticas de Fuga e Evasão Escolar Espacial
    - Astronomia de Quintal Avançada
    - Sobrevivência com Lancheiras e Suco de Limão

1. Antes do seu texto (antes de tudo, mas ainda dentro de `<body>`), crie um container usando a tag `<nav>`. Copie o seguinte texto para dentro desse container: 
    ```ascii
    Menu Estelar
    PUC-Rio
    Resumo
    Habilidades
    Educação
    Idiomas
    Versão 2
    Meu currículo
    ```
1. Coloque a 1a linha como título `<h2>`. Coloque o restante das linhas como itens de uma lista não numerada

1. Crie um link para o site da PUC-Rio usando a tag `<a>` como mostrado a seguir:
    ```html
    <a href="http://www.puc-rio.br">PUC-Rio</a>
    ```

1. Crie um arquivo chamado `meu-curriculo.html` na pasta `HTML`.

1. Inclua um link para esse arquivo como mostrado a seguir:
    ```html
    <a href="meu-curriculo.html">Meu currículo</a>
    ```

1. Inclua links para seções do seu arquivo usando o seguinte formato:
    ```html
    <a href="#resumo">Resumo</a>
    ```
    E envolva cada uma das seções do seu texto `HTML` com a tag `<section></section>` como mostrado a seguir:
    ```html
    <section id="resumo">
        Um monte de texto aqui...
    </section>
    ```
    > A identificação (`id`) dever ser única por página.

1. Crie uma seção com a tag do tipo container `<footer>` com o seguinte texto:
    - "Nenhum alienígena fica para trás... porque eu desintegro todos!"   

1. Coloque todo o texto (menos o que estiver em `<nav>` e `<footer>`) dentro de uma tag container `<main>`.

1. Inclua no texto, uma tabela com as disciplinas que você já cursou com:
    - Código da disciplina
    - Nome da disciplina
    - Ano e semestre
    - Nome do professor
    
    Uma tabela é escrita dentro de `<table>`. Cada linha da tabela é escrita dentro de `<tr>` e cada célula (conteúdo) é escrita dentro de `<td>`. Uma tabela também pode ter células de cabeçalho (com destaque) escritas dentro de `<th>`. Opcionalmente, por motivos semânticos, uma tabela também pode (deve) ter `<thead>`, `<tbody>` e `<tfoot>`. Por exemplo:
    ```html
    <table>
        <thead>
            <tr>
                <th>Aluno 1</th>
                <th>Aluno 2</th>
                <th>Aluno 3</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Araci do Precioso Sangue</td>
                <td>Asteroide Silverio</td>
                <td>Cafiaspirina Cruz</td>
            </tr>
            <tr>
                <td>8</td>
                <td>7</td>
                <td>5</td>
            </tr>
        </tbody>
        <tfoot>
            <tr>
                <td>Rodapé 1</td>
                <td>Rodapé 2</td>
                <td>Rodapé 3</td>
            </tr>
        </tfoot>
    </table>
    ```
    Resultado:
    <table>
        <thead>
            <tr>
                <th>Aluno 1</th>
                <th>Aluno 2</th>
                <th>Aluno 3</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Araci do Precioso Sangue</td>
                <td>Asteroide Silverio</td>
                <td>Cafiaspirina Cruz</td>
            </tr>
            <tr>
                <td>8</td>
                <td>7</td>
                <td>5</td>
            </tr>
        </tbody>
        <tfoot>
            <tr>
                <td>Rodapé 1</td>
                <td>Rodapé 2</td>
                <td>Rodapé 3</td>
            </tr>
        </tfoot>
    </table>

# CSS - Cascading Style Sheets

1. Crie um arquivo chamado `curriculo.css` na pasta `css`.

1. Crie um link CSS do arquivo HTML para o arquivo `css/curriculo.css` como mostrado a seguir:
    ```html
        <link rel="stylesheet" href="css/curriculo.css">
    ```

1. Troque a cor de fundo da página para preto. As cores podem ser especificadas pelo seu nome (o resultado não é exato) ou pela quantidade de Vermelho (R), Verde (G) e Azul (B), com valores variando, para cada um, entre 0 e 255, em decimal, ou o seu equivalente em hexadecimal, onde 0 é a total ausência do compontente na cor e 255 é a quantidade máxima do componente (o resultado é exato). Os valores em hexadecimal são escritos com `#` antes do número. Por exemplo, letra vermelha nos parágrafos pode ser descrita como:

    ```css
    p {
        color: red;
    }
    ```
    ou
    ```css
    p {
        color: #FF0000;
    }
    ```

    > Note que o VS-Code mostra um quadrado com a cor selecionada numericamente.

    A cor de fundo de um elemento é dada pelo atributo `background-color`. Em resumo, aplique cor preta (#000000) ao atributo `background-color` para a  tag `<body>` no arquivo CSS.

1. Troque a cor dos textos dos parágrafos para branco, ou seja, o valor máximo de `RGB`.

1. Troque também o tipo de fonte para `Orbitron` através do atributo `font-family`. Esse tipo de fonte não é padrão para os seus usuários mas está disponível no site do Google, então inclua, na seção `<head>` um link para o navegador fazer donwload:
    ```html
        <link href="https://fonts.googleapis.com/css2?family=Orbitron&display=swap" rel="stylesheet">
    ```

1. Mude a cor de fundo da barra de navegação para azul.

1. No seu código HTML, coloque os links de navegação em uma lista não numerada. Coloque essa lista na classe `navegacao` usando o atributo class. Na folha de estilo, crie uma classe `.navegacao` como mostrado a seguir. Examine o efeito dessa classe nos links de navegação.
    ```css
    .navegacao {
       list-style-type: none;
    }
    ```

1. Remova o sublinhado dos links e troque a sua cor para amarelo, mas somente dos links que estiverem dentro de um objeto da classe `navegacao`. Para isso, no CSS, informe o nome da classe seguido da tag para criar link. Para remover o sublinhado, use atributo `text-decoration` e coloque o seu valor como `none`.

1. Coloque os títulos `h1`, `h2` e `h3` com texto amarelo e margem a esquerda de 10px.

1. Alinhe os parágrafos com os títulos.

1. Coloque o texto do rodapé como laranja.

1. Coloque o sumário do currículo dentro de um container do tipo `<div>`. Identifique esse container como `sumario`. Troque a cor do texto e do alinhamento desse texto. Para referenciar esse container no CSS, use o formato `#sumario`.

# Próxima Aula

>Na próxima aula iremos resolver o problema da *responsividade*  da página.
