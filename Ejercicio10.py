'''Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
'''

numero = 5 

def dia_de_la_semana(numero):
    dia_de_la_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    if 1 <= numero <= 7:
        return dia_de_la_semana[numero - 1]
    
print (dia_de_la_semana(numero))    

                    