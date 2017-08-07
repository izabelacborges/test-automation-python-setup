
from pages.pucminas_page import PucminasPage
from base.base_test import TestCase

class TestSelenium(TestCase):

    def loginThenLogout_Test(self):
        pucminasPage = PucminasPage(self.driver)

        #Dados
        matricula = ""
        senha = ""

        pucminasPage.type_matricula(matricula)
        pucminasPage.type_senha(senha)
