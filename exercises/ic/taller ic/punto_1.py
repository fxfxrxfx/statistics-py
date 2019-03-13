import sys
sys.path.insert(0, '../../../lib/')
import ic

"""Un teatro de cine local desea desarrollar un intervalo para estimar las cajas promedio 
de palomitas de maíz que se venden por sala de cine. Si los registros llevados para 70 salas 
revelan un promedio de 54.98 cajas y una desviación estándar de 12.7, calcule e interprete 
un intervalo de confianza del 92% para la media poblacional. """

n = 70
promedio = 54.98
sd = 12.7

intervalo = ic.media_poblacional_muestras_grandes(n, promedio, sd, 0.92)

print(intervalo)