#Funciones
def separador():
    print("-------------------------------------------+")
#Cuenta 
class cuenta:
  #Metodo Constructor
  def __init__(self,numerodecuenta,dni,saldo,interes):
    self.numerodecuenta=numerodecuenta
    self.dni=dni
    self.saldo=saldo
    self.interes=interes  
    self.__mensajeoculto="Gracias por utilizar nuestro banco"
    #Accedentes y Mutadores
  def __saldointeres (self):
    print("Su saldo tiene un interes del", self.interes)
  def get_oculto(self):
    print(self.__mensajeoculto)
  def set_oculto(self):
   mensaje=self.__saldointeres()
    #Metodos
  def actualizarsaldo(self):
      saldo=self.interes*self.saldo
      print("Su saldo con interes es de ",saldo)
  def ingresarsaldo (self):
        ingresarcantidad=float(input("Ingresa la cantidad que desee agregar al saldo "))
        print("Se agrego a su cuenta la cantidad de ",ingresarcantidad)
        saldo=self.saldo+ingresarcantidad
        return saldo
  def retirarsaldo (self):
        retirarcantidad=float(input("Ingrese la catidad que desee retirar "))
        if retirarcantidad<self.saldo:
            print("Se retiro de la cuenta la cantidada de",retirarcantidad)
            saldo=self.saldo-retirarcantidad
            return saldo
        else:
            print("El monto solicitado excede el disponible que tiene en la cuenta ")
            return self.saldo
  def datos (self):
    print("Numero de Cuenta",self.numerodecuenta)
    print("Saldo",self.saldo )
    print("DNI",self.dni)
    print("Interes",self.interes)

#Bloque Principal
numerodecuentaaux=int (input("Numero de Cuenta "))
if numerodecuentaaux >= 100001:
    numerodecuenta = numerodecuentaaux
    saldo=float (input("Ingrese Saldo "))
    dni=int (input("Ingrese su DNI "))
    interes=float (input("Ingrese el Interes "))
    opcion=0 
    ingresarcantidad=0
    retirarcantidad=0
    cuentabancaria=cuenta(numerodecuenta,dni,saldo,interes)
    while opcion <=4:
        print("1. Mostrar el interes del saldo")
        print("2. Agregar el saldo")
        print("3. Retirar el saldo")
        print("4. Mostrar los datos de la cuenta")
        print("5. Salir")
        opcion=int(input("Ingrese el numero de la opcion que desee "))
        if opcion==1:
            cuentabancaria.actualizarsaldo()
            cuentabancaria.set_oculto()
            separador()
            cuentabancaria=cuenta(numerodecuenta,dni,saldo,interes)
        if opcion==2:
            saldo=cuentabancaria.ingresarsaldo()
            cuentabancaria.get_oculto()
            separador()
            cuentabancaria=cuenta(numerodecuenta,dni,saldo,interes)
        if opcion==3:
            saldo=cuentabancaria.retirarsaldo()
            cuentabancaria.get_oculto()
            cuentabancaria=cuenta(numerodecuenta,dni,saldo,interes)
            separador()
        if opcion == 4:
            cuentabancaria.datos()
            separador()
else:
    print("El Numero de cuenta debe ser mayor a 100.001 ")