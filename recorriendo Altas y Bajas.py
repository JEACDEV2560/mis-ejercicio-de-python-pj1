altas = 0
bajas =0
x=1

while x <=10:
    nota= int(input("introduce la nota: "))
    if nota >=7:
        altas = altas+1
    else:
        bajas= bajas+1
    x=x+1

print("Cantidad de Alumnos con notas mayores igual a 7: ", altas)
print("Cantidad de Alumnos cin notas menores igual a 7: ", bajas)
    
