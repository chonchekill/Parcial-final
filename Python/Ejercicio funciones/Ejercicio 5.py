from audioop import mul


def tablas_de_multiplicar(num,tablas_hasta):
    x=1
    for x in range(tablas_hasta+1):
        mult=num*x
        print("La tabla de ",num,"x",x,end=" ")
        print("es",mult)
num=int(input("Ingrese el numero de la tabla de multiplicar= "))
tablas_hasta=int(input("Ingrese el valor hasta donde quiera la tabla= "))
tablas_de_multiplicar(num,tablas_hasta)