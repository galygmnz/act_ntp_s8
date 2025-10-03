import pandas as pd
import csv
import os

def procesar_archivo_csv():

    nombre_archivo = 'cursos.csv'

    # 1. Crear el archivo CSV
    print(f"Creando el archivo '{nombre_archivo}'...")
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo_csv:
        writer = csv.writer(archivo_csv)
        # Escribir el encabezado
        writer.writerow(['curso', 'instructor', 'duracion'])
        # Escribir los datos
        writer.writerow(['Introducción a Python', 'Juan Pérez', '20 horas'])
        writer.writerow(['Análisis de Datos con Pandas', 'Ana Gómez', '30 horas'])
        writer.writerow(['Aprendizaje Automático', 'Carlos Ruiz', '45 horas'])

    print(f"Archivo '{nombre_archivo}' creado con éxito.\n")
    print("="*50 + "\n")

    # 2. Leer el archivo CSV usando pandas.read_csv()
    try:
        df_cursos = pd.read_csv(nombre_archivo)
        
        # 3. Mostrar el DataFrame resultante
        print("DataFrame de Cursos:")
        print(df_cursos)

        print("\n" + "="*50 + "\n")

        # Eliminar el archivo para la próxima ejecución de prueba
        os.remove(nombre_archivo)
        print(f"Archivo '{nombre_archivo}' eliminado.")

    # 4. Implementar manejo de errores (FileNotFoundError)
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró. Por favor, verifica la ruta.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Llamar a la función para ejecutar el proceso
procesar_archivo_csv()