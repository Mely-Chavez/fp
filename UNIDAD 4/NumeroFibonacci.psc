Algoritmo NumeroFibonacci
	ESCRIBIR "	Ingresa un numero: "
	LEER NF
		Definir x Como Entero
		Definir a,b,c Como Real
		a = 0
		b = 1
		c = 1
		Mientras x <= NF Hacer
			Escribir a
			c = a + b
			a = b
			b = c
			x = x + 1
		FinMientras
		z= x + b - x -1
		ESCRIBIR "La suma es: ",z
FinAlgoritmo
