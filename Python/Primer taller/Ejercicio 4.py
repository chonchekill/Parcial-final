opcion=0
while opcion<=2:
    print("1. Convertidor de velocidad");
    print("2. Tiempo");
    print("3. Salir");
    opcion=int(input("Escoger una opción= "));
    if opcion == 1:
        km_h=int(input("Ingrese los kilometros x hora= "));
        m_s= (km_h*1000)/3600
        print("Metros x segundos= ", m_s)
    else:
        if opcion == 2:
            velocidad_final=int(input("Velocidad final= "));
            velocidad_inicial=int(input("Velocidad inicial= "));
            aceleracion=float(input("Aceleracion= "))
            tiempo= (velocidad_final-velocidad_inicial)/aceleracion;
            print("El tiempo es= ", tiempo);
else:
    quit     