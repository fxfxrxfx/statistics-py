import sys
sys.path.insert(0, '../../../lib/')
import ic

"""Gerry Gerber, CPA, acaba de registrar las declaraciones de impuestos de sus clientes. 
Desea estimar la cantidad promedio que deben al servicio de renta interna. De los 50 clientes 
que seleccionó en su muestra, la cantidad promedio que se adeudaba era de 652.68. La desviación 
estándar de todos los clientes σ es desconocida, la desviación estándar de la muestra es s = 217.43.
Se desea un nivel de confianza del 99%"""

n = 50
promedio = 652.68
sd = 217.43
alfa = 0.99

intervalo = ic.media_poblacional_muestras_grandes(n, promedio, sd, alfa)

print(intervalo)