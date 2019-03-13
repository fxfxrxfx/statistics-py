import sys
sys.path.insert(0, '../../../lib/')
import ph

"""
Chuck Cash es el jefe de personal de una empresa. A partir de un breve análisis de los registros de los 
empleados, Chuck considera que los empleados tienen un promedio de más de 31000 USD en sus cuentas de pensiones.
Al tomar como muestra 100 empleados, Chuck encuentra una media de 31366, con s = 1894. Se supone que Chuck desea 
calcular el valor p relacionado con esta prueba de cola a la derecha.
"""

#Hipotesis nula media poblacional <= 31000
#Hipotesis alternativa media poblacional > 31000

n = 100
media_muestral = 31366
s = 1894

media_nula = 31000



ph.valor_p_cola_derecha(media_muestral, media_nula, n, s)

"""
Valor Z:  1.9324181626187962
Probabilidad de Z:  0.9733460429699563
Valor p:  0.026653957030043696
Puede bajar alfa hasta  0.026653957030043696  sin rechazar la hipotesis nula.
"""