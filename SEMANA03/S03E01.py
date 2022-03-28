# Leer dos números y calcular:
#
# La suma de sus cuadrados.
# El promedio de sus cubos.

num1 = int(input("Ingrese el 1er numero:"))
num2 = int(input("Ingrese el 2do numero:"))

suma_cuadrados = num1**2 + num2**2
promedio_cubos = (num1**3 + num2**3) / 2

print("La suma de los cuadrados es", suma_cuadrados)
print("El promedio de los cubos es", promedio_cubos)
