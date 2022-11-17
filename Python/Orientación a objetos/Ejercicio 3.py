#Contructor
class cachorro():
    #Metodo contructor
    def __init__(self, p_color ,p_raza):
        self.color= p_color
        self.raza= p_raza

perrito = cachorro("Marron claro", "Golden retriever")
perritovicky=cachorro("Blanco","shitzu")
perritomio=cachorro("Marron","pekipug")
print("Este es un cachorro de la raza {} y es de color {}".format(perrito.raza,perrito.color))
print("Este es un cachorro de la raza {} y es de color {}".format(perritovicky.raza,perritovicky.color))
print("Este es un cachorro de la raza {} y es de color {}".format(perritomio.raza,perritomio.color))