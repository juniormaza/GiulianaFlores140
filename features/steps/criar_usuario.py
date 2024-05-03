# 1 - Bibliotecas / Imports
import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'que acesso o site Giuliana Flores')
def step_impl(context):
        # método de inicialização dos testes
        context.driver = webdriver.Chrome()            # instancia o objeto do Selenium WebDriver como Chrome
        context.driver.maximize_window()               # Maximizar a janela do navegador
        context.driver.implicitly_wait(10)             # define o tempo de esperar padrão por elementos em 10 segundos 
        # Passo em si 
        context.driver.get("https://www.giulianaflores.com.br") # abrir o navegador no endereço so site alvo 


@when(u'clico no icone perfil')
def step_impl(context):
   # clica no icone do perfil
    context.driver.find_element(By.XPATH, "//img[@alt='Icone Perfil']").click()   

@when(u'clico em Login/Cadastrar')
def step_impl(context):
    # clica no login/cadastrar
    context.driver.find_element(By.XPATH, "//li[@id='UrlLogin']").click()
   
@when(u'clico em Criar cadastro')
def step_impl(context):
 # clica no criar cadastro
    context.driver.find_element(By.CSS_SELECTOR, "a#ContentSite_ibtNewCustomer").click()  

@then(u'sou direcionado para a pagina Meu cadastro')
def step_impl(context):
# validação de transição de tela por link 
    context.driver.find_element(By.XPATH, "//a[contains(@href, 'login.aspx')]")

@given(u'que estou na pagina Meu cadastro')
def step_impl(context):
     # validação de transição de tela por link 
    context.driver.find_element(By.XPATH, "//a[contains(@href, 'login.aspx')]")

@when(u'insiro nome completo')
def step_impl(context):
 # preencher do nome
    context.driver.find_element(By.XPATH, "//input[@id='ContentSite_txtName']").send_keys("Nideu Junior") 

@when(u'insiro CPF')
def step_impl(context):
 # preencher do cpf
    context.driver.find_element(By.XPATH, "//input[@id='ContentSite_txtCpf']").send_keys("571.621.750-82")

@when(u'insiro Email')
def step_impl(context):
    
 # preencher do email
    context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("nideu@yopmail.com")

@when(u'insiro senha')
def step_impl(context):
    # preencher de senha 
    context.driver.find_element(By.ID, "ContentSite_txtPasswordNew").send_keys("Nideu123456")

@when(u'insiro CEP')
def step_impl(context):
     # preencher cep
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").send_keys("69315-653")

@when(u'insiro Numero')
def step_impl(context):
     # Preencher numero 
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").send_keys("200")

@when(u'insiro Celular')
def step_impl(context):
    # preencher celular
    context.driver.find_element(By.CSS_SELECTOR, "#ContentSite_CustomerAddress_txtPhoneCelularNum").send_keys("11966665555")

@then(u'clico em Finalizar Cadastro')
def step_impl(context):
    # clicar no botão finalizar cadastro
    context.driver.find_element(By.ID, "ContentSite_btnCreateCustomer").click()
     # teardown / encerramento
    context.driver.quit()