# Configuração e instalação de ambiente - Mac OS Sierra / OS X

### Instalando e configurando o `python`
1. __Instalação__
    
    Mesmo o python já vindo pré-instalado no Mac, é recomendável reinstalá-lo via Homebrew para evitar incompatibilidade com algumas bibliotecas.
    ```shell
        brew doctor
        brew update
        brew install python   #for python 2
    ```
2. __Alteração do `$PATH`__

    Abra o arquivo bash com:
    ```shell
        vim ~/.bash_profile
    ```
    e adicione:
    ```shell
        export PATH=/usr/local/bin:$PATH
        test -f ~/.bashrc && source ~/.bashrc
    ```
    Salve e saia do arquivo vim. Em seguida, para aproveitar as alterações do bash na sessão atual do terminal, execute:
    ```shell
        source ~/.bash_profile
    ```
3. __Instalação e configuração de ambiente virtual__
    
    ```shell
        pip install virtualenv   #for python 2
    ```
    Agora vamos criar diretórios para salvar os ambientes virtuais e arquivos de configuração:
    ```shell
        mkdir -p ~/Virtualenvs ~/Library/Application\ Support/pip
    ```
    Em seguida, abra o arquivo de configuração
    ```shell
        vim ~/Library/Application\ Support/pip/pip.conf
    ```
    E adicione:
    ```shell
        [install]
        require-virtualenv = true

        [uninstall]
        require-virtualenv = true
    ```
    com este passo você limita as instalações e desinstalações para apenas dentro dos ambientes virtuais, o que acaba evitando algumas dores de cabeça :D
    
    Agora é só criar o ambiente virtual com:
    ```shell
        cd ~/Virtualenvs
        virtualenv selenium2env                       #for Python 2
    ```
    Ative o ambiente virtual com: 
    ```shell
        cd selenium2env
        source bin/activate
    ```
    Agora que você está dentro do ambiente virtual você pode instalar qualquer biblioteca usando o pip.
    
    E desativar o ambiente com `deactivate`

### Clonando o repositório
Recomendo utilização do [GitKraken](http://gitkraken.com/) para melhor visualização do projeto no GitHub, e notificações sobre o estado do projeto. Com ele você deve dar um fork no meu projeto no GitHub e cloná-lo para a sua máquina.

Caso prefira fazer isso pelo terminal, navegue até o diretório em que você deseja que fique o projeto e clone o repositório com:
```shell
    git clone https://github.com/izabelacborges/test-automation-python-setup.git
```
Após clonar o repositório por qualquer um dos caminhos acima, instale as dependências com `pip install -r requirements.txt` dentro do ambiente virtual.

### Instalando o Chrome e o ChromeDriver:
1. __Chrome__

Este passo só deve ser reproduzido caso você não tenha o Chrome instalado em seu computador.

Instale o Chrome browser clicando [aqui](https://www.google.com/chrome/index.html).

2. __ChromeDriver__

```shell
brew install chromedriver
```
Se aparecer uma mensagem `"Warning: chromedriver already installed, it's just not linked"` execute o comando:
```shell
brew link --overwrite chromedriver
```
Se você está usando o Sierra pode passar por alguns problemas de permissão, para mudar as permissões de usuário, use:
```shell
sudo chown -R (whoami) /usr/local
```
refaça a instalação e o link (caso necessário) e volte a permissão de usuário para o padrão com:
```shell
sudo chown root:wheel /usr/local
```

### selenium-server-standalone
Para rodar os testes será necessário ter o selenium server. Você pode baixar o arquivo `.jar` [aqui](https://goo.gl/s4o9Vx).

Antes de executar os testes você precisa rodar o arquivo `.jar` com:
```shell
java -jar selenium-server-standalone-3.4.0.jar
```

### PyCharm IDE
Neste projeto foi usado o PyCharm. Você pode instalá-lo por [aqui](https://www.jetbrains.com/pycharm/download/).