#Funcion
def separador():
    print("--------------------------------------------")
#Clase
class cafetera():
    #Metodo constructor
    def __init__(self,capacidad_max,capacidad_actual):
        self.capacidad_max=capacidad_max
        self.capacidad_actual=capacidad_actual
        self.__faltaporllenar=capacidad_max-capacidad_actual
        # Accedentes y mutadores
    def __mensajeoculto (self):
        print ("Disfruta del nuestro café colombiano")
    def set_oculto(self):
        self.mensaje=self.__mensajeoculto()
    def get_oculto(self):
        print("La cafetera falta por llenar ",self.__faltaporllenar,"(c^3)")
    #Metodos
    def llenar_cafetera(self):
        capacidad_actual=self.capacidad_max
        print("La cafetera esta al máximo ",self.capacidad_max,"(c^3)")
        return capacidad_actual
    def servir_taza(self):
        cantidad_taza=int(input("Índica la cantidad a servir el en la taza (c^3)= "))
        if self.capacidad_actual >= cantidad_taza:
            capacidad_actual1=self.capacidad_actual-cantidad_taza
            print("Se sirvió un taza de ",cantidad_taza,"(c^3)")
            cafetera1.set_oculto()
            return capacidad_actual1
        else:
            print("No hay cafe en la cafetera")
            return self.capacidad_actual
    def vaciar_cafetera(self):
        capacidad_actual=0
        print("La cafetera está vacia")
        return capacidad_actual
    def agregar_cafe(self):
        agregar_cafe=int(input("Ingrese el valor de cafe que se agrega a la cafetera(c^3)= "))
        capacidad_actual=self.capacidad_actual+agregar_cafe
        print("Se agrego ",agregar_cafe,"(c^3) de cafe")
        return capacidad_actual
#Bloque principal
opcion=0
capacidad_max=1000
capacidad_actual=0
cafetera1=cafetera(capacidad_max,capacidad_actual)
while opcion <= 4:
    separador()
    print("1. Llenar cafetera")
    print("2. Servir taza")
    print("3. Vaciar cafetera")
    print("4. Agregar una cantidad de café a la cafetera")
    print("5. Salir")
    opc=int(input("Elije la opcion: "))
    if opc == 1:
        capacidad_actual=(cafetera1.llenar_cafetera())
        cafetera1=cafetera(capacidad_max,capacidad_actual)
    if opc == 2:
        capacidad_actual=(cafetera1.servir_taza())
        
        cafetera1=cafetera(capacidad_max,capacidad_actual)
    if opc == 3:
        print(cafetera1.vaciar_cafetera())
        cafetera1=cafetera(capacidad_max,capacidad_actual)
    if opc == 4:
        capacidad_actual=cafetera1.agregar_cafe()
        if capacidad_actual>capacidad_max:
            capacidad_max=capacidad_actual
        cafetera1=cafetera(capacidad_max,capacidad_actual)
        cafetera1.get_oculto()