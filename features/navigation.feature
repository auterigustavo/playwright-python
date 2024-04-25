Feature: Automatizacion carrefour

    @demi
    Scenario: Obtener lista de precios
        Given Ingreso a la pagina https://www.carrefour.com.ar/
        When Busco el producto yerba union suave 1kg y obtengo el precio
        And Busco el producto harina integral pureza 1 kg y obtengo el precio
        And Busco el producto jabon dove y obtengo el precio
        And Busco el producto arvejas y obtengo el precio
        And Genero un reporte con los datos
        Then Guardo el trace en la carpeta logs