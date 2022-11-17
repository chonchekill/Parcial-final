sueldo=int(input("Sueldo= "));
años=int(input("Años de antiguedad= "))
if sueldo<500 and años>=10:
    sueldo20=sueldo*1.2 #sueldo del 20%
    print("Su sueldo aumento un 20% = ",sueldo20)
if sueldo<500 and años<10:
    sueldo5=sueldo*1.05
    print("Su sueldo aumento un 5% = ",sueldo5)

if sueldo>=500:
    print("Su sueldo no ha aumentado = ",sueldo)
