#Pedir al usuario 5 calificaciones y obtener promedio

Nombre = input("Ingresar nombre de el alumno: ")
l = ("Ingresa la calificacion segun la materia: ")
C = int(input("Calculo: "))
P = int(input("Programacion: "))
T = int(input("TICS: "))
M = int(input("Matematicas: "))
I = int(input("Ingles: "))


Cal = (C+P+T+M+I)
Promedio = Cal/5

print(Promedio)
print("Finalizado")