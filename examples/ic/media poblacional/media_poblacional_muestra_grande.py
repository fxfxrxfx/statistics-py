import sys
sys.path.insert(0, '../../../lib/')
import ic

"""Un promotor inmobiliario desea construir un centro comercial. Él puede estimar el
área donde desea construir el ingreso promedio por familia como indicador de ventas esperadas.
Una muestra de n = 100 familias da una media muestral de 35500. Se asume que al desviación estándar 
poblacional es s = 7200. Se asume un intervalo de confianza del 95%."""

media = 35500
sd = 7200
n = 100
alfa = .95

intervalo = ic.media_poblacional_muestras_grandes(n, media, sd, alfa)
print(intervalo)