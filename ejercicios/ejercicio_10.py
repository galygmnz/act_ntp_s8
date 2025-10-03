import pandas as pd
import requests

def consumir_api_y_crear_dataframe():
 
    url = 'https://playground.mockoon.com/users'
    
    print(f"Realizando petición GET a la URL: {url}\n")
    
    try:
        # 1.Petición GET
        response = requests.get(url)
        
        # 2. Verificar que el código de estado sea 200
        response.raise_for_status()  # Esto lanzará una excepción para códigos de error HTTP
        
        # 3. Convertir la respuesta JSON a DataFrame
        datos_json = response.json()
        df_usuarios = pd.DataFrame(datos_json)
        
        print("Petición exitosa. DataFrame creado.\n")
        print("="*50 + "\n")
        
        # 4. Mostrar las primeras 5 filas
        print("Primeras 5 filas del DataFrame (df.head()):")
        print(df_usuarios.head())
        
        print("\n" + "="*50 + "\n")
        
        
        print("Información del DataFrame (df.info()):")
        df_usuarios.info()

   
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error de Conexión: No se pudo conectar a la URL. {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Error de Tiempo de Espera: La petición ha expirado. {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Ocurrió un error inesperado al realizar la petición: {req_err}")
    except json.JSONDecodeError:
        print("Error: La respuesta de la API no es un JSON válido.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


consumir_api_y_crear_dataframe()