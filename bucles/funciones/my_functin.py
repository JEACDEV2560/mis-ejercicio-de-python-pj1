#def saludo():
#    print("Hola, ¿cómo estás? josias Aguilar")


#saludar()

#creando funciones con parametros 
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == 'mujer'):
        ajectivo = 'bella mi reina '
    elif (sexo == 'hombre'):
            ajectivo = 'Titan'
    else:
            ajectivo = ' amor'
       
    print(f'Hola, ¿cómo estás? {nombre} ¿como andas?  mi {ajectivo}' ) 

saludar('kamila', 'Mujer')
saludar('Josias', 'Hombre')
   
#crear una funcion que retorne valores
 
def crear_contraseña_radom(num):
    chars = "abdcfghijklmnopqrstuvwxyz1234567890"
    numero_entero= str(num)
    c1 = num -2
    c2 = num 
    c3 = num - 5

    contraseña = f"{chars[c1]} {chars[c2]}  {chars[c3]} {num*2}"
    return contraseña

password= crear_contraseña_radom(8) 
frase = f"Su contraseña nueva  es:  {password}"
print(frase)