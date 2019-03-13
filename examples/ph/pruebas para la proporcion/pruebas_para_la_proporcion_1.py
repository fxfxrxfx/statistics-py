import sys
sys.path.insert(0, '../../../lib/')
import ph

"""
El CEO de una gran firma manufacturera debe garantizar que por lo menos 75% de sus empleados ha concluido un 
curso avanzado de capacitación. De los 1200 empleados seleccionados aleatoriamente, 875 lo han hecho. El CEO 
registra su asistencia para probar esta hipótesis y calcular el valor de p. A un nivel de significancia del 5%, 
¿qué conclusiones incluye usted en su reporte?
"""

#Hipotesis nula proporcion problacional >= 0.75
#Hipotesis alternativa media poblacional < 0.7
#Dos colas

proporcion_planteada = 0.75
n = 1200
m = 875
proporcion = m / n
nivel = 0.05

ph.pruebas_para_proporcion_cola_izquierda(proporcion, n, proporcion_planteada, nivel)
ph.valor_p_proporcion_cola_izquierda(proporcion, n, proporcion_planteada)

"""
Error estandar:  0.0125
Valor de Z -1.6666666666666696
Valor Z: -1.6666666666666696
Valor crítico: -1.6448536269514729
Regla de decisión:
No se rechaza la hipotesis nula si Z crítica:  -1.6448536269514729  <= Z: -1.6666666666666696
Resultado:
Se rechaza la hipotesis nula
Valor Z:  -1.6666666666666696
Probabilidad de Z:  0.047790352272814404
Valor p:  0.047790352272814404
Puede subir alfa hasta  0.047790352272814404  sin rechazar la hipotesis nula.
"""