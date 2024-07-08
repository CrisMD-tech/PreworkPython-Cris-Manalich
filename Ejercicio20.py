'''Ejercicio 20: Suma de Números en una Lista
Crea un programa que sume todos los números en una lista ingresada por el
usuario.'''

def lista(numeros):
    contador = 0
    for numero in numeros:
        contador += numero
    return contador

total = (lista([1,2,3,13,15,84,625]))

print(total)
    