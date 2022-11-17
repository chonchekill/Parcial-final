class Coche():
  #  Atributos
  ruedas=4
  cilindraje =1000
  combustible= "Gasolina"
  puertas = 3
  # Metodo
  def desplazamiento(self):
    print("El coche se esta desplazando sobre 4 ruedas")
#Programa Principal

# Generar una instancia de la clase
#Instanciar un objeto
#Declarar un objeto

miVehiculo=Coche()
obj_miCarrito = Coche()
# Acceso al atributo
print("Mi coche tiene ", miVehiculo.ruedas, " de ruedas")
print("Mi coche tiene ", miVehiculo.combustible, " de combustible")
print("Mi coche tiene ", miVehiculo.cilindraje, " de cilindraje")
print("Mi coche tiene ", miVehiculo.puertas, " de puertas")
#forma que un objeto solicita que se ejecute un metodo
miVehiculo.desplazamiento()