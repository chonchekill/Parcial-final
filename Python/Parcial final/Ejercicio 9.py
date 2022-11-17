#Funciónes
def separador():
    print("--------------------------------------------------------------------------------------------------------")
class Coche():
    #Metodo iniciador
    def __init__(self,color,marca,modelo,combustible,puertas,motor,ruedas,ventanas,puerta):
        self.color=color
        self.marca=marca
        self.modelo=modelo
        self.combustible=combustible
        self.puertas=puertas
        self.motor=motor
        self.ruedas=ruedas
        self.ventanas=ventanas
        self.puerta=puerta
        separador()
        print("El carro es un {}, modelo {}, de color {}, tiene {} puertas, usa {}, el motor está {}, tiene las ruedas {}, y sus ventanas están {}.".format(marca,modelo,color,puertas,combustible,motor,ruedas,ventanas,))
        print("sus puertas estan")
        print(puerta)
        separador()
#Clase
class Motor():
    #Metodos
    def encendido_apagado(self,opc1):
        if opc1 == "encender":
            motor="encendido"
            return motor
        if opc1 == "apagar":
            motor="apagado"
            return motor        
#Clase
class Ruedas(Motor):
    #Metodos 
    def inflar_desinflar(self,opc2):
        if opc2 == "inflar":
            ruedas="infladas"
            return ruedas
        if opc2 == "desinflar":
            ruedas="desinfladas"
            return ruedas
#Clase
class Ventanas(Ruedas):
    #Metodos 
    def  abrir_cerrar_ventanas(self,opc3):
        if opc3== "abrir":
            ventanas="abiertas"
            return ventanas    
        if opc3 == "cerrar":
            ventanas="cerradas"
            return ventanas
#Clase
class Puertas(Ventanas):
    #Metodo 
    def abrir_cerrar_puertas(self,opc4):
        if opc4 == "abrir":
            puerta="""   __---~~~~--__                      __--~~~~---__
 `\---~~~~~~~~\\                    //~~~~~~~~---/'  
   \/~~~~~~~~~\||                  ||/~~~~~~~~~\/ 
               `\\                //'
                 `\\            //'
                   ||          ||      
         ______--~~~~~~~~~~~~~~~~~~--______              
    ___ // _-~                        ~-_ \\ ___  
   `\__)\/~                              ~\/(__/'          
    _--`-___                            ___-'--_        
  /~     `\ ~~~~~~~~------------~~~~~~~~ /'     ~\        
 /|        `\         ________         /'        |\     
| `\   ______`\_      \------/      _/'______   /' |          
|   `\_~-_____\ ~-________________-~ /_____-~_/'   |  
`.     ~-__________________________________-~     .'       
 `.      [_______/------|~~|------\_______]      .'
  `\--___((____)(________\/________)(____))___--/'           
   |>>>>>>||                            ||<<<<<<|"""
            return puerta
        if opc4 == "cerrar":
            puerta="""
    
         ______--~~~~~~~~~~~~~~~~~~--______              
    ___ // _-~                        ~-_ \\ ___  
   `\__)\/~                              ~\/(__/'          
    _--`-___                            ___-'--_        
  /~     `\ ~~~~~~~~------------~~~~~~~~ /'     ~\        
 /|        `\         ________         /'        |\     
| `\   ______`\_      \------/      _/'______   /' |          
|   `\_~-_____\ ~-________________-~ /_____-~_/'   |  
`.     ~-__________________________________-~     .'       
 `.      [_______/------|~~|------\_______]      .'
  `\--___((____)(________\/________)(____))___--/'           
   |>>>>>>||                            ||<<<<<<|"""
            return puerta
#Bloque principal 
color=input("El color del coche es: ")
marca=input("La marca de coche es: ")
modelo=int(input("El modelo del coche es: "))
combustible=input("Tipo de combustible del coche: ")
puertas=int(input("Cuántas puertas tiene el coche: "))
motor="apagado"
ventanas="cerradas"
ruedas="infladas"
puerta="""         ______--~~~~~~~~~~~~~~~~~~--______              
    ___ // _-~                        ~-_ \\ ___  
   `\__)\/~                              ~\/(__/'          
    _--`-___                            ___-'--_        
  /~     `\ ~~~~~~~~------------~~~~~~~~ /'     ~\        
 /|        `\         ________         /'        |\     
| `\   ______`\_      \------/      _/'______   /' |          
|   `\_~-_____\ ~-________________-~ /_____-~_/'   |  
`.     ~-__________________________________-~     .'       
 `.      [_______/------|~~|------\_______]      .'
  `\--___((____)(________\/________)(____))___--/'           
   |>>>>>>||                            ||<<<<<<|"""
carro=Coche(color,marca,modelo,combustible,puertas,motor,ruedas,ventanas,puerta)
opcion=0
opc1="apagar"
opc2="inflar"
opc3="cerrar"
opc4="cerrar"
while opcion < 5  :
    print("1.Prender o apagar el motor")
    print("2.Inflar o desinflar ruedas")
    print("3.Abrir o cerrar ventanas")
    print("4.Abrir o cerrar puertas")
    print("5.Salir")
    opcion=int(input("Seleccione la opción que desee: "))
    if opcion==1:
        opc1=(input("Digite (encender/apagar): "))
        carro=Motor()
        separador()
        print("El carro, es un {}, modelo {}, de color {}, tiene {} puertas, usa {}, el motor está {}, tiene las ruedas {}, y sus ventanas están {}.".format(marca,modelo,color,puertas,combustible,carro.encendido_apagado(opc1),ruedas,ventanas))
        print(puerta)
        separador()
    if opcion ==2:
        opc2=input("Digite(inflar/desinflar): ")
        carro=Ruedas()
        separador()
        print("El carro, es un {}, modelo {}, de color {}, tiene {} puertas, usa {}, el motor está {}, tiene las ruedas {}, y sus ventanas están {}.".format(marca,modelo,color,puertas,combustible,carro.encendido_apagado(opc1),carro.inflar_desinflar(opc2),ventanas,))
        print(puerta)
        separador()
    if opcion == 3:
        opc3=input("Digite(abrir/cerrar): ")
        carro=Ventanas()
        separador()
        print("Él carro, es un {}, modelo {}, de color {}, tiene {} puertas, usa {}, el motor está {}, tiene las ruedas {}, y sus ventanas están {}.".format(marca,modelo,color,puertas,combustible,carro.encendido_apagado(opc1),carro.inflar_desinflar(opc2),carro.abrir_cerrar_ventanas(opc3),))
        print(puerta)
        separador()
    if opcion == 4:
        opc4=input("Digita(abrir/cerrar): ")
        carro=Puertas()
        separador()
        print("El carro, es un {}, modelo {}, de color {}, tiene {} puertas, usa {}, el motor está {}, tiene las ruedas {}, y sus ventanas están {}.".format(marca,modelo,color,puertas,combustible,carro.encendido_apagado(opc1),carro.inflar_desinflar(opc2),carro.abrir_cerrar_ventanas(opc3),))
        print(carro.abrir_cerrar_puertas(opc4))
        separador()