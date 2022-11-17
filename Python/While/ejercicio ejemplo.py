#Varibles
x=0
terminos_mayores_a_100=0
#costante
lista=[52,65,700,600,65,101,300,900]
#proceso
while x < len(lista):
    if lista[x]>=100:
        terminos_mayores_a_100=terminos_mayores_a_100+1
    x=x+1
print(terminos_mayores_a_100)