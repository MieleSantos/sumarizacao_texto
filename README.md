# Sumarização de texto com python



1 - Pré-processamento do texto<br>
2 - Frequência das palavras<br>
3 - Tokenização das Sentenças<br>
4 - Geração do resumo(nota para as sentenças)

# Configurando ambiente
### Poetry

#### O que é?

Poetry é uma ferramenta de gerenciamento de dependências do python. Auxilia na instalação de pacotes e ajuda na configuração do ambiente de desenvolvimento.

#### Para que serve?
Utilizaremos o poetry para controlar a versão das bibliotecas utilizadas para desenvolvimento do sistema. Com ele podemos baixar uma versão específica de uma biblioteca ou facilmente atualizar suas dependências.

Ele também nos ajuda a manter um ambiente isolado de desenvolvimento entre pacotes e dependências.

O poetry nos ajuda a ter um ambiente separado para cada projeto.

### Como instalar?

`curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -`

Abra um terminal e digite:

`poetry --version`

Obs: `caso não apareça fecha o terminal oou reiniciar o pc`

Caso já tem o `poetry.lock`, use o comando 
`poetry shell` para criar o ambiente  depois use `poetry install` ele vai instalar todas as bibliotecas do arquivo poetry.lock

Se não segue o passo a passo para configura

#### Iniciando um projeto Python

Agora com o repositório criado, vamos começar a criar um projeto Python.

Execute o comando:

`poetry init -n`

Obs:``` A opção -n evita que o poetry fique perguntando algumas opções do projeto. Considere remove-la em próximos projetos.```

Este comando iniciliza um arquivo `pyproject.toml` de configuração do projeto.

Com o projeto iniciado, vamos instalar as dependências.

Exemplo de instalação

Execute o comando:

`poetry add fastapi`

Vamos verificar se deu tudo certo?
Execute

`poetry run python -c "import fastapi"`

### isort

#### O que é?

isort é uma ferramenta que ordena de forma alfabética as importações, separando as bilbiotecas que são padrões da linguagem, as externas ao sistema e as nativas do próprio sistema.

#### Para que serve?

O isort irá modificar o seu código ordenando as importações alfabéticamente. Dessa forma, o bloco de importações fica organizado e padronizado no projeto.

#### Como instalar

Execute o comando abaixo:

`poetry add isort --dev`
Obs: `Utilizamos a opção --dev pois é um pacote necessário somente durante o desenvolvimento e não durante a execução do software.`

#### Configuração

Precisamos adicionar no arquivo `pyproject.toml` a seguinte configuração
```bash
   [tool.isort]
   profile = "black"
   line_length = 80
```
Como executar
`poetry run isort .`

#### Black

#### O que é?

Black é o formatador de código Python intransigente. Ao usá-lo, você concorda em ceder o controle sobre as minúcias da formatação manual. Em troca, o black dá a você velocidade, determinismo e liberdade do irritante pycodestyle sobre formatação. Você economizará tempo e energia mental para assuntos mais importantes.

#### Para que serve?

O black é um formatador automático de código, ele irá modificar o seu código seguindo o guia de estilo do Python. Iremos configurá-lo junto ao nosso editor para que a formatação seja feita através de um atalho do teclado como shift + ctrl + i.

Como instalar
Execute o comando abaixo:

`poetry add black --dev`

#### Configuração

Precisamos adicionar no arquivo pyproject.toml a seguinte configuração
```bash
[tool.isort]
profile = "black"
line_length = 80
```
Como executar
`poetry run black .`

Para remover uma biblioteca com poetry:
```bash
poetry remove <nome>
```

Habilitar ambiente virtual:
```bash
poetry shell
```

Para instalar a partir dos arquivos poetry.lock
```bash
poetry install
```