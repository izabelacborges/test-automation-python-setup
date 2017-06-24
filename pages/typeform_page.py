# encoding: utf-8

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.base_element import BaseElement

class TypeformPage(BaseElement):

    NEXT = Keys.ENTER
    START_BUTTON = (By.XPATH, "//a[text()='Vamos lá?']")
    CANTOR_INPUT = (By.XPATH, "//div[@class='question']/span[text()='Melhor cantor']/parent::div/following-sibling::div[@class='content']/descendant::input")
    CANTORA_INPUT = (By.XPATH, "//div[@class='question']/span[text()='Melhor cantora']/parent::div/following-sibling::div[@class='content']/descendant::input")
    GRUPO_INPUT = (By.XPATH, "//div[@class='question']/span[text()='Melhor grupo']/parent::div/following-sibling::div[@class='content']/descendant::input")
    SHOW_INPUT = (By.XPATH, "//div[@class='question']/span[text()='Melhor show']/parent::div/following-sibling::div[@class='content']/descendant::input")
    MUSICA_INPUT = (By.XPATH, "//div[@class='question']/span[contains(text(),'Melhor m')]/parent::div/following-sibling::div[@class='content']/descendant::input")
    CHICLETE_INPUT = (By.XPATH, "//div[@class='question']/span[contains(text(),'chiclete')]/parent::div/following-sibling::div[@class='content']/descendant::input")
    EXPERIMENTE_INPUT = (By.XPATH, "//div[@class='question']/span[text()='Experimente']/parent::div/following-sibling::div[@class='content']/descendant::input")
    PERGUNTA_BUTTON = (By.XPATH, "//input[contains(@value,'Porchat') and contains(@value,'Werneck')]")
    SUBMIT = (By.XPATH, "//div[text()='Enviar meus votos!']")
    END_MESSAGE = (By.XPATH, "//*[text()='Obrigado pelo seu voto!']")

    def __init__(self, driver):
        BaseElement.__init__(self, driver)

    def click_start(self):
        self.click( self.START_BUTTON )

    def type_inputCantor(self, value):
        self.type( self.CANTOR_INPUT, value + self.NEXT )

    def type_inputCantora(self, value):
        self.type( self.CANTORA_INPUT, value + self.NEXT )

    def type_inputGrupo(self, value):
        self.type( self.GRUPO_INPUT, value + self.NEXT )

    def type_inputShow(self, value):
        self.type( self.SHOW_INPUT, value + self.NEXT )

    def type_inputMusica(self, value):
        self.type( self.MUSICA_INPUT, value + self.NEXT )

    def type_inputChiclete(self, value):
        self.type( self.CHICLETE_INPUT, value + self.NEXT )

    def type_inputExperimente(self, value):
        self.type( self.EXPERIMENTE_INPUT, value + self.NEXT )

    def click_perguntaHumano(self):
        #letter = self.get_element((By.XPATH, "//input[contains(@value,'Porchat') and contains(@value,'Werneck')]/following-sibling::div[@class='letter']/span")).get_attribute('text')
        self.click( self.PERGUNTA_BUTTON )
        self.click( self.SUBMIT )

    def assert_menssagemFinal(self):
        self.assert_this( self.END_MESSAGE )