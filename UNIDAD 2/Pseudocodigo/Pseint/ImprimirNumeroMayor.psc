Algoritmo ImprimirNumeroMayor
	ESCRIBIR "Ingresa el primer numero"
	LEER Num1
	ESCRIBIR "Ingresa el segundo numero"
	LEER Num2
	ESCRIBIR "Ingresa el tercer numero"
	LEER Num3
	
	SI Num1>Num2 O Num1>Num3 Entonces 
		ESCRIBIR "El numero mayor es ",Num1;
	SiNo
		SI Num2>Num1 O Num2>Num3 Entonces
			ESCRIBIR "El numero mayor es ",Num2;
			
		SiNo
			SI Num3>Num1 O Num3>Num2 Entonces
				ESCRIBIR "El numero mayor es ",Num3;
			FinSi
		FinSi
	FinSi
FinAlgoritmo
