n=int(input("Ingrese la cantidad de triangulos a procesar: "))
cantidad=0
for f in range (n):
    base = int(input("Ingrese la base del triangulo: "))
    altura = int(input("Ingrese la altura del triangulo: "))
    superficie = base * altura / 2
    print("La superficie del triangulo es: ", superficie)
    if superficie > 12:
        cantidad = cantidad + 1
print("La cantidad de triangulos con superficie mayor a 12 son: ", cantidad)