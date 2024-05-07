#Calculo de años bisiestos entre 1900 y 2199 CON CICLOS
def es_bisiesto(año):
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        return True
    else:
        return False

def contar_bisiestos(año_inicio, año_final):
    contador = 0
    for año in range(año_inicio, año_final + 1):
        if es_bisiesto(año):
            contador += 1
    return contador

#Solicitar al usuario el año
año = int(input("Ingrese un año entre 1900 y 2199: "))

#Verificar si el año esta dentro del rango
if año < 1900 or año > 2199:
    print("El año debe estar entre 1900 y 2199.")
else:
#Calculo del número de años bisiestos hasta el año de entrada
    bisiestos_hasta_año = contar_bisiestos(1900, año)
    print(f"El número de años bisiestos entre 1900 y {año} es: {bisiestos_hasta_año}")
