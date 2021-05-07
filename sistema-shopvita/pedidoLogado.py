from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import choice
import xPath


PATH = "../chromedriver"
browser = webdriver.Chrome(PATH)
url = "https://next.shopvita.com.br/"
browser.get(url)
browser.maximize_window()


def realizarPedido():
    Entre = browser.find_element_by_xpath(xPath.signin)
    sleep(3)
    Entre.click()
    sleep(3)
    
    Email = browser.find_element_by_xpath(xPath.username)
    sleep(2)
    Email.send_keys('bea@teste.com')
    sleep(3)
    
    Senha = browser.find_element_by_xpath(xPath.signinPassword)
    sleep(2)
    Senha.send_keys('teste123')    
    sleep(3)
    mostrarSenha = browser.find_element_by_xpath(xPath.showSigninPassword)
    mostrarSenha.click()
    sleep(1)
    mostrarSenha.click()
    sleep(1)
    
    Entrar = browser.find_element_by_xpath(xPath.login)
    Entrar.click()
    sleep(5)

    Pesquisa = browser.find_element_by_xpath(xPath.pesquisaProduto)
    sleep(5)

    Atualizar = browser.find_element_by_xpath(xPath.atualizar)
    Atualizar.click()
    sleep(5)

    Pesquisa = browser.find_element_by_xpath(xPath.pesquisaProduto)
    sleep(5)

    Atualizar = browser.find_element_by_xpath(xPath.atualizar)
    Atualizar.click()
    sleep(5)

    Pesquisa = browser.find_element_by_xpath(xPath.pesquisaProduto)
    sleep(5)
    Pesquisa.send_keys('bola')
    Pesquisa.send_keys(Keys.ENTER)
    sleep(3)

    SelecionaProduto = browser.find_element_by_xpath(xPath.selecionaProduto)
    sleep(3)
    SelecionaProduto.click()

    AdicionarCarrinho = browser.find_element_by_xpath(xPath.addCarrinho)
    sleep(3)
    AdicionarCarrinho.click()
    sleep(1)

    Carrinho = browser.find_element_by_xpath(xPath.carrinho)
    sleep(3)
    Carrinho.click()
    sleep(3)

    FecharPedido = browser.find_element_by_name('Fechar Pedido')
    FecharPedido.click()
    sleep(6)

    Opcao = browser.find_element_by_xpath(xPath.opcaoEnvio)
    Opcao.click()
    sleep(6)

    Pagamento = browser.find_element_by_xpath(xPath.formaPagamento)
    Pagamento.click()
    sleep(6)

    FinalizarPagamento = browser.find_element_by_xpath(xPath.finalizarPagamento)
    FinalizarPagamento.click()
    sleep(3)
    
try:
    realizarPedido()
    sleep(3)

finally:
    sleep(2)
    # browser.quit()
   