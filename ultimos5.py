sum =0

for f in range (10):
    valores = int(input("Ingrese un valor: "))
    if f >= 5:
        sum = sum + valores
print("La suma de los ultimos 5 valores ingresados es: ", sum)