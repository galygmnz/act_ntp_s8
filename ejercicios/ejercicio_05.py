import pandas as pd

def crear_dataframe_desde_lista_de_diccionarios():
    
    # 1. Crear una lista de diccionarios, cada uno para un empleado
    lista_empleados = [
        {'empleado': 'Ana García', 'salario': 55000, 'departamento': 'Marketing'},
        {'empleado': 'Luis Pérez', 'salario': 72000, 'departamento': 'Ventas'},
        {'empleado': 'Sofía Rojas', 'salario': 60000, 'departamento': 'Recursos Humanos'},
        {'empleado': 'Pedro Gómez', 'salario': 95000, 'departamento': 'Ingeniería'}
    ]

    # 2. De lista de diccionarios a un DataFrame
    df_empleados = pd.DataFrame(lista_empleados)
    
    print("DataFrame de Empleados:")
    print(df_empleados)
    
    print("\n" + "="*50 + "\n")

    # 3. Acceder a filas específicas usando índices
    # Acceder a la primera fila (índice 0)
    primer_empleado = df_empleados.iloc[0]
    print("Datos del primer empleado (índice 0):")
    print(primer_empleado)
    
    print("\n" + "-"*30 + "\n")

    # Acceder a índices 1 y 2
    empleados_selectos = df_empleados.iloc[1:3]
    print("Datos de los empleados en los índices 1 y 2:")
    print(empleados_selectos)
    
    print("\n" + "="*50 + "\n")

    # Acceder a una fila por su nombre o índice
    # Aquí accedemos por la posición 2, que es la fila del empleado 'Sofía Rojas'
    tercer_empleado = df_empleados.loc[2]
    print("Datos del tercer empleado (índice 2) usando .loc:")
    print(tercer_empleado)
    
# ejecutar el proceso
crear_dataframe_desde_lista_de_diccionarios()