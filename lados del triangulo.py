equil=0
isoceles=0
escal=0

n=int(input("Ingrese la cantidad de triangulos a procesar: "))

for f in range(n):
    lado1 = int(input("Ingrese el primer lado del triangulo: "))
    lado2 = int(input("Ingrese el segundo lado del triangulo: "))
    lado3 = int(input("Ingrese el tercer lado del triangulo: "))
    if lado1 == lado2 and lado2 == lado3:
        equil = equil + 1
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        isoceles = isoceles + 1
    else:
        escal = escal + 1

print("La cantidad de triangulos equilateros son: ", equil)
print("La cantidad de triangulos isoceles son: ", isoceles)
print("La cantidad de triangulos escalenos son: ", escal)