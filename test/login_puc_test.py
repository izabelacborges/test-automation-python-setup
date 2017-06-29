
from pages.pucminas_page import PucminasPage
from base.base_test import TestCase

class TestSelenium(TestCase):

    def loginThenLogout_Test(self):
        pucminasPage = PucminasPage(self.driver)

        #Dados
        matricula = "463243"
        senha = "pucminas463243"

        pucminasPage.type_matricula(matricula)
        pucminasPage.type_senha(senha)