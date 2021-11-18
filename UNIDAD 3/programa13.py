#Imprimir la palabra con mayor cantidad de letras

A = input("Escribir primer palabra: ")
First = (A)
B = input("Escribir segunda palabra: ")
Second = (B)

if len(First) > len(Second):
	print(First)
elif len(First) < len(Second):
	print(Second)
else: 
	print("Tiene la misma cantidad de letras")

print("Fin")