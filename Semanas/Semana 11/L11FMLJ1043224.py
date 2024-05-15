print("Semana No.11: Ejercicio 1")

N=0
while N<=0:
    N=int(input("Ingrese un número mayor que 0:"))
    if N<=0:
        print("El número debe de ser mayor a que 0:")
        print()
A=0
B=1
C=0
i=2
resultados=""
resultado=str(A)
if N>1:
    resultado+=(","+str(B))
    while i<N:
        C=A+B
        resultado+=(","+str(C))
        A=B
        B=C
        i=i+1
        print(resultado)
else:
    print(resultado)

    