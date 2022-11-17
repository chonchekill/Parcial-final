def primer_digito(num):
    while num >= 10:
        num//=10
    return num
num=int(input("Ingrese el numero= "))
print("El primer digito es= ",primer_digito(num))