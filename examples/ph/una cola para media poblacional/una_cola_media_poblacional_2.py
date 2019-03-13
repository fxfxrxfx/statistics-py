import sys
sys.path.insert(0, '../../../lib/')
import ph

"""
Durante los últimos meses Raynor & Sons ha publicitado ampliamente su negocio de suministros electrónicos. 
El señor Raynor espera que el resultado haya sido incrementar las ventas en promedio semanales por encima de 7880 USD
que la compañía experimentó en el pasado. Una muestra de 36 semanas da una media de 8023 USD con una desviación 
estándar de 1733 USD. A un nivel de significancia del 1%, ¿parece que la publicidad a producido efecto? 
(tenga en cuenta los 4 pasos al realizar la prueba).
"""

#Hipotesis alternativa: Media poblacional > 7800
#Hipotesis nula: Media poblacional <= 7800

media_nula = 75
n = 36
media_muestral = 8023
s = 1733
nivel = 0.01

ph.media_poblacional_cola_derecha(media_muestral, media_nula, n, s, nivel)

"""
Valor Z: 27.517599538372767
Valor crítico: 2.3263478740408408
Regla de decisión:
No se rechaza la hipotesis nula si Z crítica 2.3263478740408408  >= Z  27.517599538372767
Resultado:
Se rechaza la hipotesis nula
"""