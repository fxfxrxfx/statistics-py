import sys
sys.path.insert(0, '../../../lib/')
import ph
"""
La gerencia de First Bank of America está planeando basar los cargos para las cuentas corrientes en el saldo 
diario promedio. El gerente de cunetas preferenciales desea probar la hipótesis de que las cuentas tienen un 
promedio de 312. Se selecciona una muestra de 200 cuentas, dando una media de 298.10 con s = 97.30.
Para minimizar la probabilidad de un error tipo I, se selecciona un valor α de 1%. (tenga en cuenta los 4 pasos al realizar 
la prueba).
"""

media_nula = 312
n = 200
media_muestral = 298.10
s = 97.30
nivel = 0.01

ph.media_poblacional_dos_colas(media_muestral, media_nula, n, s, nivel)

"""
Valor Z: -2.0203050891044185
Valor crítico: +- 2.575829303548901
Regla de decisión:
No se rechaza la hipotesis nula si  -2.575829303548901  <=  -2.0203050891044185  <=  2.575829303548901
Resultado:
No se rechaza la hipotesis nula
"""