#Definición de variables 
p=0
t=0
f=0
m=0
n=0
d=0
z=0
salario_total_hombre=0
salario_total_mujeres=0
total_sueldo_pagado=0
total_horas_trabajadas_hombres=0
total_horas_trabajadas_mujeres=0
total_horas_extras_hombres=0
total_horas_extras_mujeres=0
salario_ind1=0
salario_ind_m1=0
salario_ind_m=0
salario_ind=0

opcion=0
sexo_f=1
sexo_m=1
numero_empleados=1

valor_hora=float(input("Ingrese el valor por hora= "))#Dato entrada
while opcion <= 3:
    print("1. Ingresar un nuevo empleado masculino")
    print("2. Ingresar un nuevo empleado femenino")
    print("3. Estadisticas")
    print("4. Salir")
    opcion=int(input("Eligir una opcion= "))#Dato de entrada
    if opcion==1:
        nombre_empleado=input("Ingrese el nombre del empleado: ")#Datos de entrada
        horas_trabajadas=int(input("Ingrese las horas trabajadas= "))#Datos de entrada
        #Proceso de cantidad de hombres
        sexo_m=f+1
        f=sexo_m
        #Proceso de total de horas trabajadas hombres
        total_horas_trabajadas_hombres=horas_trabajadas+t
        t=total_horas_trabajadas_hombres
        
        #proceso de salario
        if horas_trabajadas<=40:
            salario_ind=horas_trabajadas*valor_hora
            print("Es salario de ", nombre_empleado ,"es de= ", salario_ind)
        else:
            if horas_trabajadas>40:
                salario_ind=valor_hora*40
                horas_extras=horas_trabajadas-40
                # Numero de horas extras
                total_horas_extras_hombres=m+horas_extras
                m=total_horas_extras_hombres
                salario_ind=salario_ind+(horas_extras*(valor_hora*1.8))
        salario_mensual=salario_ind*4 #Salario mensual
        if salario_mensual >=1800000 and salario_mensual<=2300000:
            salario_ind=salario_ind*0.8
            print("Es salario de ", nombre_empleado ,"es de= ", salario_ind)
        if salario_mensual >2300000:
            salario_ind=salario_ind*0.3
            print("Es salario de ", nombre_empleado ,"es de= ", salario_ind)
        #Salario total de hombres
        salario_total_hombre=n+salario_ind
        n=salario_total_hombre
        #se halla el salari máximo
    if(salario_ind1 <= salario_ind):
        max_sal_h = salario_ind
        #Se halla el salario minimo
    else:
        min_sal_h=salario_ind1
    salario_ind1=salario_ind    
    if opcion==2:
        nombre_empleado=input("Ingrese el nombre de la empleada: ")#Datos de entrada
        horas_trabajadas=int(input("Ingrese las horas trabajadas= "))#Datos de entrada
        sexo_f=sexo_f
        #Proceso de total de horas trabajadas hombres
        total_horas_trabajadas_mujeres=horas_trabajadas+p
        p=total_horas_trabajadas_mujeres
        if horas_trabajadas<=40:
            salario_ind_m=horas_trabajadas*valor_hora
            print("Es salario de ", nombre_empleado ,"es de= ", salario_ind_m)
        else:
            if horas_trabajadas>40:
                salario_ind_m=valor_hora*40
                horas_extras_m=horas_trabajadas-40
                # Numero de horas extras
                total_horas_extras_mujeres=d+horas_extras_m
                d=total_horas_extras_mujeres
                salario_ind_m=salario_ind_m+(horas_extras_m*(valor_hora*1.8))
        salario_mensual_m=salario_ind_m*4 #Salario mensual
        if salario_mensual_m >=1800000 and salario_mensual_m<=2300000:
            salario_ind_m=salario_ind_m*0.8
            print("Es salario de ", nombre_empleado ,"es de= ", salario_ind_m)
        if salario_mensual_m >2300000:
            salario_ind_m=salario_ind_m*0.3
            print("Es salario de ", nombre_empleado ,"es de= ", salario_ind_m)
        #Salario total de mujeres
      
        salario_total_mujeres=z+salario_ind_m
        z=salario_total_mujeres
        # se halla el salario máximo
    if(salario_ind_m1 <= salario_ind_m):
        max_sal_m = salario_ind_m
        #Se halla el salario minimo
    else:
        min_sal_m=salario_ind_m1
    salario_ind_m1=salario_ind_m
    if opcion ==3:
        print("Estadisticas")
        print("Salario total de hombres= ", salario_total_hombre)
        print("Salario total de mujeres= ",salario_total_mujeres)
        total_sueldo_pagado=salario_total_hombre+salario_total_mujeres
        print("Sueldo total pagado= ", total_sueldo_pagado)
        print("Maximo sueldo pagado a hombres",max_sal_h)
        print("Maximo sueldo pagado a mujeres",max_sal_m )
        print("Minimo sueldo pagado a hombres",min_sal_h)
        print("Minimo sueldo pagado a mujeres",min_sal_m )
        sueldo_promedio_hombres=salario_total_hombre/sexo_m
        print("Sueldo promedio de hombres= ",sueldo_promedio_hombres)
        sueldo_promedio_mujeres=salario_total_mujeres/sexo_f
        print("Sueldo promedio de mujeres= ",sueldo_promedio_mujeres)
        sueldo_promedio_pagado=total_sueldo_pagado/(sexo_f+sexo_m)
        print("Sueldo promedio pagado es= ",sueldo_promedio_pagado)
        print("Total de horas trabajadas hombres",total_horas_trabajadas_hombres)
        print("Total de horas trabajadas mujeres",total_horas_trabajadas_mujeres)
        total_horas_trabajadas=total_horas_trabajadas_hombres+total_horas_trabajadas_mujeres
        print("Total de horas trabajadas= ",total_horas_trabajadas)
        print("Total horas extras hombres es= ",total_horas_extras_hombres)
        print("Total horas extras mujeres es= ",total_horas_extras_mujeres)
        total_de_horas_extras=total_horas_extras_hombres+total_horas_extras_mujeres
        print("Total de horas extras trabajadas= ",total_de_horas_extras)
else:
    quit