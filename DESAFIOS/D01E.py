# Además, el desafío incluye al final una quinta consigna o pregunta adicional, en la cual se le pedirá hacer un programa que haga el proceso inverso: 
# deberá tomar tres datos, que serán el valor en horas, el valor en minutos y el valor en segundos transcurridos desde un evento dado,
# y su programa deberá calcular la cantidad total de segundos a partir de esos datos. 
# Por ejemplo, si los datos ingresados fuesen: horas = 4, minutos = 36 y segundos = 8 entonces el resultado a obtener es que la cantidad total de segundos es 16568.

horas = int(input("Ingrese la cantidad de horas: ")) * 3600
minutos = int(input("Ingrese la cantidad de minutos: ")) * 60
segundos = int(input("Ingrese la cantidad de segundos: "))

print("Transcurrieron " + str(horas + minutos + segundos) + " segundos")