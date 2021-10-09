Algoritmo PersonaMayor
	
	Escribir 'Ingresa el nombre de la primer persona: '
	Leer nombre1
	Escribir 'Ingrese la edad:'
	Leer edad1
	Escribir 'Ingresa el nombre de la segunda persona: '
	Leer nombre2
	Escribir 'Ingrese la edad:'
	Leer edad2
	Escribir 'Ingresa el nombre de la tercera persona'
	Leer nombre3
	Escribir 'Ingrese la edad:'
	Leer edad3
	Si edad1>edad2 y edad1>edad3 Entonces
		Escribir 'La persona mayor es: ',nombre1;
	SiNo
		Si edad2>edad1 y edad2>edad3 Entonces
			Escribir 'La persona mayor es: ',nombre2;
		 SiNo
			Si edad3>edad1 y edad3>edad2 Entonces
				Escribir 'La persona mayor es: ',nombre3; 
			FinSi
		FinSi
	FinSi
	
	
FinAlgoritmo
