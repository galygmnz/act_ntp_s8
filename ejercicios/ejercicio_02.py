import pandas as pd

def crear_serie_calificaciones():
    # Crear la Serie con índices personalizados
    serie = pd.Series([85, 92, 78], index=['Matemáticas', 'Ciencias', 'Historia'])
    
    # Acceder a un valor específico por índice
    valor_ciencias = serie['Ciencias']
    print("Calificación en Ciencias:", valor_ciencias)
    
    # Mostrar información básica de la Serie
    print("\nSerie completa:")
    print(serie)
    
    print("\nÍndices:")
    print(serie.index)
    
    print("\nValores:")
    print(serie.values)
    
    # Calcular estadísticas básicas
    suma = serie.sum()
    promedio = serie.mean()
    
    print("\nSuma de calificaciones:", suma)
    print("Promedio de calificaciones:", promedio)

# Llamada a la función (puedes poner esto en otra celda o al final de tu script)
crear_serie_calificaciones()
