animales = ["gato", "perro","loro","cocodrilo","pez"]
numeros = [10,63,12,72,36,55]
numero1 = [12,23,44,55,77,88,123,43,434]
for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')


#recorriendo la lista de numero y multiplicando  cada valor por 10

for numero in numeros:
    print(numero * 10)
    print("El Valor de los numeros es : " , numero)


for numero , animales,numero1  in zip (animales, numeros,numero1):
    print(f'recorriendo la lista 1 {numero }')
    print(f'recorriendo la lista 2{animales }')
    print(f'recorriendo la lista 3{numero1 }')