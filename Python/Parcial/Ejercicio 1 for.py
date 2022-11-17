#EJERCICIO 1 CICLO FOR
resul=0
m=1
resul1=1
num=int(input("Digite el número de términos "))

for m in range(m,num):
    total= resul+ resul1
    resul1=resul
    resul= total
    print ("La secuencia es :", resul)