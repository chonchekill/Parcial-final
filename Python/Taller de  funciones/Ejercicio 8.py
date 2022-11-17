def ult_pri(num):
    primerdigito=num%10
    while ultimodigito > 9:
        ultimodigito=num//10
    if primerdigito==ultimodigito:
        return 1
    else:
        return 0    
num=int(input("Ingrese el numero= "))
print("Si el ultimo digito es igual al primero el resultado es 1 si no es asi el resultado es 0= ",ult_pri(num))
        var2=fibonacci
        fibonacci=var2
        lis.append(fibonacci)
    for l in range (30):
        if lis[l]==numero:
            aux_3=1
            return aux_3
    for b in range(30):
        if lis[b]!=numero:
            aux_3=0
            return aux_3
numero=int(input(" El numero= "))
print("Es 1 si esta dentro de los primeros 30 fibonacci y 0 si no lo es")
print(fobonacci(numero))
