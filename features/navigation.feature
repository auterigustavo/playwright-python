Feature: Automatizacion carrefour

    @listadeprecios
    Scenario: Obtener lista de precios
        Given Ingreso a la pagina https://www.carrefour.com.ar/
        When Busco los siguientes productos y obtengo los precios:
            | Producto                           |
            | yerba union suave 1kg              |
            | harina integral pureza 1 kg        |
            | jabon dove                         |
            | arvejas                            |
            | te taragui x25                     |
            | Queso cremoso horma x kg          |
            | mayonesa hellmann's 475            |
            | arroz integral ala 1kg             |
            | lomitos de atun carrefour          |
        And Genero un reporte con los datos
        Then Envio un reporte por mail
