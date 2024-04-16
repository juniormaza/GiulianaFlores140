# 1 - Bibliotecass
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2 - Clase (opcional)
class Teste_criar_usuario():

    # 2.1 Atributos
    url = "https://www.giulianaflores.com.br"

    # 2.2 Funções e Métodos 
    def setup_method(self, method):                 # método de inicialização dos testes
        self.driver = webdriver.Chrome()            # instancia o objeto do Selenium WebDriver como Chrome
        self.driver.maximize_window()       # Maximizar a janela do navegador
        self.driver.implicitly_wait(15)             # define o tempo de esperar padrão por elementos em 15 segundos 

    def teardown_method(self):              # método de finalização
        self.driver.quit()                  # encerra / destrói o objeto do Selenium WebDriver da memória 

    def test_criar_usuario(self):           # método de teste
        self.driver.get(self.url)           # abre o navegador

        # clica no icone do perfil
        self.driver.find_element(By.XPATH, "//img[@alt='Icone Perfil']").click()   
        # clica no login/cadastrar
        self.driver.find_element(By.XPATH, "//li[@id='UrlLogin']").click()
        # clica no criar cadastro
        self.driver.find_element(By.CSS_SELECTOR, "a#ContentSite_ibtNewCustomer").click()
        # validação de transição de tela por link 
        self.driver.find_element(By.XPATH, "//a[contains(@href, 'login.aspx')]")
        # preencher do nome
        self.driver.find_element(By.XPATH, "//input[@id='ContentSite_txtName']").send_keys("Orakun Junior")
        # preencher do cpf
        self.driver.find_element(By.XPATH, "//input[@id='ContentSite_txtCpf']").send_keys("557.460.940-13")
        # preencher do email
        self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("fts140@yopmail.com")
        # preencher de senha 
        self.driver.find_element(By.ID, "ContentSite_txtPasswordNew").send_keys("Orakun123456")
        # preencher cep
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").send_keys("85814-395")
        # Preencher numero 
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").send_keys("200")
        # preencher celular
        self.driver.find_element(By.CSS_SELECTOR, "#ContentSite_CustomerAddress_txtPhoneCelularNum").send_keys("11966665555")
        # clicar no botão finalizar cadastro
        self.driver.find_element(By.ID, "ContentSite_btnCreateCustomer").click()
