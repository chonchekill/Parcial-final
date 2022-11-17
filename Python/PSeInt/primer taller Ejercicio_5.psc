Algoritmo Ejercicio_6
	definir R, h, a, ap como Reales
	Escribir "Calculadora del área y volumen del cono"
	Repetir
		Escribir "1. Calculadora a partir del radio y la altura inclinada"
		Escribir "2. Calculadora a partir de la altura y la altura inclinada"
		Escribir "3. Calculadora a partir del ángulo (apertura) en grados y altura inclinada"
		Escribir "4. Calculadora a partir del ángulo (apertura) en grados y altura inclinada"
		Escribir "5. Salir"
		Leer op 
		segun op Hacer
			1 : Escribir "Radio(R)="
				Leer R 
				Escribir "altura"
				Leer h
				V=((3.1416*h*R^2)/3)
				Escribir "Volumen =", V
				A= (3.1416*R)*(R+((R^2+h^2)^0.5))
				Escribir "Area =", A
				a=A/(3.1416*R)-R
				Escribir "Altura inclinada =", a
			2 :
				Escribir "Radio ="
				leer R
				Escribir "Altura inclinada ="
				Leer a
				A=(3.1416*R)*(R+a)
				Escribir "Area =", A
				h=((A/(3.1416*R)-r)^2-R^2)^0.5
				Escribir "Altura =", h
				V=(3.1416*h*R^2)/3
				Escribir "Volumen =", V
			3 :
				Escribir "Altura ="
				Leer h
				Escribir "altura inclinada"
				Leer a
				R=(a^2-H^2)^0.5
				Escribir "Radio =", R
				V=(3.1416*h*R^2)/3
				Escribir "Volumen =", V
				A=(3.1416*R)*(R+a)
				Escribir "Area =", A
			4 :
				Escribir "Apertura (Grados) ="
				Leer ap
				Escribir "Altura inclinada"
				Leer a
				h=cos(ap/2*PI/180)*a
				Escribir "Altura =", h
				R=sen(ap/2*PI/180)*a
				Escribir "Radio =", R7
				A=(3.1416*R)*(R+a)
				Escribir "Area =", A
				V=(3.1416*h*R^2)/3
				Escribir "Volumen =", V
				
		FinSegun
		
	Hasta Que op = 5
	
FinAlgoritmo
