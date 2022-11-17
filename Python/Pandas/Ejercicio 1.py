import pandas as pd
notas_semillero=pd.DataFrame({"Nombre":["pedro","ana","santiago","viviana","mateo","esteban","juan","gloria","laura","martha"],"Semestres":[9,2,3,5,1,2,6,8,6,10]})
notas_semillero["nota1"]=[8,5,9,6,8,9,6,5,6,8]
notas_semillero["nota2"]=[1.2,3.5,5,10,5.5,6.5,2,4.7,9,6]
notas_semillero["nota3"]=[5.5,6.5,8,6.5,3.2,3,4,3.2,8,9]
notas_semillero.insert(5,"Cuidad",["Manizales","pereira","bogota","neira","sta marta","victoria","Manizales","dorada","victoria","pereira"])
def Promedio(lista):
    promedio =(lista["nota1"]+lista["nota2"]+lista["nota3"])/3
    return promedio
notas_semillero["Promedio"]=notas_semillero.apply(Promedio, axis=1)#Para que lea todas las filas
notas_semillero=notas_semillero.groupby("Cuidad").mean([["nota1","nota2","nota3"]])#Esto sirve para agrupar todas las cuidades que tengan el mismo nombre en una
notas_semillero=notas_semillero[notas_semillero["Promedio"]>5]
notas_semillero=notas_semillero.iloc[0]
print(notas_semillero)