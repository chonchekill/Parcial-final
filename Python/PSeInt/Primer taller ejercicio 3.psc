Algoritmo ejercicio_3
	Definir Vf, Vo, T, So, s  Como Real
	Definir a, a2 Como Real
	Repetir
		escribir "1. Aceleración"
		Escribir "2. Distancia recorrida"
		Escribir "3. Salir"
		Leer op 
		Segun op hacer 
			1 : 
				Escribir "Velocidad final";
				leer Vf;
				Escribir "Velocidad inicial";
				leer Vo;
				Escribir "Tiempo";
				leer T
				a= ((Vf - Vo)/T)
				Escribir "Aceleración:" , a
			2 :
				Escribir "Distancia inicial"
				leer So
				Escribir "Velocidad inicial"
				Leer Vo
				Escribir "Tiempo"
				Leer T
				Escribir "Aceleración"
				Leer a2
				s=Vf+(So*T)+0.5*(a2*(T*T))
				Escribir "Distancia recorrida" , s
				
		FinSegun
		
		
	Hasta Que op = 3
	
	
	
FinAlgoritmo
