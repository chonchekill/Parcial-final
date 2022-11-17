lista_paises=[]
lista_de_habitantes=[]
for x in range(5):
    paises=input("Ingrese el nombre del pais: ")
    lista_paises.append(paises)
    habitantes=int(input("Ingrese el numero de habitantes: "))
    lista_de_habitantes.append(habitantes)
for k in range(4):
    for y in range(4-k):
        if len(lista_paises[y])>len(lista_paises[y+1]):
            aux1=lista_paises[y]
            lista_paises[y]=lista_paises[y+1]
            lista_paises[y+1]=aux1
            aux2=lista_de_habitantes[y]
            lista_de_habitantes[y]=lista_de_habitantes[y+1]
            lista_de_habitantes[y+1]=aux2
print ("Lista ordenada alfabeticamente")
print (lista_paises)
print (lista_de_habitantes)
for m in range(4):
    for t in range(4-k):
        if lista_de_habitantes[t] > lista_de_habitantes[t+1]:
            aux3=lista_de_habitantes
            lista_de_habitantes[t]=lista_de_habitantes[t+1]
            lista_de_habitantes[t+1]=aux3
            aux4=lista_paises[t]
            lista_paises[t]=lista_paises[t+1]
            lista_paises[t+1]=aux4
print("Lista ordenadamente por numero de habitantes")
print(lista_de_habitantes)
print(lista_paises)