Feature: API test

  @api
  Scenario: Obtener libro por ISBN
    Given Llamo al endpoint /BookStore/v1/Book?ISBN=9781449325862
    Then El status code debe ser 200
