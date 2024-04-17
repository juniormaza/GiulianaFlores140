# 1 - Bibliotecass
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2 - Clase (opcional)
class Teste_realizar_compra():

    # 2.1 Atributos
    url = "https://www.giulianaflores.com.br"

    # 2.2 Funções e Métodos 
    def setup_method(self, method):                 # método de inicialização dos testes
        self.driver = webdriver.Chrome()            # instancia o objeto do Selenium WebDriver como Chrome
        self.driver.maximize_window()       # Maximizar a janela do navegador
        self.driver.implicitly_wait(20)             # define o tempo de esperar padrão por elementos em 15 segundos 

    def teardown_method(self):              # método de finalização
         self.driver.quit()                 # encerra / destrói o objeto do Selenium WebDriver da memória '''

    def test_criar_usuario(self):           # método de teste
        self.driver.get(self.url)           # abre o navegador

        # clicla no banner coleção de rosas
        self.driver.find_element(By.XPATH, "//img[@class='img_banner']").click
        # clica no buscar endereço
        self.driver.find_element(By.XPATH, "//img[@alt='Busca endereco']").click()
        # inserir o cep 
        self.driver.find_element(By.ID, "inputSearchAddress").send_keys("85814-395")
        # clica em aplicar
        self.driver.find_element(By.XPATH, "//div[contains(text(),'Aplicar')]").click()
        # clica no endereço
        self.driver.find_element(By.XPATH, "//li[contains(text(), 'Rua Aristóteles, Interlagos, Cascavel - PR, 85814-395, Brasil')]").click
        # procura por produto
        self.driver.find_element(By.ID, "txtDsKeyWord").send_keys("Cesta Paixão Por Chocolates")
        # clica na lupa
        self.driver.find_element(By.ID, "btnSearch").click()
        # fecha a aba de cep
        self.driver.find_element(By.XPATH, "//div[contains(text(),'✖')]").click()
        # clica no produto
        self.driver.find_element(By.XPATH, "//img[@alt= 'Cesta Paixão Por Chocolates']").click()
        # valida o nome
        assert self.driver.find_element(By.ID, "ContentSite_lblProductDsName").text == ("CESTA PAIXÃO POR CHOCOLATES")
        # valida o preço
        assert self.driver.find_element(By.CLASS_NAME, "precoPor_prod").text == ("R$ 147,90")
        # inserir cep
        self.driver.find_element(By.ID, "ContentSite_txtZip").send_keys("85814395")
        # clicar em ok
        #self.driver.find_element(By.CSS_SELECTOR, "btn_okcep").click()
        # clica no botão adicionar ao carrinho 
        self.driver.find_element(By.ID, "ContentSite_lbtBuy").click()
        #self.driver.find_element(By.CSS_SELECTOR, "btOk jConfirmShippingData").click()