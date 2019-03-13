import sys
sys.path.insert(0, '../../../lib/')
import ph
"""
Como gerente de compras para una gran empresa de seguros usted debe decidir si actualizar o no los computadores
de la oficina. A usted se le ha dicho que el costo promedio de los computadores es de 2100 USD. Una muestra 
de 64 minoristas revela un precio promedio de 2251 USD, con una desviación estándar de 812 USD. ¿A 
un nivel de significancia del 5% parece que su información es correcta? (tenga en cuenta los 4 pasos al realizar 
la prueba)
"""

media_nula = 2100
n = 64
media = 2251
sd = 812
nivel = 0.05

ph.media_poblacional_dos_colas(media, media_nula, n, sd, nivel)

"""
Valor Z: 1.4876847290640394
Valor crítico: +- 1.9599639845400545
Regla de decisión:
No se rechaza la hipotesis nula si  -1.9599639845400545  <=  1.4876847290640394  <=  1.9599639845400545
Resultado:
No se rechaza la hipotesis nula
"""