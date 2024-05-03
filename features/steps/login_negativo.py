# 1 - Bibliotecas / Imports
import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By



@given(u'que entro no site Giuliana Flores')
def step_impl(context):
    # método de inicialização dos testes
    context.driver = webdriver.Chrome()            # instancia o objeto do Selenium WebDriver como Chrome
    context.driver.maximize_window()               # Maximizar a janela do navegador
    context.driver.implicitly_wait(15)             # define o tempo de esperar padrão por elementos em 10 segundos 
    # Passo em si 
    context.driver.get("https://www.giulianaflores.com.br") # abrir o navegador no endereço so site alvo 

@when(u'aperto no icone do perfil')
def step_impl(context):
    # clica no icone do perfil
    context.driver.find_element(By.XPATH, "//img[@alt='Icone Perfil']").click()   


@when(u'aperto no Login/Cadastrar')
def step_impl(context):
    # clica no login/cadastrar
    context.driver.find_element(By.XPATH, "//li[@id='UrlLogin']").click()
    


@when(u'digito meu usuario e senha')
def step_impl(context):
    # preencher email
    context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("nideu@yopmail.com")  
     # preencher senha
    context.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("123456")

@when(u'aperto no botão continuar')
def step_impl(context):
     # clica no botão continuar
    context.driver.find_element(By.ID, "ContentSite_ibtContinue").click()

@then(u'o acesso foi negado')
def step_impl(context):
    # Encontrando o elemento pelo XPath
    element = context.driver.find_element(By.XPATH, "//span[@class='font_erro']")
    # Validando o texto retornado
    texto = element.text
    assert texto == "e-mail ou senha inválidos!"
