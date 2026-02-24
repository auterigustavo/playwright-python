import os

# Se congura variables por defecto. Pueden ser variables de entorno o en caso contrario se especifica una
# Por el momento solo se esta utilizando API_BASE_URL
# Debo modificar el codigo para que se trabaje con las variables en todos los features files en lugar de especificarla en los steps
BASE_URL = os.getenv("BASE_URL", "https://demoqa.com")
API_BASE_URL = os.getenv("API_BASE_URL", "https://demoqa.com")