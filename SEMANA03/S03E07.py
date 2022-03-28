# En el Congreso se vota la sanción de una ley muy importante.
# Desarrollar un programa que permita ingresar la cantidad de votos a favor y en contra,
# e informe el porcentaje obtenido en cada caso.

favor = int(input("Ingrese la cantidad de votos a favor:"))
contra = int(input("Ingrese la cantidad de votos en contra:"))

total = favor + contra
porc_favor = round((favor / total) * 100, 2)
porc_contra = round((contra / total) * 100, 2)

print("La cantidad de votos es", total, ". De ellos, ", porc_favor, "% son a favor y ", porc_contra, "% en contra.")
