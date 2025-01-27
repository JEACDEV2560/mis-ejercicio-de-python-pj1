aprobados =0
reprobados =0

for f in range (10):
    notas = int(input("Ingrese la nota: "))
    if notas >= 7:
        aprobados = aprobados + 1
    else:
        reprobados = reprobados + 1

print("Cantidad de aprobados: ", aprobados)
print("Cantidad de reprobados: ", reprobados)