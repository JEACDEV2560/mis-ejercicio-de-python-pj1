cantidad =0
n=int(input("Ingrese la cantidad de valores a ingresar: "))
for f in range (n):
    valor=int(input("Ingrese un valor: "))
    if valor >= 1000:
        cantidad = cantidad + 1
print("La cantidad de valores mayores o iguales a 1000 son: ", cantidad)

