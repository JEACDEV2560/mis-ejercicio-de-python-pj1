cantidad=0
x=1
n= int(input("Cuantas Piezas cargara:"))
while x<=n:
    largo=float(input("Ingrese la medida de lsa pieza:"))
    if largo>=1.2 and largo <=1.3:
        cantidad=cantidad+1
    x=x+1
    print("Cantidad de piezas son aptas son: ", cantidad)
