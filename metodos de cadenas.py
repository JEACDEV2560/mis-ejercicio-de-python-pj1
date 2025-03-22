cadena = "Hola Soy Dalto"
cadena1= "Hola Chamo como estas ! " 
cadena2= "Hola Maria soy jose "
cadena3= "Hola Maria soy Paul el Actor"
resultado=cadena.upper()

#print(resultado)

minusculas=cadena.lower()

#print(minusculas)

#buscamos una cadena dentro de otra

busqueda_find = cadena1.find("a")

print(busqueda_find) 

busqueda_index= cadena1.isnumeric()

es_alfa = cadena1.isalpha()

contar_coincidencias = cadena2.count("a")

print(contar_coincidencias)

#contar caracteres en python 
contar_caracteres= len(cadena1)

print(contar_caracteres)


termina_con = cadena1.startswith("la")

print(termina_con)


cadena_nueva = cadena1.replace("Hola","Saludos")

print(cadena_nueva)



cadena_nueva2 = cadena_nueva.capitalize()


print(cadena_nueva2)

#separar una cadena en python

cadena_separa = cadena3.split(" ")

print(cadena_separa)

