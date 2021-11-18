#Hacer un programa que pida nombre y edad y que imprima la persona más grande. 
z=int(input("Ingrese la cantidad de personas a comparar "))
c=1
x='relleno'
w=0

while z>=c:
	c=c+1
	a=str(input("ingrese un nombre "))
	b=int(input("ingrese una edad "))
	if b>w:
		x=a


print ("La persona con la mayor edad es ",x)