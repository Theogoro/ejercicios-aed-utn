# Un productor agricola desea saber cuantos quintales de trigo puede producir en su parcela.
# Se pide ingresar el largo y el ancho en metros de la parcela y determinar el rinde sabiendo que en 10 m2 se obtienen 2 quintales.

largo = float(input("Ingrese el largo en metros de la parcela:"))
ancho = float(input("Ingrese el ancho en metros de la parcela:"))

superficie = largo * ancho
quintales = superficie * 2

print("En ", superficie, "mts2 se pueden producir", quintales, " quintales de trigo")
