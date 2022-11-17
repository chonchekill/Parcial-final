'''Crea una clase Racional que permita trabajar con números racionales (fracciones).
Incluye los siguientes métodos: constructores (por defecto y parametrizado), accedentes,
leer(), suma, resta, multiplicación, división, comparaciones, copia() y print().'''
class racional():
  #Metodo Constructor
  def __init__(self,num1,num2,num3,num4):
    self.num1=num1
    self.num2=num2
    self.num3=num3
    self.num4=num4

    
    #Metodos
  def suma(self):
   if self.num3 == self.num4:
        resn = self.num3
   else:
        resn = num3 * num4
   total=self.num1+self.num2
   print("El resultado de la suma de  fracciones es",total,"/",resn)

  def resta(self):
   if self.num3 == self.num4:
        resn = self.num3
   else:
        resn = num3 * num4
   total=self.num1-self.num2
   print("El resultado de la resta de fracciones es",total,"/",resn)

  def multi(self):
   total=self.num1*self.num2
   resn=self.num3*self.num4
   print("El resultado de la multiplicación de fracciones es",total,"/",resn)

  def div(self):
   total=self.num1*self.num4
   resn=self.num2*self.num3
   print("El resultado de la división de fracciones es",total,"/",resn)


#Bloque Principal
num1=int (input("Ingrese el primer numerador: "))
num3=int (input("Ingrese el primer denominador "))
num2=int (input("Ingrese el segundo numerador "))
num4=int (input("Ingrese el segundo denominador "))
    
opcion=0 
resn =0
resd = 0
total=0
frac = racional(num1,num2,num3,num4)


while opcion <=4:
  print("1. Suma")
  print("2. Resta")
  print("3. Multiplicación")
  print("4. División")
  print("5. Salir")
  opcion= int (input("Ingrese el numero de la opcion que desee "))
  if opcion==1:
    frac.suma()
    frac=racional(num1,num2,num3,num4)     
  if opcion==2:
    frac.resta()
    frac=racional(num1,num2,num3,num4) 
  if opcion==3:
    frac.multi()
    frac=racional(num1,num2,num3,num4) 
  if opcion==4:
    frac.div()
    frac=racional(num1,num2,num3,num4) 
else:
    print("La opción no es correcta")