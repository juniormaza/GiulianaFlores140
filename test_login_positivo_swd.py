# 1 - Bibliotecass
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2 - Clase (opcional)
class Teste_usuario_positivo():

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
        # preencher email
        self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("fts140@yopmail.com")
        # preencher senha
        self.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("Orakun123456")
        # clica no botão continuar
        self.driver.find_element(By.ID, "ContentSite_ibtContinue").click