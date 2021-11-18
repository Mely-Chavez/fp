#realizar un algoritmo para realizar sorteos.
import random
a=int(input("Ingrese el primer numero del sorteo: "))
b=int(input("Ingrese el ultimo numero del sorteo: "))
 
print("El ganador del sorteo es: ",random.randint(a,b))