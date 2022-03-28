# Calcular el descuento y el monto a pagar por un medicamento cualquiera en una farmacia (cargar por teclado el precio de ese medicamento)
# sabiendo que todos los medicamentos tienen un descuento del 35%.Mostrar el precio actual, el monto del descuento y el monto final a pagar.
precio = float(input("Ingrese el precio de la medicina:"))
monto_desc = precio * 0.35
monto_final = precio - monto_desc

print("El precio del producto es: $", precio)
print("El monto de descuento es: $", monto_desc)
print("El monto final es: $", monto_final)

