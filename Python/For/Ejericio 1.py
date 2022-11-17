suma_de_estudiantes_noche=0
suma_de_estudiantes_tarde=0
suma_de_estudiantes_mañana=0
print("turno de la mañana")
for x in range (5):
    edad_de_los_estudiantes_mañana=int(input("Ingrese la edad de los estudiantes de la mañana ="))
    suma_de_estudiantes_mañana=suma_de_estudiantes_mañana+edad_de_los_estudiantes_mañana
promedio_de_estudiantes_mañana=suma_de_estudiantes_mañana/5
print("Promedio de estudiantes mañana = ", promedio_de_estudiantes_mañana)
print("Turno tarde")
for t in range (6):
    edad_de_estudiantes_tarde=int(input("Ingrese la edad de los estudiantes de la tarde ="))
    suma_de_estudiantes_tarde=suma_de_estudiantes_tarde+edad_de_estudiantes_tarde
promedio_estudiantes_tarde=suma_de_estudiantes_tarde/6
print("Promedio de estudiantes tarde = ",promedio_estudiantes_tarde)
print("turni de noche = ")
for y in range (11):
    edad_de_estudiantes_noche=int(input("Ingrese la edad de los estudiantes de la noche = "))
    suma_de_estudiantes_noche=suma_de_estudiantes_noche+edad_de_estudiantes_noche
promedio_de_estudiante_noche=suma_de_estudiantes_noche/11
print("Promedio de estudiantes noche = ", promedio_de_estudiante_noche)
if promedio_de_estudiantes_mañana>promedio_estudiantes_tarde and promedio_de_estudiantes_mañana>promedio_de_estudiante_noche:
    print("El promedio mas grande son de los estudiantes de la mañana")
else:
    if promedio_estudiantes_tarde>promedio_de_estudiante_noche:
        print("El promedio mas grande es el de la tarde")
    else:
        print("Promedio mas grande es el de la noche")


