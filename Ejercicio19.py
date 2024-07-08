'''Ejercicio 19: Verificación de Año Bisiesto
Escribe un programa que determine si un año ingresado por el usuario es bisiesto o
no.'''

def bisiesto(año):
    if (año % 4 == 0 and año != 0) or (año % 400 == 0):
        return "es bisiesto"
    else:
        return "no es bisiesto"
    
año = 2024

print (f"{año} {bisiesto(año)}")
    
    
    

