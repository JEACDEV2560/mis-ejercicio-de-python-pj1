#

#def suma(lista):
 #   numeros_sumados=0
  #  for numero in lista:
   #     numeros_sumados = numeros_sumados + numero
   #     return  numeros_sumados
        
   # return numeros_sumados

#resultado = suma([1,5,9])
#print(resultado)

#utilizando el parametro *args (argumentos variables)

def  suma(nombre,*numeros):
    return  f"{nombre}la suma de tus numeros:  {sum(numeros)}"

resultado = suma("Lucas",1,5,9,10,20,30)
print(resultado)
