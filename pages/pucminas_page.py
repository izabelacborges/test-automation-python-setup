# encoding: utf-8

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.base_element import BaseElement
from selenium.webdriver.support.ui import WebDriverWait

class PucminasPage(BaseElement):

    INPUT_MATRICULA = (By.NAME,"S33_")
    INPUT_SENHA = (By.NAME, "S35_")


    def type_matricula(self, matricula):
        self.type(self.INPUT_MATRICULA, matricula)

    def type_senha(self, senha):
        self.type(self.INPUT_SENHA, senha)