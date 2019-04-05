import sys
sys.path.insert(0, '../../../lib/')
import ppp

"""
Para el caso de Hop Scotch tenemos
ERROR ESTANDAR => 0.906780212
SUMA CUADRADOS DE X => 137.7333333
"""

ERROR_ESTANDAR = 0.906780212
SUMA_CUADRADOS_X = 137.7333333

Sb1 = ERROR_ESTANDAR / SUMA_CUADRADOS_X ** (0.5)
Beta1 = 0               #Hipotesis nula
gL = 15 - 2             #Siempre es n - 2
b1 = 1.081316554        #Pendiente de la recta de regresión
nivel = 0.05            #Mucho nivel rey   
print(Sb1)

t = ppp.pB1( Sb1, b1, Beta1, nivel, gL )


"""
OUTPUT:
0.07726494597254674
Valor t: 13.99491762259442
Valor crítico: +- 2.160368656461013
Regla de decisión:
No se rechaza la hipotesis nula si  -2.160368656461013  <=  13.99491762259442  <=  2.160368656461013
Resultado:
Se rechaza la hipotesis nula

Debido a que t = 13.995, la hipótesis nula de que β1 = 0 se rechaza. Al nivel del 5% parece existir 
una relación entre pasajeros y publicidad.
"""

print("IC", ppp.icB1(b1, t, Sb1))

"""
OUTPUT:
IC [0.9143957864777564, 1.2482373215222435]
Esto significa que se puede estar un 95% seguro de que 
el coeficiente de regresión para toda la población de todos los valores de X, 
está entre 0.913 y 1.247. 
"""