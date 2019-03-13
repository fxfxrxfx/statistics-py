import sys
sys.path.insert(0, '../../../lib/')
import ic

"""
The Wall Street Journal informó los esfuerzos realizados por Nestlé, la compañía de alimentos más grande 
del mundo, para introducir un nuevo producto. La gerencia decidió utilizar el sector de Chicago como mercado 
de prueba. Si más del 30% de la personas expresaban un deseo por el producto, ellos considerarían el comercializarlo 
en un sector más amplio. De las 820 personas a quienes se les practicó la prueba, 215 expresaron una reacción positiva.
¿Un intervalo de confianza del 90% para la proporción de todos los clientes quienes prefieren el producto hace que la 
gerencia continúe con sus planes de comercialización?
"""

n = 820
m = 215
p = m / n
nivel = 0.9

i = ic.proporcion_poblacional(n, p, nivel)

print(i)