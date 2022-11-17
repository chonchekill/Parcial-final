def num_multiplo(num,digito):   
    if num%digito==0:
        aux=1
        return aux
    else:
        aux=0
        return aux
num=int(input("Ingrese el numero= "))
digito=int(input("Ingrese el digito= "))
print("Si el valor es 1 si es multiplo si no lo es el resultado es 0")
print(num_multiplo(num,digito))
