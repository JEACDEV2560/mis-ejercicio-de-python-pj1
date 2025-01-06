suma=0
x=1
n=int(input("¿Cuantas Personas vas a Procesar ?:"))
while x <=n:
    altura = float(input("Indique la Altura:"))
    suma= suma+altura
    x=x+1
    promedio= suma/n
    print("La altura promedio es:",promedio)
