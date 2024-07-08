'''Ejercicio 16: Contador de Números Pares e Impares
Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario.
'''


def contador_de_numeros_pares_e_impares(numeros):
    cantidad_pares = sum(1 for numero in numeros if numero % 2 == 0)
    cantidad_impares = len(numeros) - cantidad_pares
    return cantidad_pares, cantidad_impares
    
pares, impares = contador_de_numeros_pares_e_impares([1,2,3,4,5,6,7,8,9])

   
print (f" tiene {pares} numeros pares y {impares} impares") 
 