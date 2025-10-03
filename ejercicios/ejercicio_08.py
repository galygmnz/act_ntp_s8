import pandas as pd
import json
import os

def procesar_archivo_json():
   
    nombre_archivo = 'vehiculos.json'
    
    # 1.La estructura de datos
    datos_vehiculos = [
        {"marca": "Toyota", "modelo": "Corolla", "año": 2022},
        {"marca": "Ford", "modelo": "Mustang", "año": 2023},
        {"marca": "Tesla", "modelo": "Model 3", "año": 2024}
    ]

    # 2. Guardar la lista de diccionarios en un archivo JSON
    print(f"Creando y guardando el archivo '{nombre_archivo}'...")
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo_json:
        json.dump(datos_vehiculos, archivo_json, indent=4)
        
    print(f"Archivo '{nombre_archivo}' guardado con éxito.\n")
    print("="*50 + "\n")

    # 3. Leer JSON usando pandas.read_json()
    try:
        df_vehiculos = pd.read_json(nombre_archivo)
        
        # 4. Mostrar el DataFrame 
        print("DataFrame de Vehículos:")
        print(df_vehiculos)
        
        print("\n" + "="*50 + "\n")

        # 5. Mostrar los tipos de datos de las columnas
        print("Tipos de datos del DataFrame (df.dtypes):")
        print(df_vehiculos.dtypes)

        # Opcional: Eliminar el archivo para no dejar rastros
        os.remove(nombre_archivo)
        print(f"\nArchivo '{nombre_archivo}' eliminado.")

    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Llamar a la función para ejecutar el proceso
procesar_archivo_json()