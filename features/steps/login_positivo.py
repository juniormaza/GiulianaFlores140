# 1 - Bibliotecas / Imports
import time
import re
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By



@given(u'que estou no site Giuliana Flores')
def step_impl(context):
        # método de inicialização dos testes
        context.driver = webdriver.Chrome()            # instancia o objeto do Selenium WebDriver como Chrome
        context.driver.maximize_window()               # Maximizar a janela do navegador
        context.driver.implicitly_wait(15)             # define o tempo de esperar padrão por elementos em 10 segundos 
        # Passo em si 
        context.driver.get("https://www.giulianaflores.com.br") # abrir o navegador no endereço so site alvo 

@when(u'clico no icone do perfil')
def step_impl(context):
    # clica no icone do perfil
    context.driver.find_element(By.XPATH, "//img[@alt='Icone Perfil']").click()   


@when(u'clico no Login/Cadastrar')
def step_impl(context):
    # clica no login/cadastrar
    context.driver.find_element(By.XPATH, "//li[@id='UrlLogin']").click()
    


@when(u'insiro meu usuario e senha')
def step_impl(context):
    # preencher email
    context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("nideu@yopmail.com")  
     # preencher senha
    context.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("Nideu123456")

@when(u'clico no botão continuar')
def step_impl(context):
     # clica no botão continuar
    context.driver.find_element(By.ID, "ContentSite_ibtContinue").click()
     

@then(u'o acesso foi realizado com sucesso')
def step_impl(context):
   # Clica no ícone do perfil
    context.driver.find_element(By.CSS_SELECTOR, 'img[alt="Icone Perfil"]').click()
    # Validando o nome do perfil
    welcome_text = context.driver.find_element(By.ID, 'lblWelcome').text
    assert re.search(r"(Bom Dia|Boa Tarde|Boa Noite), Nideu!", welcome_text) is not None
    # Teardown / Encerramento 
    context.driver.quit()
