from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import choice
import xPath


PATH = "../chromedriver"
browser = webdriver.Chrome(PATH)
url = "https://next.ispsaude.com.br/"
browser.get(url)


def alterarDados():
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
    sleep(2)

    Icone = browser.find_element_by_xpath(xPath.icon)
    Icone.click()
    sleep(5)

    MinhaConta = browser.find_element_by_xpath(xPath.minhaConta)
    MinhaConta.click()
    sleep(5)

    MeusDados = browser.find_element_by_xpath(xPath.meusDados)
    MeusDados.click()
    sleep(5)

    ListaTelefones = browser.find_element_by_xpath(xPath.listaTelefones)
    ListaTelefones.click()
    sleep(5)

    AdicionarTelefone = browser.find_element_by_xpath(xPath.addTelefone)
    AdicionarTelefone.click()
    sleep(5)

    DDD = browser.find_element_by_xpath(xPath.ddd)
    sleep(0.3)
    DDD.click()
    DDD.send_keys('45')
    sleep(1)

    Telefone = browser.find_element_by_xpath(xPath.telefone)
    sleep(0.3)
    Telefone.click()
    Telefone.send_keys('999901010')
    sleep(1)

    TipoTelefone = browser.find_element_by_xpath(xPath.tipoTelefone)
    TipoTelefone.click()
    sleep(5)
    Adicional = browser.find_element_by_xpath(xPath.adicional)
    Adicional.click()
    sleep(5)

    SalvarTelefone = browser.find_element_by_xpath(xPath.salvarTelefone)
    SalvarTelefone.click()
    sleep(5)

    ExcluirTelefone = browser.find_element_by_xpath(xPath.excluirTelefone)
    ExcluirTelefone.click()
    sleep(5)
    Confirmar = browser.find_element_by_xpath(xPath.confirmarExclusaoTel)
    Confirmar.click()
    sleep(5)

    EditarTelefone = browser.find_element_by_xpath(xPath.editarTelefone)    
    EditarTelefone.click()
    sleep(5)

    TelefoneEditado = browser.find_element_by_xpath(xPath.telefoneEdit)    
    for x in range(10):
        TelefoneEditado.send_keys(Keys.BACKSPACE)
    TelefoneEditado.send_keys('999628373')
    sleep(5)
    SalvarEdicao = browser.find_element_by_xpath(xPath.salvarEdicaoTel)    
    SalvarEdicao.click()
    sleep(5)

    ListaEnderecos = browser.find_element_by_xpath(xPath.listaEnderecos)
    ListaEnderecos.click()
    sleep(5)

    AdicionarEndereco = browser.find_element_by_xpath(xPath.adicionarEndereco)
    AdicionarEndereco.click()
    sleep(5)

    CEP = browser.find_element_by_xpath(xPath.cep)
    CEP.click()
    CEP.send_keys('85807-676')
    sleep(2)
    Numero = browser.find_element_by_xpath(xPath.numero)
    Numero.click()
    Numero.send_keys('10')
    sleep(5)

    SalvarEndereco = browser.find_element_by_xpath(xPath.salvarEndereco)
    SalvarEndereco.click()
    sleep(5)

    ExcluirEndereco = browser.find_element_by_xpath(xPath.excluirEndereco)
    ExcluirEndereco.click()
    sleep(5)
    Confirmar = browser.find_element_by_xpath(xPath.confirmarExclusaoEnd)
    Confirmar.click()
    sleep(5)

    EditarEndereco = browser.find_element_by_xpath(xPath.editarEndereco)    
    EditarEndereco.click()
    sleep(5)

    AdicionarComplemento = browser.find_element_by_xpath(xPath.addComplemento)
    AdicionarComplemento.send_keys('45B')
    sleep(5)
    SalvarEdicao = browser.find_element_by_xpath(xPath.salvarEdicaoEnd)    
    SalvarEdicao.click()
    sleep(5)
    EditarEndereco = browser.find_element_by_xpath(xPath.editarEndereco)    
    EditarEndereco.click()
    sleep(5)
    RemoverComplemento = browser.find_element_by_xpath(xPath.removerComplemento)
    for x in range(3):
        RemoverComplemento.send_keys(Keys.BACKSPACE)
    sleep(5)
    SalvarEdicao = browser.find_element_by_xpath(xPath.salvarEdicaoEnd)    
    SalvarEdicao.click()
    sleep(5)
   

    ListaEmails = browser.find_element_by_xpath(xPath.listaEmails)
    ListaEmails.click()
    sleep(5) 

    AdicionarEmail = browser.find_element_by_xpath(xPath.adicionarEmail)
    AdicionarEmail.click()
    sleep(5)

    NomeEmail = browser.find_element_by_xpath(xPath.nomeEmail)
    NomeEmail.click()
    NomeEmail.send_keys('Beatriz')
    sleep(2)
    NovoEmail = browser.find_element_by_xpath(xPath.novoEmail)
    NovoEmail.click()
    NovoEmail.send_keys('beatriz@teste.com')
    sleep(5)

    SalvarEmail = browser.find_element_by_xpath(xPath.salvarEmail)    
    SalvarEmail.click()
    sleep(5)

    ExcluirEmail = browser.find_element_by_xpath(xPath.excluirEmail)
    ExcluirEmail.click()
    sleep(5)
    Confirmar = browser.find_element_by_xpath(xPath.confirmarExclusaoEmail)
    Confirmar.click()
    sleep(5)

    # EditarEmail = browser.find_element_by_xpath(xPath.editarEmail)    
    # EditarEmail.click()
    # sleep(5)

    # CampoEmail = browser.find_element_by_xpath(xPath.campoEmail)    
    # for x in range(13):
    #     CampoEmail.send_keys(Keys.BACKSPACE)
    # CampoEmail.send_keys('beatriz.snichelotto@teste.com')
    # sleep(5)
    # SalvarEdicao = browser.find_element_by_xpath(xPath.salvarEdicaoEmail)    
    # SalvarEdicao.click()
    # sleep(5)

    # Alterar senha (1)
    AlterarSenha =  browser.find_element_by_xpath(xPath.alterarSenha)    
    AlterarSenha.click()
    sleep(5)
    SenhaAtual = browser.find_element_by_xpath(xPath.senhaAtual)
    SenhaAtual.click()
    SenhaAtual.send_keys('teste123')
    sleep(2)
    NovaSenha = browser.find_element_by_xpath(xPath.novaSenha)
    NovaSenha.click()
    NovaSenha.send_keys('senha123')
    sleep(2)
    ConfirmaSenha = browser.find_element_by_xpath(xPath.confirmaNovaSenha)
    ConfirmaSenha.click()
    ConfirmaSenha.send_keys('senha123')
    sleep(5)
    SalvarSenha =  browser.find_element_by_xpath(xPath.salvarSenha)    
    SalvarSenha.click()
    sleep(5)

    # Alterar senha (2)
    DadosPessoais = browser.find_element_by_xpath(xPath.dadosPessoais)
    DadosPessoais.click()
    sleep(5)
    AlterarSenha =  browser.find_element_by_xpath(xPath.alterarSenha)    
    AlterarSenha.click()
    sleep(5)
    SenhaAtual = browser.find_element_by_xpath(xPath.senhaAtual)
    SenhaAtual.click()
    SenhaAtual.send_keys('senha123')
    sleep(2)
    NovaSenha = browser.find_element_by_xpath(xPath.novaSenha)
    NovaSenha.click()
    NovaSenha.send_keys('teste123')
    sleep(2)
    ConfirmaSenha = browser.find_element_by_xpath(xPath.confirmaNovaSenha)
    ConfirmaSenha.click()
    ConfirmaSenha.send_keys('teste123')
    sleep(5)
    SalvarSenha =  browser.find_element_by_xpath(xPath.salvarSenha)    
    SalvarSenha.click()
    sleep(5)




try:
    alterarDados()
    sleep(3)

finally:
    sleep(5)
    # browser.quit()