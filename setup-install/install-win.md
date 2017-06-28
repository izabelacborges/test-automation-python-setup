# Configuração e instalação de ambiente - Windows
Primeiramente, eu não recomendo, nem estimulo o desenvolvimento com Python no Windows.

Porém duas alternativas são:
1. Instalar o Python puro, de acordo com o [The Hitchhiker's Guide to Python](https://github.com/kennethreitz/python-guide);
    - Instalação do [Python 2](http://docs.python-guide.org/en/latest/starting/install/win/#install-windows)
    - Instalação do [Python 3](http://docs.python-guide.org/en/latest/starting/install3/win/#install3-windows)
2. Ou utilizar a distribuição do [Miniconda](https://conda.io/docs/install/quick.html) ou [Anaconda](https://conda.io/docs/install/full.html)

### Clonando o repositório
Recomendo utilização do [GitKraken](http://gitkraken.com/) para melhor visualização do projeto no GitHub, e notificações sobre o estado do projeto. Com ele você deve dar um fork no meu projeto no GitHub e cloná-lo para a sua máquina.

Caso prefira fazer isso pelo terminal, navegue até o diretório em que você deseja que fique o projeto e clone o repositório com:
```shell
    git clone https://github.com/izabelacborges/test-automation-python-setup.git
```
Após clonar o repositório por qualquer um dos caminhos acima, instale as dependências com `pip install -r requirements.txt` dentro do ambiente virtual.

### Instalando o Chrome e o ChromeDriver:
1. __Chrome__

Este passo só deve ser reproduzido caso você não tenha o Chrome instalado em seu computador. Você estando no Windows, se não pular este passo, creio que você é louco, ou muito hardcore...

Instale o Chrome browser clicando [aqui](https://www.google.com/chrome/index.html).

2. __ChromeDriver__

Você pode installar o Chromedriver mais recente por [aqui](https://chromedriver.storage.googleapis.com/2.30/chromedriver_win32.zip).

É tido como padrão que o executável fique em `C:\chromedriver.exe`

### selenium-server-standalone
Para rodar os testes será necessário ter o selenium server. Você pode baixar o arquivo `.jar` [aqui](https://goo.gl/s4o9Vx).

Antes de executar os testes você precisa rodar o arquivo `.jar` com:
```shell
java -jar selenium-server-standalone-3.4.0.jar
```

### PyCharm IDE
Neste projeto foi usado o PyCharm. Você pode instalá-lo por [aqui](https://www.jetbrains.com/pycharm/download/).