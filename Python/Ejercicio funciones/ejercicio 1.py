def numero_menor():
    num1=int(input("Ingrese el numero 1= "))
    num2=int(input("Ingrese el numero 2= "))
    num3=int(input("Ingrese el numero 3= "))
    if num1 < num2 and num1 < num3:
        print("El numero menor es el primero= ",num1)
    else:
        if num2 < num3:
            print("El numero menor es el segundo= ",num2)
        else:
            print("El numero menoe es el tercero= ",num3)
for x in range (2):
    numero_menor()