def fobonacci(numero):
    var1=1
    fibonacci=0
    var2=0
    y=0
    lis=[]
    for x in range (30):
        fibonacci=var1+fibonacci
        var2=var1
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
numero=int(input("El numero= "))
print("Es 1 si esta dentro de los primeros 30 fibonacci y 0 si no lo es")
print(fobonacci(numero))