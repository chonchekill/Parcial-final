from pyexpat.errors import XML_ERROR_SYNTAX
import pandas as pd
Archivo= pd.read_excel('C:/Users/SANTI/Downloads/Libro.xlsx',index_col=0,engine="openpyxl")#para leer el archivo excel
print(Archivo)
print(Archivo.fillna({"Nota2":2}))#Remplaza los datos vacios por los valores que les demos
print(Archivo.dropna())#Elimina las filas con los datos vacios
"print(Archivo['A1'])"#Muestra solo una columna
"print(Archivo[['A1',A2]])"#Muestra un grupo de columnas
"print(Archivo.iloc[0])"#Muestra una sola fila
print(Archivo.iloc[0:2])#Muestra las filas hasta el valor despues de los :
Archivo.iloc[[0,1,2]]#Muestra un grupo de filas
Archivo.head(3)#Muestra las primera 5 filas si no se le da valor
Archivo.tail(3)#Muestra las ultimas 5 filas si no se le da valor
Archivo.info()#Muestra informacion sobre nuestro documento
"Archivo.loc[]"#Muestra por fila pero con id
"""Archivo[Archivo[["Nota2"]>3]]"""#Condicion
"""Archivo[Archivo["Nombre"].str.contains("Santiago")]"""#Condicion de tipo cadena

#Como trasformar datos por medio de una función
"""def Promedio(Nota1):
    promedio=Nota1/2          
    return promedio
Archivo["Promedio"]=Archivo["Nota1"].apply(Promedio)"""
def Promedio(lista):
    promedio=lista["Nota1"]+lista["Nota2"]/2
    return [promedio]

    



