from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import choice
import xPath
from selenium.webdriver import Firefox
from fordev.generators import people, uf, cnpj as generateCNPJ, state_registration as generateIE


browser = Firefox()

browser.get('https://ispsaude.com.br/')

# Gerador de dados aleatorios do 4Devs
estado = uf()
pessoa = people(uf_code=estado[0], formatting=False)
Telefone = pessoa.get('celular').split()
Telefone = Telefone[0]
ddd = Telefone[0:2]
numero = Telefone[1:12]
CPF = pessoa.get('cpf').split()
CPF = CPF[0]
# dataNasc = pessoa.get('data_nasc')
# dataNasc = dataNasc[0]


def realizarCadastro():
    Entre = browser.find_element_by_xpath(xPath.signUp)
    Entre.click()
    sleep(3.5)
    
    Email = browser.find_element_by_xpath(xPath.cadEmail)
    sleep(0.3)
    Email.send_keys(pessoa.get('email'))
    sleep(1)
    
    Senha = browser.find_element_by_xpath(xPath.cadSenha)
    sleep(0.3)
    Senha.send_keys('teste123')
    sleep(0.5)
    mostrarSenha = browser.find_element_by_xpath(xPath.showSigninPasswordCad)
    mostrarSenha.click()
    sleep(1)
    mostrarSenha.click()
    sleep(1)

    DDD = browser.find_element_by_xpath(xPath.cadDDD)
    sleep(0.3)
    DDD.send_keys(ddd)
    sleep(1)

    Telefone = browser.find_element_by_xpath(xPath.cadTelefone)
    sleep(0.3)
    Telefone.send_keys(numero)
    sleep(1)

    Nome = browser.find_element_by_xpath(xPath.cadNome)
    sleep(0.3)
    Nome.send_keys(pessoa.get('nome'))
    sleep(1)
    
    Cpf = browser.find_element_by_xpath(xPath.cpf)
    for x in range(11):
        Cpf.send_keys(Keys.BACKSPACE)
        Cpf.send_keys(CPF[x])
    sleep(1)

    Data = browser.find_element_by_xpath(xPath.cadData)
    for y in range(8):
        Data.send_keys(Keys.BACKSPACE)
        #Data.send_keys(dataNasc[y])
    Data.send_keys('data_nasc')
    sleep(1)

    Cadastrar = browser.find_element_by_xpath(xPath.cadastrar)
    Cadastrar.click()
    
try:
    realizarCadastro()
    sleep(3)

finally:
    sleep(2)
    # browser.quit()