import sys
sys.path.insert(0, '../../../lib/')
import ic

"""
La Asociación de Finanzas Estudiantiles en Faber Collage está planeando una “Feria primaveral” en la cual intentan 
vender camisetas con su logo. El tesorero desea un estimado de la proporción de estudiantes que comprarán una camiseta. 
El estimado debe proporcionar un nivel de confianza del 90% y el error no debe exceder del 3%. ¿Qué tan grande debe 
tomarse la muestra? 
"""

nivel = .90

error = 0.03

p = 0.5 #No nos dan una proporción

n = ic.numero_datos_para_error_proporcion(p, error, nivel)

print(n)