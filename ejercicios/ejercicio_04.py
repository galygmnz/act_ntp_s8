import pandas as pd

def crear_dataframe_desde_diccionario():
    """
    Crea un DataFrame de Pandas a partir de un diccionario de datos
    de productos y realiza un análisis básico.
    """
    # 1. Crear un diccionario 
    datos_productos = {
        'Producto': ['Laptop', 'Smartphone', 'Tablet'],
        'Precio': [1200, 800, 450],
        'Categoria': ['Electrónica', 'Electrónica', 'Electrónica']
    }

    # 2. De diccionario a un DataFrame
    df_productos = pd.DataFrame(datos_productos)
    
    print("DataFrame de Productos:")
    print(df_productos)
    
    print("\n" + "="*50 + "\n")

    # 3. Acceder a una columna específica
    precios = df_productos['Precio']
    print("Columna 'Precio':")
    print(precios)

    print("\n" + "="*50 + "\n")
    
    # 4. Mostrar información básica del DataFrame
    print("Información del DataFrame (df.info()):")
    df_productos.info()


crear_dataframe_desde_diccionario()