import sys
sys.path.insert(0, '../../../lib/')
import ph
"""
Una encuesta realizada por la Asociación Nacional de Estudiantes Colegiados mostró que los estudiantes 
de las universidades de la nación gastan en promedio más de 75 USD mensuales en mantenimiento. 
Si usted puede hallar evidencias para confirmar esta afirmación, podría utilizarla para solicitar a su 
casa ayuda monetaria adicional. De los 100 estudiantes que tomó de muestra, usted halla una media de 80.23 USD 
con una desviación estándar de 45.67 USD. ¿A un nivel de significancia del 2%, se encuentra justificación para 
la solicitud? (tenga en cuenta los 4 pasos al realizar la prueba).
"""

#Hipotesis alternativa: Media poblacional > 75
#Hipotesis nula: Media poblacional <= 75

media_nula = 75
n = 100
media_muestral = 80.23
s = 45.67
nivel = 0.02

ph.media_poblacional_cola_derecha(media_muestral, media_nula, n, s, nivel)

"""
Valor Z: 1.1451718852638502
Valor crítico: 2.0537489106318225
Regla de decisión:
No se rechaza la hipotesis nula si Z crítica 2.0537489106318225  >= Z  1.1451718852638502
Resultado:
No se rechaza la hipotesis nula

Interpretación: a pesar de su estilo de vida decadente, el estudiante típico no gasta más de US$ 75. Tendrá 
que encontrar otra forma para obtener más dinero de casa. 
"""
