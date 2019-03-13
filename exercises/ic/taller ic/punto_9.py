import sys
sys.path.insert(0, '../../../lib/')
import ic

"""
El director de su división le pide, como analista de mercadeo recientemente contratado, que estime las ventas 
semanales promedio. Le advierte que debe mantener el error dentro de 100 y mantener un nivel de confianza del 90%. 
¿Cuántas semanas de datos debe recolectar si la desviación estándar es 750?
"""

s = 750

error = 100

nivel = 0.9

n = ic.numero_datos_para_error(s, error, nivel)


print(n)