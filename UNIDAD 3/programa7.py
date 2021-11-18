#Pedir un numero al usuario y que imprima el numero mayor.

Num1 = int(input("Ingresa primer numero: "))
Num2 = int(input("Ingresa segundo numero: "))

if Num1 < Num2:
	print (Num2)
elif Num1 > Num2:
	print(Num1)
else:
	print("Error: Datos incorrectos")

