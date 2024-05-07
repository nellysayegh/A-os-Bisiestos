#Calculo de años bisiestos entre 1900 y 2199 SIN CICLOS
def es_bisiesto(año):
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        return True
    else:
        return False

def contar_bisiestos(año_inicio, año_final):
    # Calculo número de años divisibles entre 4 desde el año_inicio = 1900 hasta el año_final = año 
    divisible_4 = (año_final // 4) - ((año_inicio - 1) // 4)

    # Calculo del número de años divisibles entre 100 desde el año_inicio = 1900 hasta el año_final = año 
    divisible_100 = (año_final // 100) - ((año_inicio - 1) // 100)

    # Calculo del número de años divisibles entre 400 desde el año_inicio = 1900 hasta el año_final = año 
    divisible_400 = (año_final // 400) - ((año_inicio - 1) // 400)

    # Calcular el número de años bisiestos
    bisiestos = divisible_4 - divisible_100 + divisible_400
    return bisiestos

# Solicitar al usuario el año
año = int(input("Ingrese un año entre 1900 y 2199: "))
if año < 1900 or año > 2199:
    print("El año debe estar entre 1900 y 2199.")
else:
    # Calculo del número de años bisiestos hasta el año de entrada
    bisiestos_hasta_año = contar_bisiestos(1900, año)
    print(f"El número de años bisiestos entre 1900 y {año} es: {bisiestos_hasta_año}")
