nombre=input("Ingrese el nombre= ")
numero_preguntas=int(input("Ingrese el numero de preguntas= "))
preguntas_buenas=int(input("Ingrese las preguntas que respondio bien= "))
calificacion=preguntas_buenas*100/numero_preguntas
if calificacion>=90:
    print("Nivel maximo")
else:
    if calificacion>=75:
        print("Nivel medio")
    else:
        if calificacion>=50:
            print("Nivel regular")   
        else:
            if calificacion<50:
                print("Fuera de nivel")
