import pandas as pd

def analizar_ventas_diarias():

    ventas = pd.Series([150, 200, 180, 220, 175, 190, 165])

    valor_indice_3 = ventas[3]

   
    promedio = ventas.mean()
    ventas_ordenadas = ventas.sort_values()

    print("Ventas diarias:", ventas.tolist())
    print("Valor en índice 3:", valor_indice_3)
    print("Promedio de ventas:", promedio)
    print("Ventas ordenadas:", ventas_ordenadas.tolist())
    
analizar_ventas_diarias()
