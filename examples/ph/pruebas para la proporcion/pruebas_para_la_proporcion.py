import sys
sys.path.insert(0, '../../../lib/')
import ph

"""
Como director de operaciones de mercadeo para una gran cadena minorista, usted considera que el 60% de los 
clientes de la firma se han graduado de la universidad. Usted intenta establecer una importante política 
respecto a la estructura de precios sobre esta proporción. Una muestra de 800 clientes revela que 492 clientes 
tienen grados universitarios. A un nivel del 5%, ¿qué puede concluir sobre la proporción de todos los clientes 
que se han graduado de la universidad?
"""

#Hipotesis nula proporcion problacional = 0.6
#Hipotesis alternativa media poblacional != 0.6
#Dos colas

proporcion_planteada = 0.6
n = 800
m = 492
proporcion = m / n
nivel = 0.05

ph.pruebas_para_proporcion_dos_colas(proporcion, n, proporcion_planteada, nivel)
#ph.valor_p_para_proporcion_dos_colas(proporcion, n, proporcion_planteada)

"""
Error estandar:  0.017320508075688773
Valor de Z 0.8660254037844394
Valor Z: 0.8660254037844394
Valor crítico: +- 1.9599639845400545
Regla de decisión:
No se rechaza la hipotesis nula si  -1.9599639845400545  <=  0.8660254037844394  <=  1.9599639845400545
Resultado:
No se rechaza la hipotesis nula

Valor Z:  0.8660254037844394
Probabilidad de Z:  0.8067618846143838
Valor p:  0.3864762307712324
Puede bajar alfa hasta  0.3864762307712324  sin rechazar la hipotesis nula.
"""