# Desarrolle un programa o script Python que permita cargar por teclado un número entero que representa la  cantidad de segundos que pasaron desde un evento dado.  
# El programa debe convertir esa cantidad de segundos  a la cantidad de horas, minutos y segundos que transcurrieron. 
# Por ejemplo, si la cantidad de segundos  ingresada es 4452 deberá mostrar un mensaje que informe que el tiempo transcurrido fue de 1 hora, 14 minutos  y 12 segundos.

segundos = int(input("Ingrese la cantidad de segundos: "))

sec_en_hora = 3600
sec_en_minutos = 60

horas = segundos // sec_en_hora

segundos = segundos % sec_en_hora

minutos = segundos // sec_en_minutos

segundos = segundos % sec_en_minutos

print(horas, ":", minutos, ":", segundos)