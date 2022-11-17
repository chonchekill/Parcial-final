class coche():
    ruedas=4
    def despazamiento(self):
        print("El coche se desplaza en en 4 ruedas")
class moto():
    ruedas=2
    def desplazamiento(self):
        print("La moto se desplaza sobre 2 ruedas")
mi_carro=coche()
print("Mi coche tiene", coche.ruedas, "ruedas")
mi_carro.despazamiento()
print("----------------------------------")
mi_moto= moto()
print("Mi moto tiene ",mi_moto.ruedas, "ruedas")
mi_moto.desplazamiento()