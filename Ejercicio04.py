'''Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario.
'''

def contador_vocales(palabra):
    vocales = 'aeiouAEIOU'
    
    return ([letra for letra in palabra if letra in vocales])

palabra = 'ordenador'

print(len(contador_vocales(palabra)))


