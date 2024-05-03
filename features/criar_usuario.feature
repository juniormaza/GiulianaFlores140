Feature: Criar Usuario

    Scenario: Criar conta no site "Giuliana Flores"
    Given que acesso o site Giuliana Flores
    When clico no icone perfil
    And clico em Login/Cadastrar
    And clico em Criar cadastro
    Then sou direcionado para a pagina Meu cadastro

    Given que estou na pagina Meu cadastro
    When insiro nome completo
    And insiro CPF
    And insiro Email
    And insiro senha 
    And insiro CEP
    And insiro Numero
    And insiro Celular
    Then clico em Finalizar Cadastro


    