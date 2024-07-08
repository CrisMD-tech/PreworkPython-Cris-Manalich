'''Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta'''

Ensalada = 10
Carne = 15
Pescado = 18
Postre = 7

Cuenta = [Ensalada, Carne, Pescado, Postre]

total = 0

for plato in Cuenta:
    total += plato
    
porcentaje_propina = 15 

total_neto = total + (total * porcentaje_propina / 100)   
    
print(f"total_neto: {total_neto}")    
