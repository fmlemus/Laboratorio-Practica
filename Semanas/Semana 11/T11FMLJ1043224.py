print("Semana No.11 Fátima Lémus - 1043224")

N=0
while N<=0:
    N=int(input("Ingrese un número mayor que 0:"))
    A=int(input("Ingrese un número mayor que 0:"))
    B=int(input("Ingrese un número mayor que 0:"))
    if N<=0:
        print("El número debe de ser mayor a que 0:")
        print()

CalculoA=0
a=int(0)
c=0
for i in range(N):
        a += 1
        c1 = 1/a
        c2 = c + c1
     print(c2)

CalculoB=0
a = int(0)
c = 0
for i in range(N):
        a+=1
        c1 = 1/(2**a)
        c = c + c1
    print(CalculoB)

CalculoC=0
a = int(0)
c = 1
k = 1 
    
for i in range(N):
        a +=1
        c1 = (B*a)(A**(a-k)/N)
        k += 1
        c = c + c1
    print(CalculoC)

if n <= 0:
    print("Ingrese un numero valido, tiene que ser mayor a 0")
else:
    CalculoA(N)
    CalculoB(N)
    CalculoC(N)
