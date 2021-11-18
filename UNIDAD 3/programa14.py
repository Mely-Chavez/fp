#Pedir calificaciones y que muestre si aprobo
N = 5
Nombre = input("Ingresar nombre del alumno: ")
print("Ingresa calificaciones de cada materia ")
C1 = int(input("Calculo: "))
C2 = int(input("Programacion: "))
C3 = int(input("Fisica: "))
C4 = int(input("TICS: "))
C5 = int(input("Matematicas: "))

Calif = (C1+C2+C3+C4+C5)
Promedio = (Calif/N)

if Promedio > 7:
	print(Nombre, Promedio, " Aprobo")
elif Promedio < 7:
	print(Nombre, Promedio, " Reprobo")
else:
	print("Error")

print("Fin")