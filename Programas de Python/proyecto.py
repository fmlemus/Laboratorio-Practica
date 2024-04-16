import turtle 
import time

def dibujar_rectangulo(lado1, lado2, color): 
    t = turtle.Turtle() 
    t.fillcolor(color) 
    t.begin_fill()
    for _ in range(2): 
        t.forward(lado1) 
        t.right(90) 
        t.forward(lado2) 
        t.right(90)

def dibujar_triangulo(lado, color): 
    t = turtle.Turtle() 
    t.fillcolor(color) 
    t.begin_fill()
    t.forward(lado) 
    t.right(120) 
    t.forward(lado) 
    t.right(120) 
    t.forward(lado)
    t.end_fill()
    t.end_fill()

def dibujar_circulo(radio, color): 
    t = turtle.Turtle() 
    t.penup() 
    t.fillcolor(color) 
    t.begin_fill() 
    t.circle(radio) 
    t.end_fill()

def dibujar_hexagono(lado, color): 
    t = turtle.Turtle() 
    t.penup() 
    t.fillcolor(color)
    t.begin_fill()

    for _ in range(6): 
        t.forward(lado) 
        t.right(60)
        t.end_fill()

nombre = input("Por favor, ingresa tu nombre: ") 
edad = int(input("Ingresa tu edad: ")) 
colores = ["red", "blue", "green", "yellow", "purple"] 
color_favorito = input("Elige un color favorito entre los siguientes: " + ", ".
                       join(colores) + ": ").lower() 
def mostrar_datos_y_menu(): 
    print("Bienvenido(a)")
print("\nSelecciona una secuencia del cuento:") 
print("1. Secuencia 1") 
print("2. Secuencia 2") 
print("3. Secuencia 3") 
print("4. Secuencia 4") 
print("5. Secuencia 5") 
print("6. Salir")


def dibujar_panel(secuencia):
    turtle.clearscreen() 
    turtle.reset()
    dibujar_rectangulo(300, 200, "white")
    dibujar_rectangulo(270, 30, "black")
    turtle.write("Secuencia " + str(secuencia), font=("Arial", 14, "normal"))
    if secuencia == 1: 
        dibujar_rectangulo(250, 80, "white") 
            turtle.write("Había una vez un pequeño que se llamaba " + nombre +"y tenia"+ edad + ". \nÉl siempre soñaba con conocer el mundo y aprender cosas nuevas.", font=("Arial", 8, "normal")) O:
    if secuencia == 2: 
        dibujar_rectangulo(250, 80, "white") 
    turtle.write("Había una vez un pequeño " + color_favorito + " que se llamaba " + nombre + ". \nÉl siempre soñaba con conocer el mundo y aprender cosas nuevas.", font=("Arial", 8, "normal")) O:
    while color_favorito not in colores: 
    color_favorito = input("Elige un color favorito válido entre los siguientes: " + ", "
                           .join(colores) + ": ").lower()
    while True: mostrar_datos_y_menu() 
secuencia = int(input("Elige una secuencia (1-5) o 6 para salir: ")) 
        if secuencia == 1: dibujar_panel(secuencia) O:
         elif secuencia == 6: 

            dibujar_triangulo(70, color_favorito) 
            dibujar_circulo(30, "red") 
            dibujar_hexagono(40, "blue")
            time.sleep(5)
    
break else: print("Opción inválida, inténtalo de nuevo.")
turtle.done()

