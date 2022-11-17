from cmath import cos, pi, sin
print("Calculadora de área y volumen de un cono");
opcion=0
while opcion<=5:
    print("1. Calculadora a partir del radio y la altura inclinada");
    print("2. Calculadora a partir de la altura y la altura inclinada");
    print("3. Calculadora a partir del ángulo (apertura) en grados y altura inclinada");
    print("4. Calculadora a partir del ángulo (apertura) en grados y altura inclinada");
    print("5. Salir")
    opcion=int(input("Seleccione una opcion= "));
    if opcion == 1:
        radio=float(input("Radio= "));
        altura=float(input("Altura= "));
        volumen=((3.1416*altura*(radio*radio))/3)
        area=(3.1416*radio)*(radio+((radio**2+altura**2)**0.5))
        altura_inclinada=area/(3.1416*radio)-radio
        print("Volumen= ", volumen);
        print("Área= ", area);
        print("Altura inclinada= ", altura_inclinada);
    if opcion == 2:
        radio=float(input("Radio= "));
        altura_inclinada=float(input("Altura inclinada= "));
        area=(3.1416*radio)*(radio+altura_inclinada)
        altura=((area/(3.1416*radio)-radio)**2-radio**2)**0.5
        volumen=(3.1416*altura*radio**2)/3
        print("Área= ", area);
        print("Altura= ", altura);
        print("volumen= ", volumen);
    if opcion == 3:
        altura_inclinada=float(input("Altura inclinada= "))
        altura=float(input("Altura= "))
        radio=(altura_inclinada**2-altura**2)**0.5
        volumen=(3.1416**radio**2)/3
        area= (3.1416*radio)*(radio+altura_inclinada)
        print("Radio= ", radio)
        print("Volumen= ", volumen)
        print("Área= ",area)
    if opcion == 4:
        apertura=float(input("Apertura(grados)= "))
        altura_inclinada=float(input("Altura inclinada= "))
        altura=cos(apertura/2*pi/180)*altura_inclinada
        radio=sin(apertura/2*pi/180)*altura_inclinada
        area=(pi*radio)*(radio+altura_inclinada)
        volumen=(pi*altura*radio**2)/3
        print("Altura= ", altura)
        print("Radio", radio)
        print("Área= ", area)
        print("Volumen", volumen)
else:
    if opcion == 5:
        quit        

        

        



        