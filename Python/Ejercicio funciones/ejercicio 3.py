def cantidad_de_A_a(cadena):
    cantidad=0
    for x in range (len(cadena)):
        if cadena[x]=="a" or cadena[x]=="A":
            cantidad=cantidad+1
    return cantidad
palabra=input("Ingrese la palabra o oracion")
cantidad_de_A_a(palabra)
print("La cantidad de a o A es de= ",cantidad_de_A_a(palabra))