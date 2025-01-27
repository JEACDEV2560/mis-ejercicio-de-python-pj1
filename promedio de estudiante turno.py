suma1=0
suma2=0 
suma3=0

for fa in range(5):
    edad= int(input("Ingrese la edad del estudiante: "))
    suma1 = suma1 + edad
    promedio1 = suma1 / 5
    print("El promedio de edad de los estudiantes del turno de la  mañana es: ", promedio1)

for fa in range(6):
    edad= int(input("Ingrese la edad del estudiante: "))
    suma2 = suma2 + edad
    promedio2 = suma2 / 6
    print("El promedio de edad de los estudiantes del turno de la tarde es: ", promedio2)

for fa in range(11):
    edad= int(input("Ingrese la edad del estudiante: "))
    suma3 = suma3 + edad
    promedio3 = suma3 / 11
    print("El promedio de edad de los estudiantes del turno de la noche es: ", promedio3)

    if promedio1 > promedio2 and promedio1 > promedio3:
       print("El promedio de edad  el es mas  bajo  es del turno de la mañana")
    elif promedio2 > promedio1 and promedio2 > promedio3:
        print("El promedio de  el es edad mas bajo  es del turno de la tarde")
    else:
        print("El promedio de el es  edad mas bajo  es del turno de la noche")
