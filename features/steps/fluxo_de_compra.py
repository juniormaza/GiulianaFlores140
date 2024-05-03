# 1 - Bibliotecas / Imports
import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'que acesso o site da Giuliana Flores')
def step_impl(context):
    # método de inicialização dos testes
    context.driver = webdriver.Chrome()            # instancia o objeto do Selenium WebDriver como Chrome
    context.driver.maximize_window()               # Maximizar a janela do navegador
    context.driver.implicitly_wait(15)             # define o tempo de esperar padrão por elementos em 15 segundos 
    # Passo em si 
    context.driver.get("https://www.giulianaflores.com.br") # abrir o navegador no endereço so site alvo 

   


@when(u'clico em um banner da pagina')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'img[alt="Imagem de A Rosa Encantada"]').click()
    


@when(u'clico em adicionar ao carrinho')
def step_impl(context):
    context.driver.find_element(By.ID, 'ContentSite_lbtBuy').click()
    


@when(u'insiro cep de entrega e clico em ok')
def step_impl(context):
   context.driver.find_element(By.ID, "ContentSite_uwcCalendar_txtZip").send_keys("69315-653")
   context.driver.find_element(By.CLASS_NAME, 'jSelectZip').click()
   context.driver.find_element(By.CSS_SELECTOR, 'input[type="radio"][name="periodRadio"][dslabel="Boa Vista"][idshippingmethod="1433753"]').click()
   context.driver.find_element(By.CSS_SELECTOR, 'span.btOk.jConfirmShippingData').click()


@then(u'clico em adicionar ao carrinho')
def step_impl(context):
     context.driver.find_element(By.CSS_SELECTOR, 'a#ContentSite_lbtBuy').click()


@given(u'que estou no carrinho de compra')
def step_impl(context):
    # Localize o elemento span
    element = context.driver.find_element(By.XPATH, "//span")
    # Obtenha o texto do elemento
    element_text = element.text
    # Compare o texto obtido com o texto esperado
    assert element_text == "Carrinho"



@when(u'valido nome do produto')
def step_impl(context):
    element = context.driver.find_element(By.XPATH, "//img[@alt='A Rosa Encantada']")
    assert element.get_attribute("alt") == "A Rosa Encantada"



@when(u'valido quantidade de produto')
def step_impl(context):
   element = context.driver.find_element(By.NAME, 'ctl00$ContentSite$Basketcontrol1$rptBasket$ctl00$rptBasketItems$ctl01$nuQty')
   assert element.get_attribute("value") == "1"



@when(u'valido preco do produto')
def step_impl(context):
    # Obter o elemento
    element = context.driver.find_element(By.XPATH, "//span[@class='valor-total-carrinho']")

    #   Obter o texto do elemento
    element_text = element.get_attribute("textContent").strip()

    # Verificar se o texto do elemento corresponde ao esperado
    assert element_text == "R$ 339,90"




@then(u'clico em excluir produto do carrinho')
def step_impl(context):
   context.driver.find_element(By.ID, 'ContentSite_Basketcontrol1_rptBasket_rptBasketItems_0_lbtRemoveProduct_0').click()
