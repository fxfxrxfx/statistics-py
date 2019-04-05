import sys
sys.path.insert(0, '../../../lib/')
import ppp

"""
Para el caso de Hop Scotch tenemos
"""
p = 0                                                   #Hipotesis nula
gL = 15 - 2                                             #Siempre es n - 2
b1 = 1.081316554                                        #Pendiente de la recta de regresión
nivel = 0.05                                            #Mucho nivel rey   
r = 0.968378371                                         #COEFICIENTE DE CORRELACION
Sr = ( ( 1 - r ** 2 ) / ( gL ) ) ** 0.5                 #ERROR ESTANDAR DEL COEFICIENTE DE CORRELACIÓN

ppp.pruebap(r, p, Sr, nivel, gL)


"""
OUTPUT:
Valor t: 13.994917585769151
Valor crítico: +- 2.160368656461013
Regla de decisión:
No se rechaza la hipotesis nula si  -2.160368656461013  <=  13.994917585769151  <=  2.160368656461013
Resultado:
Se rechaza la hipotesis nula
"""