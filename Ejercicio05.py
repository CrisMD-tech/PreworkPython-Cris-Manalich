'''Ejercicio 5: Suma de Números Pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
'''

Suma = 0

for n in range(1, 101):
    if n % 2 == 0:
        Suma += n
        
print (Suma)        