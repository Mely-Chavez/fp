#Imprimir el numero mayor
A = int(input("Primer numero: "))
B = int(input("Segundo numero: "))
C = int(input("Tercer numero: "))

if A > B and C:
	print(A)
elif B > A and C:
		print(B)
elif C > A and B:
		print(C)
else:
		print("No se pudo encontrar el mayor")

print("Fin")