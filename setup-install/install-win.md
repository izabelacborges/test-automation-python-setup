# Configuração e instalação de ambiente - Windows
Primeiramente, eu não recomendo, nem estimulo o desenvolvimento com Python no Windows.

Porém duas alternativas são:
1. Instalar o Python puro, de acordo com o [The Hitchhiker's Guide to Python](https://github.com/kennethreitz/python-guide);
    - Instalação do [Python 2](http://docs.python-guide.org/en/latest/starting/install/win/#install-windows)
    - Instalação do [Python 3](http://docs.python-guide.org/en/latest/starting/install3/win/#install3-windows)
2. Ou utilizar a distribuição do [Miniconda](https://conda.io/docs/install/quick.html) ou [Anaconda](https://conda.io/docs/install/full.html)

### Clonando o repositório
No terminal, navegue até o diretório em que você deseja que fique o projeto e clone o repositório com:
```shell
    git clone https://github.com/belacb/test-automation-python-setup.git
```
E instale as dependencias com `pip install -r requirements.txt` dentro do ambiente virtual.

### Chromedriver
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