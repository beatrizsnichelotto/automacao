from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import choice
import xPath


PATH = "../chromedriver"
browser = webdriver.Chrome(PATH)
url = "https://www.ispsaude.com.br/"
browser.get(url)


def esqueciSenha():
    Entre = browser.find_element_by_xpath(xPath.signin)
    Entre.click()
    sleep(3)
    
    EsqueciSenha = browser.find_element_by_xpath(xPath.esqueciSenha)
    EsqueciSenha.click()
    sleep(3)

    Email = browser.find_element_by_xpath(xPath.emailRecuperacao)
    Email.send_keys('snichelott.o@hotmail.com')
    sleep(3)
    
    Recuperar = browser.find_element_by_xpath(xPath.recuperar)
    Recuperar.click()
    sleep(3)
    
try:
    esqueciSenha()
    sleep(3)

finally:
    sleep(5)
    # browser.quit()