#EJERCICIO FACTORIAL
x=1
m=1
z=1
com=0
total=1

fac_num1=int(input("Digite el primer número ")) #n
fac_num2=int(input("Digite el segundo número ")) #m
fac_res = (fac_num2-fac_num1)
for x in range(x ,fac_num1):
  r_fnum1= fac_num1 * x
  fac_num1 = r_fnum1
  

for m in range(m ,fac_num2):
  r_fnum2 = fac_num2 * m
  fac_num2 = r_fnum2 
  

#print(str(r_fnum1))
#print(str(r_fnum2))

#print(fac_res)

for z in range(z, fac_res):
  r_fnum3 =  fac_res * z
  fac_res = r_fnum3

com= fac_num2 / (fac_num1*fac_res)
print("La combinatoria de los números es ",com)