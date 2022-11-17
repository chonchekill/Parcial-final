# Desarrollo de la funcion
def ultimo_numero(num):
    ultimo_numero=num%100
    return(ultimo_numero)
# Llamado a la funcion
num=int(input("Ingrese el numero= "))
print("Los dos ultimos digitos son= ",ultimo_numero(num))