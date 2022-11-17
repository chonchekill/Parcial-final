#EJECRICIO 1 -- CICLO WHILE
resul = 0
resul1 = 1
m=1 


num=int(input("Digite el número de términos "))

while(m <= num):
   total= resul+ resul1
   resul1=resul
   resul=total
   print ("La secuencia es :", resul)
   m= m+1