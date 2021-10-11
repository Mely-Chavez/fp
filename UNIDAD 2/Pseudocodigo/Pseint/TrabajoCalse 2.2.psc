Algoritmo PalabrasConMasLetras
	ESCRIBIR 'Ingresa la primera palabra'
	LEER palabra1;
	ESCRIBIR 'Ingresa la segunda palabra'
	LEER palabra2;
	a = longitud (palabra1)
	c = longitud (palabra2)
	Si a>c Entonces
		ESCRIBIR 'La palabra ' ,palabra1 ' es mayor';
		SiNo 
			Si c>a Entonces 
				ESCRIBIR 'La palabra ', palabra2 ' es mayor'
			FinSi
		FinSi
FinAlgoritmo
