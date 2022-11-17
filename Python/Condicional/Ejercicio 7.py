num=int(input("Ingrese el numero del 1 al 999= "))
if num<=9:
    print("1 cifra")
if num>=10:
    if num<=100:
        print("2 cifras")
if num>=100:
    if num<=999:
        print("3 cifras")
    else:
        print("Ingreso un numero mayor a 999")
