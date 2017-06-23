# Python Setup para Automação de Testes 

Este repositório compreende os materiais utilizados ao ministrar o minicurso de Processos de teste e automação de testes Web App na 5ª [Escola de Férias do ICEI](http://icei.pucminas.br/escoladeferias/) - PUC Minas, e tem o seguinte resumo:
> Durante o minicurso será explicado como é o processo de testes, como testar o seu software, porque o teste é necessário, (e porque a culpa é sempre do desenvolvedor!) Além de aprender na prática como usar o Selenium WebDriver para automatizar seus testes para aplicações web. 
> Os alunos poderão escolher entre as linguagens Python (neste repositório) e [Java](https://github.com/belacb/test-automation-java-setup) para desenvolver os scripts de automação.
> Como pré-requisito o aluno deverá trazer o próprio notebook, pois os processos de instalação são essenciais ao aprendizado.

### Slides
Se você está acompanhando o minicurso nesse momento você deve visualizar o slide clicando [aqui](https://slides.com/izabelacb/qaautomationsummerpuc/live#/).

Se você achou esse repositório por acaso, você pode acessar os slides [por aqui](http://slides.com/izabelacb/qaautomationsummerpuc#/).

### Instalação e configuração de ambiente
Para instalar e configurar o seu ambiente de testes automatizados em Python, você deve seguir o manual de instalação segundo seu sistema operacional:
* Mac OS Sierra / OS X: [`install-macos.md`](https://github.com/belacb/test-automation-python-setup/blob/master/setup-install/install-macos.md)
* Linux Ubuntu: [`install-linux.md`](https://github.com/belacb/test-automation-python-setup/blob/master/setup-install/install-linux.md)
* Windows: [`install-win.md`](https://github.com/belacb/test-automation-python-setup/blob/master/setup-install/install-win.md)

### Execução dos testes
Abra o Terminal, preferencialmente dentro do PyCharm. Será necessário ativar o ambiente virtual criado para os testes, e só aí executar o teste desejado. Os passos serão os seguintes:
```shell
source ~/Virtualenvs/pytest2env/bin/activate
nose path/to/test/test.py
```

### Licenças
Os códigos de exemplificação estão sob a __licença MIT__: https://opensource.org/licenses/MIT ou veja o [arquivo `LICENSE`](https://github.com/belacb/test-automation-python-setup/blob/master/LICENSE) 

E os materiais de apoio desenvolvidos estão sob a licença criativa __Creative Commons Attribution Share Alike 4.0__: https://creativecommons.org/licenses/by-sa/4.0/legalcode.txt ou veja o [arquivo `LICENSE.slides.md`](https://github.com/belacb/test-automation-python-setup/blob/master/LICENSE.slides.md)