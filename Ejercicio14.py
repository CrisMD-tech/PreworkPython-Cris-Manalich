'''Ejercicio 14: Calculadora de Descuento
Crea un programa que calcule el precio final de un artículo después de aplicar un
descuento del 20%.'''

articulo = 50

porcentaje_descuento = 20

total_a_pagar = articulo - (articulo * porcentaje_descuento / 100)


print(f"total a pagar: {total_a_pagar}")
