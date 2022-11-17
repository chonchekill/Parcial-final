mayor12=0
Numero_n=int(input("Ingrese el numero de triangulos= "))
for y in range (Numero_n):
    alt=float(input("Ingrese la altura= "))
    base=float(input("Ingrese la base= "))
    superficie=base*alt/2
    print("La superficie es= ", superficie)
if superficie>=12:
     mayor12=mayor12+1
     print("La superficie mayor a 12 =", mayor12)
