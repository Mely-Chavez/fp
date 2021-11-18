
#Ingresa 5 calificaciones e imprimirlas en un renglon

Nombre = input("Ingresar nombre del alumno: ")
notas = dict()

notas["Matematicas: "] = int(input("Matematicas"))
notas["Programacion"] = int(input("Programacion: "))
notas["Ingles"] = int(input("Ingles: "))
notas["Etica"] = int(input("Etica: "))
notas["TICS"] = int(input("TICS: "))

print(notas)