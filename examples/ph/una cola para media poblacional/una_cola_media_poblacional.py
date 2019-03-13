import sys
sys.path.insert(0, '../../../lib/')
import ph

"""
En una reunión informativa para una oficina corporativa, el gerente del hotel Embassy Suites en Atlanta, 
reportó que el número promedio de habitaciones alquiladas por noche es de por lo menos 212. Es decir μ ≥ 212. 
Uno de los funcionarios operativos considera que esta cifra puede estar algo subestimada. Una muestra de 150 
noches produce una media de 201.3 habitaciones y una desviación estándar de 45.5 habitaciones. Si estos resultados 
sugieren que el gerente ha “inflado” su reporte, será amonestado severamente. A un nivel de confianza del 1%,
¿cuál es el destino del gerente?
"""

#Hipotesis Nula: La media poblacional >= 212
#Hipotesis Alternativa: La media poblacional < 212

n = 150
media = 201.3
media_nula = 212
s = 45.5
nivel = 0.01

ph.media_poblacional_cola_izquierda(media, media_nula, n, s, nivel)

"""
Valor Z: -2.8801692579977995
Valor crítico: -2.3263478740408408
Regla de decisión:
No se rechaza la hipotesis nula si Z crítica:  -2.3263478740408408  <= Z: -2.8801692579977995
Resultado:
Se rechaza la hipotesis nula
"""