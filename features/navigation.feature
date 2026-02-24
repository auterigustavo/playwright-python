Feature: Prueba UI demoqa

    @ui
    Scenario: Ingresar datos en un formulario
        Given Ingreso a la pagina https://demoqa.com/
        When Lleno los campos presentados
        And Hago click en submit
        Then Verifico que el mail gauteri@mail.com coincida
