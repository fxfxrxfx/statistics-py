import sys
sys.path.insert(0, '../../../lib/')
import ph

"""
Según The Wall Street Journal muchas compañías de ropa deportiva están tratando de comercializar sus productos 
entre los más jóvenes. El artículo sugirió que la edad promedio de los consumidores había caído por debajo del 
grupo de edad 34.4 años que caracterizó los comienzos de la década. Si una muestra de 1000 clientes reporta una 
media de 33.2 años y una desviación estándar de 9.4, ¿qué se concluye a un nivel de significancia del 4%?. 
(tenga en cuenta los 4 pasos al realizar la prueba).
"""

#Hipotesis alternativa: Media poblacional < 34.4
#Hipotesis nula: Media poblacional >= 34.4

media_nula = 34.4
n = 1000
media_muestral = 33.2
s = 9.4
nivel = 0.04

ph.media_poblacional_cola_izquierda(media_muestral, media_nula, n, s, nivel)

"""
Valor Z: -4.036950204470257
Valor crítico: -1.75068607125217
Regla de decisión:
No se rechaza la hipotesis nula si Z crítica:  -1.75068607125217  <= Z: -4.036950204470257
Resultado:
Se rechaza la hipotesis nula
"""