import sys
sys.path.insert(0, '../../../lib/')
import ic
"""Si de los 1098 turistas norteamericanos 896 recimiendan su viaje a Irlanda a sus amigos, 
¿qué porcentaje de todos los turistas norteamericanos harían lo mismo con un nivel del 99% de confianza?"""

n = 1098
m = 896
alfa = .99

p = m / n


intervalo = ic.proporcion_poblacional(n, p, alfa)

print(intervalo)