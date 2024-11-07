### diccionario ###

my_dict = dict()

my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "josias", "Apellido": "Aguilar", "Edad": 25 , 1: "python"}

my_dict= { 
  "nombre": "josias",
  "Apellido": "Aguilar",
  "Edad": 25,
  "Lenguaje":{ "Python", "C# ", "JAVA"},
    1: 1.77
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

my_dict["nombre"] = "pedro"
print(my_dict["nombre"])

print(my_dict[1])

my_dict["calle"] = "Calle Peña"
print(my_dict)

del my_dict["calle"]
print(my_dict)

print("Apellido" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_dict.fromkeys("nombre",1))
