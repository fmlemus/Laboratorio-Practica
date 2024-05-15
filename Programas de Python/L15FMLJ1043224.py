import math

def obtener_area_triangulo(base, altura):
    return (base * altura) / 2

def obtener_area_cuadrado(lado):
    return lado ** 2

def obtener_area_rectangulo(base, altura):
    return base * altura

def obtener_area_circulo(radio):
    return math.pi * (radio ** 2)

print("Semana No. 12: Ejercicio 1")

while True:
    print("Menú:")
    print("a. Área de triángulo")
    print("b. Área de cuadrado")
    print("c. Área de rectángulo")
    print("d. Área de círculo")
    opcion = input("Ingrese la opción deseada: ")

    if opcion == "a":
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = obtener_area_triangulo(base, altura)
        print(f"El área del triángulo es: {area:.2f}")
    elif opcion == "b":
        lado = float(input("Ingrese el lado del cuadrado: "))
        area = obtener_area_cuadrado(lado)
        print(f"El área del cuadrado es: {area:.2f}")
    elif opcion == "c":
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = obtener_area_rectangulo(base, altura)
        print(f"El área del rectángulo es: {area:.2f}")
    elif opcion == "d":
        radio = float(input("Ingrese el radio del círculo: "))
        area = obtener_area_circulo(radio)
        print(f"El área del círculo es: {area:.2f}")
    else:
        print("Opción inválida. Intente nuevamente.")

#Ejercicio 2
# Coordenadas globales
    X = 0
    Y = 0
    print("Semana No. 12: Ejercicio 2")
# Funciones para mover el objeto
    def MoverHaciaArriba():
        global Y
    Y+=1

    def MoverHaciaAbajo():
        global Y
    Y-=1

    def MoverHaciaLaDerecha():
        global X
    X+=1

    def MoverHaciaLaIzquierda():
        global X
    X-=1

    def mostrar_menu():
        print("a. Sube")
        print("b. Baja")
        print("c. Izquierda")
        print("d. Derecha")
        print("e. Salir")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (a, b, c, d, e): ")

        if opcion == "a":
            MoverHaciaArriba()
        elif opcion == "b":
            MoverHaciaAbajo()
        elif opcion == "c":
            MoverHaciaLaIzquierda()
        elif opcion == "d":
            MoverHaciaLaDerecha()
        elif opcion == "e":
            print("Coordenadas finales del personaje:", X, ",", Y)
            break
        else:
            print("Opción no válida")


