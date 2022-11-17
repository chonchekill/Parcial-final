Algoritmo ejercicio_2
	Definir Vf,Vo,T,M,R Como real
	Definir a Como Real
	Repetir
		Escribir "1. Convertidor de velocidad";
		Escribir "2. Tiempo";
		Escribir "3. Salir";
		Escribir "Seleciona una opcion";
		Leer op 
		segun op hacer 
			1 :
				Escribir "velocidad en km/h"
				leer M
				R=(M*1000)/3600
				Escribir "Velocidad en m/s" ,R
				
			2 :
				Escribir "Velocidad final";
				leer Vf;
				Escribir "Velocidad inicial";
				leer Vo;
				Escribir "Aceleracion";
				leer a
				T=(Vf-Vo)/a
				Escribir "Aceleración:" , T
			
		FinSegun
		
	Hasta Que op = 3
	
	
	
FinAlgoritmo
