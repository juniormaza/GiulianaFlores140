Feature: Login Postivo

    Scenario: Login Posito no site "Giuliana Flores"
    Given que estou no site Giuliana Flores
    When clico no icone do perfil
    And clico no Login/Cadastrar
    And insiro meu usuario e senha 
    And clico no botão continuar
    Then o acesso foi realizado com sucesso


    Scenario: Login Negativo no site "Giuliana Flores"
    Given que entro no site Giuliana Flores
    When aperto no icone do perfil
    And aperto no Login/Cadastrar
    And digito meu usuario e senha 
    And aperto no botão continuar
    Then o acesso foi negado