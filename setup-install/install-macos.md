# Configuração e instalação de ambiente - Mac OS Sierra / OS X

### Instalando e configurando o `python`
1. __Instalação__
    
    ```shell
        brew doctor
        brew update
        brew install python   #for python 2
        brew install python3  #for python 3
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
    Salve e saia do arquivo vim, em seguida:
    ```shell
        source ~/.bash_profile
    ```
3. __Instalação e configuração de ambiente virtual__
    
    ```shell
        pip install virtualenv   #for python 2
        pip install venv         #for python 3
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
        virtualenv pytest2env  #for Python 2
        venv pytest3env        #for Python 3
    ```
    Ative o ambiente virtual com: 
    ```shell
        cd pytest2env  #or pytest3env
        source bin/activate
    ```
    Agora que você está dentro do ambiente virtual você pode instalar qualquer biblioteca usando o pip.
    
    E desativar o ambiente com `deactivate`

### Clonando o repositório
No terminal, navegue até o diretório em que você deseja que fique o projeto e clone o repositório com:
```shell
    git clone https://github.com/belacb/test-automation-python-setup.git
```
E instale as dependencias com `pip install -r requirements.txt`

### Instalando o Chrome Driver:
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

### PyCharm IDE
Neste projeto foi usado o PyCharm. Você pode instalá-lo por [aqui](https://www.jetbrains.com/pycharm/download/).