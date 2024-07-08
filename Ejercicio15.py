'''Ejercicio 15: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por
ejemplo, 145 minutos serían 2 horas y 25 minutos.'''


def convertir_minutos_en_horas_y_minutos(tiempo):
    horas_resultantes = tiempo // 60
    minutos_resultantes = tiempo % 60
    return horas_resultantes, minutos_resultantes

tiempo = 145

horas, minutos = convertir_minutos_en_horas_y_minutos(tiempo)

print (f"{tiempo} minutos equivalen a {horas} horas y {minutos} minutos")