from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import choice
import xPath


PATH = "../chromedriver"
browser = webdriver.Chrome(PATH)
url = "https://next.ispsaude.com.br/"
browser.get(url)


def realizarLogin():
    Entre = browser.find_element_by_xpath(xPath.signin)
    Entre.click()
    sleep(3.5)
    
    Email = browser.find_element_by_xpath(xPath.username)
    sleep(0.3)
    Email.send_keys('bea@teste.com')
    sleep(1)
    
    Senha = browser.find_element_by_xpath(xPath.signinPassword)
    sleep(0.3)
    Senha.send_keys('teste123')    
    sleep(0.5)
    mostrarSenha = browser.find_element_by_xpath(xPath.showSigninPassword)
    mostrarSenha.click()
    sleep(1)
    mostrarSenha.click()
    sleep(1)
    
    Entrar = browser.find_element_by_xpath(xPath.login)
    Entrar.click()
    sleep(1)

    Icone = browser.find_element_by_xpath(xPath.icon)
    Icone.click()
    sleep(5)

    MeusPedidos = browser.find_element_by_xpath(xPath.meusPedidos)
    MeusPedidos.click()
    sleep(5)

    UltimosPedidos = browser.find_element_by_xpath(xPath.ultimosPedidos)
    UltimosPedidos.click()
    sleep(5)

    Icone = browser.find_element_by_xpath(xPath.icon)
    Icone.click()
    sleep(6)

    LogOut = browser.find_element_by_xpath(xPath.logout)
    LogOut.click()
    sleep(5)

    
try:
    realizarLogin()
    sleep(3)

finally:
    sleep(5)
    browser.quit()