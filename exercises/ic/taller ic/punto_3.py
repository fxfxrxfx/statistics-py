import sys
sys.path.insert(0, '../../../lib/')
import ic

"""Greenleaf Lawn Care descubre que el costo promedio de adornar los jardines de 20 casas del área 
es de 2365, con s = 983. Al nivel de confianza del 99%, ¿Qué costo promedio estimaría usted para adornar 
los jardines de todas las casas del área"""

n = 20  #Pequeño
s = 983
media = 2365    
alfa = 0.99

#S (Poblacional) => Desconocida => Usamos t

intervalo = ic.media_poblacional_muestras_pequenas(n, media, s, alfa)


print(intervalo)