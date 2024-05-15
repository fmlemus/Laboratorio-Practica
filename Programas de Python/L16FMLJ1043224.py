import random
def LlenarVector(arreglo):
    for i in range(10):
        r=random.randint(1,100)
        vector.append(r)
    return arreglo
def Promedio(arreglo):
    sumatoria=0
    for valor in arreglo:
        sumatoria+=valor
    sumatoria=sumatoria/len(arreglo)
    return sumatoria
def ParesImpares(arreglo):
    sumapar=0
    sumaimpar=0
    for i in range(len(arreglo)):
        if i%2==0:
            sumapar+=arreglo[1]
        else:
            sumaimpar+=arreglo[1]
    print("La suma par es:",sumapar)
    print("La suma impar es:",sumaimpar)
def ContarParImpar(matriz):
    par=0
    impar=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]%2==0:
                par+=1
            else:
                impar+=1
    print("La cantidad de numeros pares es: ",par)
    print("La cantidad de numeros impares es: ",impar)
print("Semana 16: Ejercicio 1")
vector=[]
vector=LlenarVector(vector)
print(vector)
print("El promedio es:",Promedio(vector))
print("Longitud del arreglo:",len(vector))
ParesImpares(vector)
#Ejercicio 2
print("\nSemana 16: Ejercicio 2")
filas=int(input("Ingrese la cantidad de filas: "))
columnas=int(input("Ingrese la cantidad de columnas: "))
matriz=[]
even_count=[]
odd_count=[]
for i in range(filas):
        for j in range(columnas):
            temp=[]
            r=random.randint(0,1001)
            temp.append(r)
        matriz.append(temp)
        print(matriz)
        for row in matriz:
            for num in row:
             if num%2==0:
                even_count+=1
            else:
                odd_count+=1
            if num > max_num:
                max_num=num
            if num < min_num:
                min_num=num
print(f"Número mayor: {max_num}")
print(f"Número menor: {min_num}")
ContarParImpar(matriz)