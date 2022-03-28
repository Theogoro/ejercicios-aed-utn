# Desarrollar un programa que cargue por teclado los coeficientes a, b y c de un polinomio de segundo grado,
# y calcule y muestre el valor del polinomio en el punto x (cargando también x por teclado).
# Además, para el mismo polinomio, calcule y muestre el valor del discriminante de la fórmula para el cálculo de las raíces de la ecuación.

a = float(input("Ingrese el valor del coeficiente a:"))
b = float(input("Ingrese el valor del coeficiente b:"))
c = float(input("Ingrese el valor del coeficiente c:"))
x = float(input("Ingrese el valor de x:"))

valor_fn = a * x**2 + b * x + c
discriminante = b**2 - 4 * a * c

print("El valor de la función en el punto x=", x, "es:", valor_fn)
print("El valor del discriminante es:", discriminante)
