

#promedio de duracion
otros_cursos_min= 2.5
otros_cursos_max = 7
otros_cursos_promedio= 4
dalto_curso = 1.5
#duracion de crudos

crudo_promedio = 5
crud_dalto = 3.5



#diferencias de duracion 

diferencias_con_min =100 - (dalto_curso / otros_cursos_min  * 100)
diferencias_con_max =100 - (dalto_curso  *1000 // otros_cursos_max /10)
diferencias_con_promedio = 100 -(dalto_curso / otros_cursos_promedio)*100

#Calculando el tiempo Vacio promedio
#tiempo_vacio_promedio = 100 - dalto_curso * 1000 / otros_cursos_max
tiempo_vacio_promedio1 = 100- otros_cursos_promedio* 1000 // crudo_promedio /10
tiempo_vacio_dalto = 100- dalto_curso * 1000// crud_dalto /10
#mostrando la diferencia de duracion 
print('El curso de Dalto dura: ')
print(f'-- un {diferencias_con_min} %menos que el mas  rapido')
print(f'-- una {diferencias_con_max} menos que el que mas lento ')
print(f'-- un {diferencias_con_promedio} menos que el promedio')
print('----------------------------------------')
#mostrando la cantidad de  espacio  que  se remueven  (ejercicio 0)
print(f'un curso promedio elimina un {tiempo_vacio_promedio1}% de tiempo vacio')
print(f'ESte curso promedio elimina un    {tiempo_vacio_dalto}% de tiempo vacio ')
print('-------------------------------------------------')

#Mostrando las  diferencias del ver si los cursos duran 10 hrs

print(f'ver 10 horas de este curso equile {otros_cursos_promedio*1000 // dalto_curso /100} ')
print(f'ver 10 horas de este curso equile {dalto_curso*1000 // otros_cursos_promedio /100} ')
print('-----------------------------------------------------')

