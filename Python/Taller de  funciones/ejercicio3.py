def numero_digitos(num):
    cuenta=0
    while num>0:
        num//=10
        cuenta +=1
    return cuenta
num=int(input("Ingrese el numero= "))
print("La cantidad de digitos son= ",numero_digitos(num))