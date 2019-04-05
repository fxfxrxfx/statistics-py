# coding: utf8

import sys
sys.path.insert(0, '../../../lib/')
import ic
"""
The Wall Street Journal describió dos programas de entrenamiento
utilizados por IBM. Doce ejecutivos a quienes se les dio el primer tipo
de entrenamiento obtuvieron un promedio de 73.5 en la prueba de
competencia. Aunque el artículo de noticias no reportó la desviación
estándar para estos 12 empleados, se asume que la varianza en los
puntajes para este grupo fue de 100.2. Quince ejecutivos a quienes se
les administró el segundo programa de entrenamiento obtuvieron un
promedio de 79.8. Se asume una varianza de 121.3 para este segundo
grupo. Hay un intervalo de confianza del 95% para la diferencia en los
puntajes promedio para todos los ejecutivos que ingresaron a estos
programas.
"""

n1 = 12
x1 = 73.5
s1 = 100.2 ** .5

n2 = 15
x2 = 79.8
s2 = 121.3 ** .5

nivel = 0.95

interval = ic.diferencia_medias_muestras_peq_var_desiguales(n1, x1, s1, n2, x2, s2, nivel)

print(interval)