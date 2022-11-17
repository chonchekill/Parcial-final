#Funcion
def multiplicacion_entero(num,lista):
    for x in range(len(lista)):
        mul=num*lista[x]
        print("El producto de la multiplicacion de el numero ",lista[x], "por el valor ", num, "es igual a=",mul)
lista=[3, 7, 8, 10, 2]
num=int(input("Ingrese el numero: "))
multiplicacion_entero(num,lista)

    


