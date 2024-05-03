Feature: Fluxo de Compra

    Scenario: Fluxo de compra no site "Giuliana Flores"
    Given que acesso o site da Giuliana Flores
    When clico em um banner da pagina
    And clico em adicionar ao carrinho 
    And insiro cep de entrega e clico em ok
    Then clico em adicionar ao carrinho 

    Given que estou no carrinho de compra
    When valido nome do produto
    And valido quantidade de produto 
    And valido preco do produto 
    Then clico em excluir produto do carrinho


     
