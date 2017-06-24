# encoding: utf-8

from pages.typeform_page import TypeformPage
from base.base_test import TestCase

class TestSelenium(TestCase):

    def votingA_Test(self):
        typeformPage = TypeformPage( self.driver )

        typeformPage.click_start()
        typeformPage.type_inputCantor("Thiago Iorc")
        typeformPage.type_inputCantora("Ivete Sangalo")
        typeformPage.type_inputGrupo("Anavitoria")
        typeformPage.type_inputShow("Anavitoria")
        typeformPage.type_inputMusica("Trevo (Tu)")
        typeformPage.type_inputChiclete("Trevo (Tu)")
        typeformPage.type_inputExperimente("Anavitoria")
        typeformPage.click_perguntaHumano()
        typeformPage.assert_menssagemFinal()

    def votingB_Test(self):
        typeformPage = TypeformPage( self.driver )

        typeformPage.click_start()
        typeformPage.type_inputCantor("Thiago Iorc")
        typeformPage.type_inputCantora("Manu Gavassi")
        typeformPage.type_inputGrupo("Anavitoria")
        typeformPage.type_inputShow("Anavitoria")
        typeformPage.type_inputMusica("Trevo (Tu)")
        typeformPage.type_inputChiclete("Trevo (Tu)")
        typeformPage.type_inputExperimente("Anavitoria")
        typeformPage.click_perguntaHumano()
        typeformPage.assert_menssagemFinal()

    def votingC_Test(self):
        typeformPage = TypeformPage( self.driver )

        typeformPage.click_start()
        typeformPage.type_inputCantor("Thiago Iorc")
        typeformPage.type_inputCantora("Anitta")
        typeformPage.type_inputGrupo("Anavitoria")
        typeformPage.type_inputShow("Anavitoria")
        typeformPage.type_inputMusica("Trevo (Tu)")
        typeformPage.type_inputChiclete("Trevo (Tu)")
        typeformPage.type_inputExperimente("Anavitoria")
        typeformPage.click_perguntaHumano()
        typeformPage.assert_menssagemFinal()
