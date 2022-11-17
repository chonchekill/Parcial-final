opcion=0
while opcion<=2:
    print("1. Aceleracion");
    print("2. Distancia recorrida");
    print("3. Salir");
    opcion=int(input("Escoger una opción= "));
    if opcion == 2:
        distancia_inicial=int(input("Ingrese la distancia inicial= "));
        velocidad_inicial=int(input("Ingrese la velocidad inicial= "));
        tiempo=int(input("Tiempo= "));
        aceleracion=float(input("aceleración= "));
        recorrido=(velocidad_inicial)+(distancia_inicial*tiempo)+(0.5*(aceleracion*(tiempo*tiempo)))
        print("Distancia recorrida= ", recorrido);
    else:
        if opcion == 1:
            velocidad_final=int(input("Velocidad final= "));
            velocidad_inicial=int(input("Velocidad inicial= "));
            tiempo=int(input("Tiempo= "));
            aceleracion=(velocidad_final-velocidad_inicial)/tiempo;
            print("La aceleración= ", aceleracion);
else:
    quit     