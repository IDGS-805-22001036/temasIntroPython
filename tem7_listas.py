#listas

'''
lista1=[10,5,3]
lista2=[1.5,2.66,1.70,89.2]
lista3=["Lunes","Martes","Miercoles"]
lista4=["Juan",45,1.92]

print(type(lista1))
print(len(lista1))

print(lista1[0]) 

x=0
suma=0
while x<len(lista1): 
    suma=suma+lista1[x]
    x=x+1

print("La suma es: {}".format(suma))
print(lista1)
print(lista1[0])
lista1.append(100)
print(lista1)
print(lista1[3])

#ingresar valores a una lista
lista5=[]
for x in range(5):
    valor=int(input("Ingresa valor:"))
    lista5.append(valor)
print(lista5)

#eliminar elementos de listas
print(lista1)
lista1.pop()
print(lista1)
'''
#Crear un programa pedir una cantidad de n numeros y 
#alacenarlos en un arreglo, la salida debera ser la siguiente:
#imprimir lista, numeros pares de la lista: aaaa, numeros impares de la lista: aaaa
lista6=[]
par=[]
impar=[]
valor=int(input("Ingresa valor de numeros a almacenar en la lista:"))
for x in range(valor):
    numero=int(input("Ingresa valor:"))
    lista6.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
print("La lista completa es: ",lista6)
print("Los numeros pares son: ",par)
print("Los numeros impares son: ",impar)


lista1.short()#ordenar lista
print(lista1)
lista1.reverse()
print(lista1)

lista1.remove(10)
print(lista1)#?

lista1.clear()
print(lista1)#?