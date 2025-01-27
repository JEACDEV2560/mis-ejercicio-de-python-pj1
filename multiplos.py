mult3=0
mult5=0
for f in range (10):
    valor = int(input("Ingrese un valor: "))
    if valor % 3 == 0:
        mult3 = mult3 + 1
    if valor % 5 == 0:
        mult5 = mult5 + 1
print("Cantidad de múltiplos de 3: ", mult3)
print("Cantidad de múltiplos de 5: ", mult5)
