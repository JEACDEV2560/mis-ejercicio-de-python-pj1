cantidad1=0
cantidad2=0
cantidad3=0
cantidad4=0

n=int(input("Ingrese la cantidad de puntos a procesar: "))

for fa in range(n):
    x= int(input("Ingrese la coordenada x: "))
    y= int(input("Ingrese la coordenada y: "))
    if x > 0 and y > 0:
        cantidad1 = cantidad1 + 1
    elif x < 0 and y > 0:
        cantidad2 = cantidad2 + 1
    elif x < 0 and y < 0:
        cantidad3 = cantidad3 + 1
    else:
        cantidad4 = cantidad4 + 1

print("La cantidad de puntos en el primer cuadrante son: ", cantidad1)
print("La cantidad de puntos en el segundo cuadrante son: ", cantidad2)
print("La cantidad de puntos en el tercer cuadrante son: ", cantidad3)
print("La cantidad de puntos en el cuarto cuadrante son: ", cantidad4)