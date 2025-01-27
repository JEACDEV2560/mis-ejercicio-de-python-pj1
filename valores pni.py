negativos=0
positivos=0
multi15=0
suma_pares =0
for f in range (10):
    valores = int(input("Ingrese un valor: "))
    if valores < 0:
        negativos = negativos + 1
    else:
        positivos = positivos + 1
    if valores % 15 == 0:
        multi15 = multi15 + 1
    if valores % 2 == 0:
        suma_pares = suma_pares + valores


print("La cantidad de valores negativos son: ", negativos)
print("La cantidad de valores positivos son: ", positivos)
print("La cantidad de valores multiplos de 15 son: ", multi15)
print("La suma de los valores pares es: ", suma_pares)
