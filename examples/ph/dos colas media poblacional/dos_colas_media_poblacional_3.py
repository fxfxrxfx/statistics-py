import sys
sys.path.insert(0, '../../../lib/')
import ph

"""
Debido al tiempo excesivo que se gasta hacia el sitio de trabajo, la oficina donde usted trabaja en el centro 
de Chicago está considerando espaciar las horas de trabajo para sus empleados. El gerente considera que los 
empleados gastan un promedio de 50 minutos para llegar al trabajo. Setenta empleados se toman en promedio 47.2 
minutos con una desviación estándar de 18.9 minutos. Fije α en 1% y pruebe la hipótesis. (tenga en cuenta los 4 pasos al 
realizar la prueba).
"""

media_nula = 50

n = 70
media_muestral = 47.2
s = 18.9

significancia = 0.01

ph.media_poblacional_dos_colas(media_muestral, media_nula, n, s, significancia)

"""
Valor Z: -1.2394963356060367
Valor crítico: +- 2.575829303548901
Regla de decisión:
No se rechaza la hipotesis nula si  -2.575829303548901  <=  -1.2394963356060367  <=  2.575829303548901
Resultado:
No se rechaza la hipotesis nula
"""