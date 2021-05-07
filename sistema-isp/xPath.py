# Comentários
    # selecionaProd = '//*[@id="products-show-case-category"]/div/div[1]/div[2]/a/div'
    # addProd = '//*[@id="__next"]/main/div/div[1]/div/div/div[3]/ul/li[5]/div[1]/button'
    # confirmar = '/html/body/div[12]/div[3]/div/div[3]/button[1]'


# Caminhos de login
   
signin = '//*[@id="__next"]/header/div[2]/div/div[3]/div/div/a[1]'
username = '//*[@id="__next"]/main/section/div/div/div/div/form/div/div[1]/div/input'
signinPassword = '//*[@id="__next"]/main/section/div/div/div/div/form/div/div[2]/div/input'
showSigninPassword = '//*[@id="__next"]/main/section/div/div/div/div/form/div/div[2]/div/button'
login = '//*[@id="__next"]/main/section/div/div/div/div/form/div/div[4]/button'


# Caminhos de cadastro

signUp = '//*[@id="__next"]/header/div[2]/div/div[3]/div/div/a[2]'
cadEmail = '//*[@id="__next"]/main/section/div/div/div/div/div/form/div[2]/div[1]/div/input'
cadSenha = '//*[@id="__next"]/main/section/div/div/div/div/div/form/div[2]/div[2]/div/input'
showSigninPasswordCad = '//*[@id="__next"]/main/section/div/div/div/div/div/form/div[2]/div[2]/div/button'
cadDDD = '//*[@id="__next"]/main/section/div/div/div/div/div/form/div[2]/div[3]/div[1]/div/div/input'
cadTelefone = '//*[@id="__next"]/main/section/div/div/div/div/div/form/div[2]/div[3]/div[2]/div/div/input'
cadNome = '//*[@id="__next"]/main/section/div/div/div/div/div/form/div[2]/div[4]/div/input'
cpf = '//*[@id="__next"]/main/section/div/div/div/div/div/form/div[2]/div[5]/div[1]/div/div/input'
cadData = '//*[@id="__next"]/main/section/div/div/div/div/div/form/div[2]/div[5]/div[2]/div/div/input'
cadastrar = '//*[@id="__next"]/main/section/div/div/div/div/div/form/div[3]/button'

# Caminhos de Pedido (não logado)

pesquisaProduto = "//input[@type='search']"
selecionaProduto = '//*[@id="products-show-case-category"]/div/div[3]/div[2]/a/div' 
addCarrinho = '//*[@id="__next"]/main/div/div[1]/div[1]/div/div[3]/ul/li[4]/div[1]/button'
carrinho = '//*[@id="__next"]/header/div[2]/div/div[3]/button[2]/span[1]'
fecharPedido = '//*[@id="fade-menu"]/div[3]/ul/li[3]/div[4]/div[1]'
loginPedido = '//*[@id="step-components"]/div/div[2]/form/div/div[1]/div/input'
senhaPedido = '//*[@id="step-components"]/div/div[2]/form/div/div[2]/div/input'
showSigninPasswordPed = '//*[@id="step-components"]/div/div[2]/form/div/div[2]/div/button'
entrar = '/html/body/div[2]/main/section/div/div/div/div[2]/div[2]/div/div[2]/form/div/div[4]/button/span[1]'
entrega = '//*[@id="step-components"]/div/div[2]/div[1]/div/div/div[1]/label/span[1]/span[1]/input'
opcaoEnvio = '//*[@id="step-components"]/div/div[2]/div[2]/div/ul/li/div/label/span[1]/span[1]/input'
formaPagamento = '//*[@id="step-components"]/div/div/div/ul/li[2]/div/div[1]/div[2]'
numeroCartao = '//*[@id="step-components"]/div/div/div/ul/li[2]/div/div[2]/div/div/div/div/div/form/div/div[1]/div/div/div/input'
nomeTitular = '//*[@id="step-components"]/div/div/div/ul/li[2]/div/div[2]/div/div/div/div/div/form/div/div[2]/div/div/div/input'
dataValidade = '//*[@id="step-components"]/div/div/div/ul/li[2]/div/div[2]/div/div/div/div/div/form/div/div[3]/div/div[1]/div/div/div/input'
cvv = '//*[@id="step-components"]/div/div/div/ul/li[2]/div/div[2]/div/div/div/div/div/form/div/div[3]/div/div[2]/div/div/div/input'
parcelamento = '//*[@id="parcela"]'
valorParcelamento = '//*[@id="menu-"]/div[3]/ul/li[1]'
tela = '//*[@id="__next"]/main/section/div/div/div/div[2]/div[3]'
finalizarPagamento = '//*[@id="step-components"]/div/div/div/ul/li[2]/div/div[2]/div/div/div/div/div/div[3]/div/button/span[1]'

# Caminhos de Pedido (logado)

signin = '//*[@id="__next"]/header/div[2]/div/div[3]/div/div/a[1]'
username = '//*[@id="__next"]/main/section/div/div/div/div/form/div/div[1]/div/input'
signinPassword = '//*[@id="__next"]/main/section/div/div/div/div/form/div/div[2]/div/input'
showSigninPassword = '//*[@id="__next"]/main/section/div/div/div/div/form/div/div[2]/div/button'
login = '//*[@id="__next"]/main/section/div/div/div/div/form/div/div[4]/button'
pesquisaProduto = "//input[@type='search']"
selecionaProduto = '//*[@id="products-show-case-category"]/div/div[3]/div[2]/a/div' 
addCarrinho = '//*[@id="__next"]/main/div/div[1]/div[1]/div/div[3]/ul/li[4]/div[1]/button'
carrinho = '//*[@id="__next"]/header/div[2]/div/div[3]/button[2]/span[1]'
fecharPedido = '//*[@id="fade-menu"]/div[3]/ul/li[3]/div[4]/div[1]'
entrega = '//*[@id="step-components"]/div/div[2]/div[1]/div/div/div[1]/label/span[1]/span[1]/input'
opcaoEnvio = '//*[@id="step-components"]/div/div[2]/div[2]/div/ul/li/div/label/span[1]/span[1]/input'
formaPagamento = '//*[@id="step-components"]/div/div/div/ul/li[2]/div/div[1]/div[2]'
numeroCartao = '//*[@id="step-components"]/div/div/div/ul/li[2]/div/div[2]/div/div/div/div/div/form/div/div[1]/div/div/div/input'
nomeTitular = '//*[@id="step-components"]/div/div/div/ul/li[2]/div/div[2]/div/div/div/div/div/form/div/div[2]/div/div/div/input'
dataValidade = '//*[@id="step-components"]/div/div/div/ul/li[2]/div/div[2]/div/div/div/div/div/form/div/div[3]/div/div[1]/div/div/div/input'
cvv = '//*[@id="step-components"]/div/div/div/ul/li[2]/div/div[2]/div/div/div/div/div/form/div/div[3]/div/div[2]/div/div/div/input'
parcelamento = '//*[@id="parcela"]'
valorParcelamento = '//*[@id="menu-"]/div[3]/ul/li[1]'
tela = '//*[@id="__next"]/main/section/div/div/div/div[2]/div[3]'
finalizarPagamento = '//*[@id="step-components"]/div/div/div/ul/li[2]/div/div[2]/div/div/div/div/div/div[3]/div/button/span[1]'

# Verifica Pedidos

signin = '//*[@id="__next"]/header/div[2]/div/div[3]/div/div/a[1]'
username = '//*[@id="__next"]/main/section/div/div/div/div/form/div/div[1]/div/input'
signinPassword = '//*[@id="__next"]/main/section/div/div/div/div/form/div/div[2]/div/input'
showSigninPassword = '//*[@id="__next"]/main/section/div/div/div/div/form/div/div[2]/div/button'
login = '//*[@id="__next"]/main/section/div/div/div/div/form/div/div[4]/button'
icon = '//*[@id="__next"]/header/div[2]/div/div[3]/button[1]'
meusPedidos = '/html/body/div[9]/div[3]/ul/li[2]'
ultimosPedidos = '//*[@id="__next"]/main/section/div[2]/div[1]/nav/div/div[2]/div[2]/div/div/div/div/ul/li[1]'
logout = '/html/body/div[7]/div[3]/ul/li[3]/div[2]/span'


# Caminhos Alteração de Dados

signin = '//*[@id="__next"]/header/div[2]/div/div[3]/div/div/a[1]'
username = '//*[@id="__next"]/main/section/div/div/div/div/form/div/div[1]/div/input'
signinPassword = '//*[@id="__next"]/main/section/div/div/div/div/form/div/div[2]/div/input'
showSigninPassword = '//*[@id="__next"]/main/section/div/div/div/div/form/div/div[2]/div/button'
login = '//*[@id="__next"]/main/section/div/div/div/div/form/div/div[4]/button'
icon = '//*[@id="__next"]/header/div[2]/div/div[3]/button[1]'
minhaConta = '/html/body/div[9]/div[3]/ul/li[1]/a'
meusDados = '//*[@id="__next"]/main/section/div[2]/div[1]/nav/div/div[3]/div[1]'
    # Telefones
listaTelefones = '//*[@id="__next"]/main/section/div[2]/div[1]/nav/div/div[3]/div[2]/div/div/div/div/ul/li[2]'
addTelefone = '//*[@id="my-account-data"]/section/div/h2/span/button'
ddd = '//*[@id="phone-ddd"]'
telefone = '//*[@id="phone-number"]'
tipoTelefone = '//*[@id="phone-type"]'
adicional = '//*[@id="menu-tipo"]/div[3]/ul/li[6]'
salvarTelefone = '//*[@id="my-account-data"]/section/div/ul/div[1]/form/div[2]/button[1]/span[1]'
excluirTelefone = '//*[@id="my-account-data"]/section/div/ul/div[2]/div/div[2]/button[2]/span[1]'
confirmarExclusaoTel = '/html/body/div[12]/div[3]/div/div[3]/button[1]/span[1]'
editarTelefone = '//*[@id="my-account-data"]/section/div/ul/div/div/div[2]/button[1]'
telefoneEdit = '//*[@id="phone-number"]'
salvarEdicaoTel = '//*[@id="my-account-data"]/section/div/ul/div/div/form/div[2]/button[1]'
    # Endereços
listaEnderecos = '//*[@id="__next"]/main/section/div[2]/div[1]/nav/div/div[3]/div[2]/div/div/div/div/ul/li[3]'
adicionarEndereco = '//*[@id="my-account-data"]/section/div/h2/span/button'
cep = '//*[@id="my-account-data"]/section/div/ul/div[1]/div/form/div/div[1]/div/input'
numero = '//*[@id="my-account-data"]/section/div/ul/div[1]/div/form/div/div[3]/div/div/div/div[3]/div[2]/div/div/input'
salvarEndereco = '//*[@id="my-account-data"]/section/div/ul/div[1]/div/form/div/div[3]/div/div/div/div[6]/button'
excluirEndereco = '//*[@id="my-account-data"]/section/div/ul/div[2]/div[2]/button[2]'
confirmarExclusaoEnd = '/html/body/div[12]/div[3]/div/div[3]/button[1]'
editarEndereco = '//*[@id="my-account-data"]/section/div/ul/div/div[2]/button[1]'
addComplemento = '//*[@id="my-account-data"]/section/div/ul/div/div/form/div/div[3]/div/div/div/div[3]/div[1]/div/div/input'
salvarEdicaoEnd = '//*[@id="my-account-data"]/section/div/ul/div/div/form/div/div[3]/div/div/div/div[6]/button'
editarEndereco = '//*[@id="my-account-data"]/section/div/ul/div/div[2]/button[1]'
removerComplemento = '//*[@id="my-account-data"]/section/div/ul/div/div/form/div/div[3]/div/div/div/div[3]/div[1]/div/div/input'
salvarEdicaoEnd = '//*[@id="my-account-data"]/section/div/ul/div/div/form/div/div[3]/div/div/div/div[6]/button'
    # Emails
listaEmails = '//*[@id="__next"]/main/section/div[2]/div[1]/nav/div/div[3]/div[2]/div/div/div/div/ul/li[4]'
adicionarEmail = '//*[@id="my-account-data"]/section/div/h2/span/button'
nomeEmail = '//*[@id="mail-name"]'
novoEmail = '//*[@id="mail-mail"]'
salvarEmail = '//*[@id="my-account-data"]/section/div/ul/div[1]/form/div[2]/button[1]'
excluirEmail = '//*[@id="my-account-data"]/section/div/ul/div[2]/div[2]/button[2]'
confirmarExclusaoEmail = '/html/body/div[12]/div[3]/div/div[3]/button[1]'
editarEmail = '//*[@id="my-account-data"]/section/div/ul/div/div[2]/button[1]'
campoEmail = '//*[@id="mail-mail"]'
salvarEdicaoEmail = '//*[@id="my-account-data"]/section/div/ul/div/form/div[2]/button[1]'
    # Alterar Senha
alterarSenha = '//*[@id="__next"]/main/section/div[2]/div[1]/nav/div/div[3]/div[2]/div/div/div/div/ul/li[5]'
senhaAtual = '//*[@id="person-password"]'
novaSenha = '//*[@id="person-newPassword"]'
confirmaNovaSenha = '//*[@id="person-newPasswordConfirmation"]'
salvarSenha = '//*[@id="my-account-data"]/form/section/div/div[5]/button'
dadosPessoais = '//*[@id="__next"]/main/section/div[2]/div[1]/nav/div/div[3]/div[2]/div/div/div/div/ul/li[1]'

# Esqueci minha senha
signin = '//*[@id="__next"]/header/div[2]/div/div[3]/div/div/a[1]'
esqueciSenha = '//*[@id="__next"]/main/section/div/div/div/div/form/div/div[3]/button'
emailRecuperacao = '/html/body/div[5]/div[3]/div/div[2]/div/div/form/div/div[2]/div/div/input'
recuperar = '/html/body/div[5]/div[3]/div/div[2]/div/div/form/div/div[4]/button'

