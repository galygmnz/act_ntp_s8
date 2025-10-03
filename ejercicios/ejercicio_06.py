import pandas as pd

def crear_dataframe_desde_lista_de_listas():
   
    # 1. Listas con los datos de los libros
    datos_libros = [
        ['Cien años de soledad', 'Gabriel García Márquez', 1967],
        ['El Quijote', 'Miguel de Cervantes', 1605],
        ['1984', 'George Orwell', 1949]
    ]

    # 2. Nombres de las columnas
    nombres_columnas = ['Titulo', 'Autor', 'Año']

    # 3. Crear el DataFrame, pasando tanto los datos como los nombres de las columnas
    df_libros = pd.DataFrame(datos_libros, columns=nombres_columnas)
    
    print("DataFrame de Libros:")
    print(df_libros)
    
    print("\n" + "="*50 + "\n")

    # 4. Mostrar las dimensiones del DataFrame
    print(f"Dimensiones del DataFrame (filas, columnas): {df_libros.shape}")
    print(f"El DataFrame tiene {df_libros.shape[0]} filas y {df_libros.shape[1]} columnas.")

# Llamar a la función para ejecutar el proceso
crear_dataframe_desde_lista_de_listas()