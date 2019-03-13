import sys
sys.path.insert(0, '../../../lib/')
import ic

"""¿Qué tan grande se requiere que sea una muestra para que proporcione una estimación 
del 90% del número promedio de graduados de las universidades de la nación con un 
error de 2000 estudiantes si una muestra piloto reporta que s = 8659? """


s = 8659
error = 2000
alfa = .90


tam = ic.tamano_muestra(error, s, alfa)

print(tam)