import math
#Permitir calcular la distancia entre dos puntos
#Los puntos se van a pedir 
x1=int(input("Ingresa el numero de la cordenada x1: "))
x2=int(input("Ingresa el numero de la cordenada x2: "))
y1=int(input("Ingresa el numero de la cordenada y1: "))
y2=int(input("Ingresa el numero de la cordenada y2: "))
distancia= math.sqrt((x2-x1)^2 + (y2-y1)^2)
print("La distancia es: {}".format(distancia))