def edades_mayores(*lista):
    contador=0
    for x in range (len(lista)-1):
        if lista[x] >= 18:
            contador = contador + 1
    return contador
lista=[]
opc=0
while opc < 3:
    print("------------------------------------------------")
    print("1. Si quiere agregar otra edad ")
    print("2. Si quiere saber cuales son mayores de 18 años")
    print("3. Salir")
    print("------------------------------------------------")
    opc=int(input("ingrese el numero de la opción que deseé ejecutar= "))
    if opc == 1:
        edad=int(input("Ingrese la edad= "))
        lista.append(edad)
    if opc == 2:
        print("Las edades mayores de 18 son= ",edades_mayores(lista))
        