# Configuração e instalação de ambiente - Linux Ubuntu

### Instalando e configurando o `python`
1. __Instalação `python` e `pip`__
    
    O Python já vem pré-instalado nas distribuições Ubuntu do Linux.
    Verifique utilizando os comandos `python2 --version` e `python3 --version`
    
    Caso não tenha, instale com os comandos a seguir:
    ```shell
        #para o python 2
        sudo apt-get update
        sudo apt-get install python2
    ```
    
    Para fazer o upgrade do pip:
    ```shell
        #para python 2
        pip install -U pip
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
        cd selenium2env2
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

```shell
sudo apt-get install libxss1 libappindicator1 libindicator7
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

sudo dpkg -i google-chrome*.deb
sudo apt-get install -f
```
2. __ChromeDriver__

```shell
sudo apt-get install unzip

wget -N http://chromedriver.storage.googleapis.com/2.30/chromedriver_linux64.zip -P ~/Downloads
    
unzip ~/Downloads/chromedriver_linux64.zip -d ~/Downloads
    
chmod +x ~/Downloads/chromedriver
sudo mv -f ~/Downloads/chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
```

### selenium-server-standalone
Para rodar os testes será necessário ter o selenium server. Você pode baixar o arquivo `.jar` [aqui](https://goo.gl/s4o9Vx).

Antes de executar os testes você precisa rodar o arquivo `.jar` com:
```shell
java -jar selenium-server-standalone-3.4.0.jar
```

### PyCharm IDE
Neste projeto foi usado o PyCharm. Você pode instalá-lo por [aqui](https://www.jetbrains.com/pycharm/download/).