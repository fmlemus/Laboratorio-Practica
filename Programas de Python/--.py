def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def imprimir_numeros_primos_en_rango(inicio, fin):
    primos = [str(num) for num in range(inicio, fin + 1) if es_primo(num)]
    print("Los números primos en el rango [", inicio, ", ", fin, "] son: ", ", ".join(primos))

respuesta = "Y"

while respuesta.upper() == "Y":
    inicio = int(input("Ingresa el inicio del rango: "))
    fin = int(input("Ingresa el fin del rango: "))
    
    imprimir_numeros_primos_en_rango(inicio, fin)
    
    respuesta = input("¿Deseas ingresar otro rango? (Y/N): ")

print("¡Hasta luego!")