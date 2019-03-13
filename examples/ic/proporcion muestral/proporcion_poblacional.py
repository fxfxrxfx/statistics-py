import sys
sys.path.insert(0, '../../../lib/')
import ic

"""
Ejemplo 7.7
El gerente de una estación de televisión debe determinar en la ciudad que porcentaje de casas tiene más de un 
televisor. Una muestra aleatoria de 500 casas revela que 275 tienen dos o más televisores. ¿Cuál es el intervalo 
de confianza del 90% para estimar la proporción de todas las casas que tienen dos o más televisores?
"""

n = 500
m = 275
p = m / n
nivel = 0.90

intervalo = ic.proporcion_poblacional(n, p, nivel)

print(intervalo)