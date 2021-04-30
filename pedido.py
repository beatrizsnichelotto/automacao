from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import choice
import xPath
from fordev.generators import people, uf, cnpj as generateCNPJ, state_registration as generateIE

PATH = "../chromedriver"
browser = webdriver.Chrome(PATH)
url = "https://www.ispsaude.com.br/"
browser.get(url)


# Gerador de dados aleatorios do 4Devs
# estado = uf()
# pessoa = people(uf_code=estado[0], formatting=False)
# Telefone = pessoa.get('celular').split()
# Telefone = Telefone[0]
# ddd = Telefone[0:2]
# numero = Telefone[1:12]
# CPF = pessoa.get('cpf').split()
# CPF = CPF[0]


def realizarPedido():
    Pesquisa = browser.find_element_by_xpath(xPath.pesquisaProduto)
    sleep(3)
    Pesquisa.send_keys('bola')
    Pesquisa.send_keys(Keys.ENTER)
    sleep(1)

    SelecionaProduto = browser.find_element_by_xpath(xPath.selecionaProduto)
    sleep(3)
    SelecionaProduto.click()

    AdicionarCarrinho = browser.find_element_by_xpath(xPath.addCarrinho)
    sleep(3)
    AdicionarCarrinho.click()

    # Confirmar = browser.find_element_by_xpath(xPath.confirmar)
    # sleep(3)
    # Confirmar.click()

    Carrinho = browser.find_element_by_xpath(xPath.carrinho)
    sleep(3)
    Carrinho.click()

    FecharPedido = browser.find_element_by_xpath(xPath.fecharPedido)
    sleep(3)
    FecharPedido.click()

try:
    realizarPedido()
    sleep(3)

finally:
    sleep(2)
    # browser.quit()
   