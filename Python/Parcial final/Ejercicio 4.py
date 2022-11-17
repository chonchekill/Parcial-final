#Clase 
class Linea :
    #metodo constructor
    def __init__(self,punto_A,punto_B):
        self.punto_A = punto_A
        self.punto_B = punto_B
    #Metodos
    def Moverderecha(self,derecha):
        self.punto_A=self.punto_A + derecha
        return self.punto_A
    def Moverizquierda(self,izquierda):
        self.punto_A=self.punto_A - izquierda
        return self.punto_A
    def Moverarriba(self,arriba):
        self.punto_B=self.punto_B + arriba
        return self.punto_B
    def Moverabajo(self,abajo):
        self.punto_B=self.punto_B - abajo
        return self.punto_B
    def Mostrar_vector(self):
        print("({},{})".format(self.punto_A,self.punto_B))
#Bloque principal 
punto_A=float(input("Introduzca el punto x= "))
punto_B=float(input("Introduzca el punto y= "))
vector=Linea(punto_A, punto_B)
opcion=0
while opcion < 6:
    print("1. Mover el vector hacia la derecha")
    print("2. Mover el vector hacia la izquierda")
    print("3. Mover el vector hacia arriba")
    print("4. Mover el vector hacia abajo")
    print("5. Mostrar los resultados")
    print("6. Salir")
    opcion=int(input("Introduzca la opcion que desee= "))
    if opcion == 1:
        derecha=float(input("Mover el vector a la derecha="))
        vector.Moverderecha(derecha)
    if opcion == 2:
        izquierda=float(input("Mover el vector a la izquierda= "))
        vector.Moverizquierda(izquierda)
    if opcion == 3:
        arriba=float(input("Mover el vector arriba= "))
        vector.Moverarriba(arriba)
    if opcion== 4:
        abajo=float(input("Mover el vector abajo= "))
        vector.Moverabajo(abajo)
    if opcion == 5:
        vector.Mostrar_vector()