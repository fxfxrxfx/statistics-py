import sys
sys.path.insert(0, '../../lib/')
from dists import xi2

"""
Chris Columbus, director de mercadeo de Seven Seas, tiene la responsabilidad de controlar el nivel de existencias 
para cuatro tipos de botes vendidos por su firma. En el pasado ha ordenado nuevos botes bajo la premisa de que 
los cuatro tipos son igualmente populares y la demanda de cada tipo es la misma. Sin embargo, recientemente las
existencias se han vuelto más difíciles de controlar, y Chris considera que debería probar su hipótesis respecto
a una demanda uniforme. Sus hipótesis son:
Ho: la demanda es uniforme para los cuatro tipos de datos. 
HA: la demanda no es uniforme para los cuatro tipos de 
datos.
"""

statistic = xi2([15, 11, 10, 12], [12, 12, 12, 12]).statistic
valorCritico = input("Busque el balor crítico en la tabla, y continúe")
print("REGLA DE DECISIÓN: No rechazar si {0} <=  {1}. RECHAZAR SI {0} > {1}".format(statistic, valorCritico))