print("Ejercicio 1: Operaciones aritmeticas")
#Captura de datos
n1=int(input("Ingrese un número "))
n2=int(input("Ingrese otro número "))

#Operaciones a realizar:
total=n1+n2
diferencia=n1-n2
producto=n1*n2
cocientereal=n1/n2
cocienteenntero=n1//n2
residuo=n1%n2
potencia=n1**n2
#print("suma:",total)
print(n1,"+",n2,"=",total)
print(n1,"-",n2,"=",diferencia)
print(n1,"*",n2,"=",producto)
print(n1,"/",n2,"=",cocientereal)
print(n1,"//",n2,"=",cocienteenntero)
print(n1,"%",n2,"=",residuo)
print(n1,"^",n2,"=",potencia)
print()
print("Ejercicio 2: operaciones booleanas")
igualdad=n1==n2
mayorque=n1>n2
menorque=n1<n2
distinto=n1!=n2

print(n1,"es igual a",n2,"=",igualdad)
print(n1,"es mayor a",n2,"=",mayorque)
print(n1,"es menor a",n2,"=",menorque)
print(n1,"es igual a ",n2,"=",distinto)

print()
print("Ejercicio 3: jerarquía de operadores")
a=int(input("Ingrese el primer número: "))
b=int(input("Ingrese el primer número: "))
c=int(input("Ingrese el primer número: "))

i=a*b+c
ii=a*(b+c)
iii=a/(b+c)
iv=((3*a)+(2*b))/(c**2)

print("a*b+c=", i)
print("a(b+c)=", ii)
print("a/(b+c)=", iii)
print("((3*a)+(2*b))/(c**2)=", iv)
