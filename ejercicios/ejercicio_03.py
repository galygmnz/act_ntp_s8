import pandas as pd

def operaciones_matematicas_con_series():
   
    # 1. Crear las dos Series
    precios = pd.Series([100, 150, 200], name="Precios")
    descuentos = pd.Series([10, 20, 15], name="Descuentos")
    
    print("Serie de Precios:")
    print(precios)
    print("\nSerie de Descuentos:")
    print(descuentos)
    
    print("-" * 40)

    # 2. Resta entre precios y descuentos 
    precios_con_descuento = precios - descuentos
    print("Precios después de aplicar los descuentos (precios - descuentos):")
    print(precios_con_descuento)
    
    print("-" * 40)

    # 3. Multiplicar la Serie de precios por un escalar (precios * 1.16 para IVA)
    precios_con_iva = precios * 1.16
    print("Precios con IVA (precios * 1.16):")
    print(precios_con_iva)

    print("-" * 40)
    
    # 4. Demostración de las operaciones 
    print("Demostración de la operación elemento por elemento:")
    print("El primer elemento de 'precios' (100) menos el primer elemento de 'descuentos' (10) es:", precios[0] - descuentos[0])
    print("El segundo elemento de 'precios' (150) menos el segundo elemento de 'descuentos' (20) es:", precios[1] - descuentos[1])
    print("El tercer elemento de 'precios' (200) menos el tercer elemento de 'descuentos' (15) es:", precios[2] - descuentos[2])
    print("\nComo se puede ver, las operaciones se aplican a cada par de elementos correspondientes en las Series, sin importar sus índices.")

# ejecutar el análisis
operaciones_matematicas_con_series()