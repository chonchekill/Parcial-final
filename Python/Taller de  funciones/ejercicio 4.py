def cant_numeros_pares(num):
    cuenta=0
    while num>0:
        ultimo_digito=num%10
        ultimo_digito=ultimo_digito%2
        num=num//10
        if ultimo_digito==0:
            cuenta += 1
    print("La cantidad de numeros pares es= ",cuenta)
num=int(input("Ingrese el numero= "))
cant_numeros_pares(num)


