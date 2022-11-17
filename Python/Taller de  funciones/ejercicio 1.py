# Desarrollo de la funcion
def ultimo_numero(num):
    ultimo_numero=num%10
    return(ultimo_numero)
# Llamado a la funcion
num=int(input("Ingrese el numero= "))
print("El ultimo digito es= ",ultimo_numero(num))