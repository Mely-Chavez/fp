
#EXAMEN DE UNIDAD 3
#crear clase
class Alumno():
 	def __init__ (self,edad,nombre,calculo,programacion,fundamentos,tics,etica,ingles,matematicas,promedioprep,ubicacionvivienda,recorridoaltec):
 		self.tics = tics
 		self.etica = etica
 		self.ingles = ingles
 		self.nombre = nombre
 		self.edad = edad
 		self.calculo = calculo
 		self.programacion = programacion
 		self.fundamentos = fundamentos
 		self.matematicas = matematicas
 		self.promedioprep = promedioprep
 		self.ubicacionvivienda = ubicacionvivienda
 		self.recorridoaltec = recorridoaltec

#crear objetos
paola=Alumno(18,"Paola", 10, 9, 8, 9, 10, 9, 8, 8, "Bariio de carboneras", 8)
isaac=Alumno(19, "Isaac", 10, 9, 10, 9, 10, 10, 10, 9, "Rincon de romos", 13)
areli=Alumno(19, "Areli", 10, 9, 10, 9, 10, 9, 10, 8, "Rincon de romos", 13)
alain=Alumno(18, "Alain", 10, 9, 10, 9, 10, 9, 10, 8, "Asientos", 11)
alexis=Alumno(19, "Alexis", 10, 9, 10, 8, 7, 8, 7, 8, "Rincon de romos", 13)
reyna = Alumno(18,"Reyna", 9, 8, 10, 10, 9, 6, 7, 9, "Rincon de romos", 13)
mirozlava = Alumno(18,"Mirozalva",9, 8, 10, 7, 9, 6, 7, 8, "Cosio", 27)
mely = Alumno (18,"Melany", 5, 5, 7, 5, 5, 5, 5, 9, "Pabellon de Arteaga", 5)
diego = Alumno(19,"Diego", 8, 9, 9, 10, 8, 8, 10, 10, "Rincon de romos", 13) 
britzy = Alumno(18,"Britzy", 10, 9, 10, 10, 8, 8, 10, 10, "Rincon de romos", 13) 
fernando = Alumno(17, "Fernando", 8, 8, 7, 9, 10, 8, 10, 9, "Pabellon de Arteaga", 5)
alejandra = Alumno(18,"Alejandra", 10, 10, 10, 10, 10, 10, 10, 8, "Jesus Maria", 27)
alejandro= Alumno(19, "Alejandro", 10, 9, 8, 9, 8, 9, 8, 9, "Ejido Fresnillo", 17)
donaldo= Alumno(18, "Donaldo", 8, 9, 10, 9, 8, 6, 8, 8, "Pabellon de Arteaga", 5)
austin= Alumno(18, "Austin", 10, 9, 8, 9, 10, 9, 8, 8, "Pabellon de Arteaga", 5)

#alumnos con mayor edad
print ("Los alumnos que son mayores de edad son: ", diego.nombre,",",alejandro.nombre,",",isaac.nombre,",",areli.nombre,"y",alexis.nombre )
#alumnos con su promedio
print ("A continuacion los nombres de los alumnos y sus calificiones\n", reyna.nombre,"y promedio de",reyna.promedioprep,",\n",mirozlava.nombre,"y promedio de",mirozlava.promedioprep)
print(mely.nombre,"y promedio de",mely.promedioprep,",\n",diego.nombre,"y promedio de",diego.promedioprep,",\n",britzy.nombre,"y promedio de",britzy.promedioprep)
print(fernando.nombre,"y promedio de",fernando.promedioprep,",\n",alejandra.nombre,"y promedio de",alejandra.promedioprep,",\n",alejandro.nombre,"y promedio de",alejandro.promedioprep)
print(donaldo.nombre,"y promedio de",donaldo.promedioprep,",\n",austin.nombre,"y promedio de",austin.promedioprep,",\n",paola.nombre,"y promedio de",paola.promedioprep)
print(isaac.nombre,"y promedio de",isaac.promedioprep,",\n",areli.nombre,"y promedio de",areli.promedioprep,",\n",alain.nombre,"y promedio de",alain.promedioprep,",\n",alexis.nombre,"y promedio de",alexis.promedioprep)
#alumnos que viven mas cerca y mas lejos
print("Los alumnos que viven mas lejos del tec son:\n",mirozlava.nombre,"es de ",mirozlava.ubicacionvivienda, "con una distancia de", mirozlava.recorridoaltec, "y\n", alejandra.nombre, "es de", alejandra.ubicacionvivienda, "con una distancia de",alejandra.recorridoaltec )
print("Los alumnos que viven mas cerca del tec son:\n",mely.nombre,"es de ",mely.ubicacionvivienda, "con una distancia de", mely.recorridoaltec, "y\n", donaldo.nombre, "es de", donaldo.ubicacionvivienda, "con una distancia de",donaldo.recorridoaltec )
#alumnos y su mejor calificacion de materia
print ("Los alumnos y las materias en la que mas desempeñan son: \n", reyna.nombre,"en la meteria de fundamentos de la programacion",",\n",mirozlava.nombre,"en la meteria de fundamentos de la investigación")
print(mely.nombre,"en la materia de ingles",",\n",diego.nombre,"en la materia de fundamentos de programacion",",\n",britzy.nombre,"en la materia de calculo diferencial")
print(fernando.nombre,"en la materia de introduccion de Tic's",",\n",alejandra.nombre,"en la materia de introduccion a las tics",",\n",alejandro.nombre,"en la materia de calculo diferencial")
print(donaldo.nombre,"en la materia de matematicas discretas",",\n",austin.nombre,"en la materia programacion ",",\n",paola.nombre,"en la materia de fundamentos de investigacion ")
print(isaac.nombre,"en la materia de taller de etica",",\n",areli.nombre,"en la materia de etica",",\n",alain.nombre,"en la materia de calculo diferencial",",\n",alexis.nombre,"en la materia de matematicas discretas ")
 
