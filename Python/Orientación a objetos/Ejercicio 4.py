
class C_Rectangulo:
  def __init__(self,p_ancho,p_alto):
     self.at_ancho=p_ancho
     self.at_alto=p_alto

  def m_area(self):
       area=self.at_alto*self.at_ancho
       return area 

  def m_perimetro(self):
         perimetro=(self.at_alto*2)+(self.at_ancho*2)
         return perimetro

r1=C_Rectangulo(4,2)        
area=r1.m_area()
perimetro=r1.m_perimetro()
print("El area es:",area)
print("El perimetro es:",perimetro)

p_ancho = int(input("Ancho: "))
p_alto = int(input("Alto: "))

obj_rect2=C_Rectangulo(p_ancho,p_alto)

print("El area es:",+obj_rect2.m_area())
print("El perimetro es:",+obj_rect2.m_perimetro())