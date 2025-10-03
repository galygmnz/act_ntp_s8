import pandas as pd
import numpy as np

def crear_dataframe_desde_array_numpy():
    
    # 1. Array de NumPy 2D
    # Cada fila representa un año, y cada columna un trimestre 
    ventas_trimestrales = np.array([
        [1500, 1800, 2200],  # Ventas del Año 1
        [1600, 1950, 2400],  # Ventas del Año 2
        [1700, 2100, 2550]   # Ventas del Año 3
    ])
    
    # 2.Nombres de las columnas
    nombres_columnas = ['Q1', 'Q2', 'Q3']

    # 3. Crear el DataFrame a partir del array de NumPy
    df_ventas = pd.DataFrame(ventas_trimestrales, columns=nombres_columnas)
    
    print("DataFrame de Ventas Trimestrales:")
    print(df_ventas)
    
    print("\n" + "="*50 + "\n")

    # 4. Verificar los tipos de datos del DataFrame
    print("Tipos de datos del DataFrame (df.dtypes):")
    print(df_ventas.dtypes)

# Llamar a la función para ejecutar el proceso
crear_dataframe_desde_array_numpy()