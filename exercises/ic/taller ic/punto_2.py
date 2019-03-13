import sys
sys.path.insert(0, '../../../lib/')
import ic

"""Una muestra de 121 llamadas al número 900 que usted maneja tiene una duración  promedio de 16.6 minutos
y una desviación estándar de 3.63 minutos. Usted pretende discontinuar el servicio a menos que
la duración promedio sea superior a 18 minutos. En un nivel de confianza del 95%, 
¿cuál es su decisión?  """

n = 121
promedio = 16.6
alfa = 0.95
sd = 3.63

intervalo = ic.media_poblacional_muestras_grandes(n, promedio, sd, alfa)

print(intervalo)