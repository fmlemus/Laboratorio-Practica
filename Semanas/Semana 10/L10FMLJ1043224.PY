print("Semana No.10: Ejercicio 1")

mes=int(input("Ingrese un número entre 1 y 12:"))
if mes<1 or mes>12:
    print("Error: El número debe de estar entre 1 y 12")
else:
    if mes==1:
        print("mes: enero")
    elif mes==2:
        print("mes: febrero")
    elif mes==3:
        print("mes: marzo")
    elif mes==4:
        print("mes: april")
    elif mes==5:
        print("mes: mayo")
    elif mes==6:
        print("mes: junio")
    elif mes==7:
        print("mes:julio")
    elif mes==8:
        print("mes: agosto")
    elif mes==9:
        print("mes: septiembre")
    elif mes==10:
        print("mes: octubre")
    elif mes==11:
        print("mes: noviembre")
    elif mes==12:
        print("mes: diciembre")
print()

print("Semana No.10: Ejercicio 2")

A=int(input("Ingrese el primer número:"))
B=int(input("Ingrese el segundo número:"))
C=int(input("Ingrese el tercer número:"))

if A>B:
    if A>C:
        print("El numero mayor es:",A)
    else:
        if A==C:
            print("Los maores son:",A,"y",C)
        else:
            print("El mayor es:", C)
else:
 if A==B:
    if A>C:
        print("Los mayores son:",A,"y",B)
    else:
        if A==C:
            print("Los tres valores son iguales")
        else:
            print("El mayor es:",C)
else:
if B>C
     print("EL numero mayor es:",B)
else:
         if B==C
        print("Los mayores son:",B,"y",C)
        else:
            print("El mayor es:",C)
