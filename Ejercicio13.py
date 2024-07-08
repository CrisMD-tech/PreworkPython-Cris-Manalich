'''Ejercicio 13: Verificación de Número Primo
Escribe un programa que determine si un número ingresado por el usuario es primo
o no.
'''

def numero_primo(n):
    if n <= 1:
        return 'No es un numero primo'
    else:
        for x in range (2, n):
            if n % x == 0:
                return 'No es un numero primo'
        
        return 'Es un numero primo'
        

print(numero_primo(52))  
        
        