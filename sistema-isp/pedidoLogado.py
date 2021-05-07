from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import choice
import xPath


PATH = "../chromedriver"
browser = webdriver.Chrome(PATH)
url = "https://next.ispsaude.com.br/"
browser.get(url)
browser.maximize_window()


def realizarPedido():
    Entre = browser.find_element_by_xpath(xPath.signin)
    Entre.click()
    sleep(3.5)
    
    Email = browser.find_element_by_xpath(xPath.username)
    Email.send_keys('bea@teste.com')
    sleep(1)
    
    Senha = browser.find_element_by_xpath(xPath.signinPassword)
    Senha.send_keys('teste123')    
    mostrarSenha = browser.find_element_by_xpath(xPath.showSigninPassword)
    mostrarSenha.click()
    sleep(1)
    mostrarSenha.click()
    sleep(1)
    
    Entrar = browser.find_element_by_xpath(xPath.login)
    Entrar.click()
    sleep(3)

    Pesquisa = browser.find_element_by_xpath(xPath.pesquisaProduto)
    sleep(3)
    Pesquisa.send_keys('bola')
    Pesquisa.send_keys(Keys.ENTER)
    sleep(1)

    SelecionaProduto = browser.find_element_by_xpath(xPath.selecionaProduto)
    sleep(3)
    SelecionaProduto.click()
    sleep(5)

    AdicionarCarrinho = browser.find_element_by_xpath(xPath.addCarrinho)
    AdicionarCarrinho.click()
    sleep(5)

    Carrinho = browser.find_element_by_xpath(xPath.carrinho)
    sleep(3)
    Carrinho.click()
    sleep(3)

    FecharPedido = browser.find_element_by_xpath(xPath.fecharPedido)
    sleep(3)
    FecharPedido.click()
    sleep(2)

    EntregaPedido = browser.find_element_by_xpath(xPath.entrega)
    EntregaPedido.click()
    sleep(10)

    Opcao = browser.find_element_by_xpath(xPath.opcaoEnvio)
    Opcao.click()
    sleep(5)

    Pagamento = browser.find_element_by_xpath(xPath.formaPagamento)
    Pagamento.click()
    sleep(5)

    NumeroCartao =  browser.find_element_by_xpath(xPath.numeroCartao)
    NumeroCartao.click()
    NumeroCartao.send_keys('5330400837737297')
    sleep(5)

    NomeTitular = browser.find_element_by_xpath(xPath.nomeTitular)
    NomeTitular.click()
    NomeTitular.send_keys('Beatriz Snichelotto')
    sleep(5)

    DataValidade = browser.find_element_by_xpath(xPath.dataValidade)
    DataValidade.click()
    DataValidade.send_keys('02/2022')
    sleep(5)
    
    CVV = browser.find_element_by_xpath(xPath.cvv)
    CVV.click()
    CVV.send_keys('637')
    sleep(5)

    Parcelamento = browser.find_element_by_xpath(xPath.parcelamento)
    Parcelamento.click()
    sleep(5)

    ValorParcelamento = browser.find_element_by_xpath(xPath.valorParcelamento)
    ValorParcelamento.click()
    sleep(5)

    Tela = browser.find_element_by_xpath(xPath.tela)
    Tela.click()
    sleep(5)

    FinalizarPagamento = browser.find_element_by_xpath(xPath.finalizarPagamento)
    FinalizarPagamento.click()
    sleep(3)
    

try:
    realizarPedido()
    sleep(3)

finally:
    sleep(2)
    # browser.quit()
   