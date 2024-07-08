'''Ejercicio 6: Verificación de Palíndromo
Crea un programa que verifique si una palabra ingresada por el usuario es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
'''

palabra = "rallar"

inversa = palabra[::-1]

if palabra == inversa:
    print("es palindromo")
    
else:    

    print ("no es palindromo")

