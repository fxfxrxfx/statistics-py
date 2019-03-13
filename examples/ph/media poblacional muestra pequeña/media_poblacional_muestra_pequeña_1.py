import sys
sys.path.insert(0, '../../../lib/')
import ph

"""
The American Kennel Club (AKC) reportó en su publicación Estadounidenses Propietarios de Perros (abril 1997) 
que los perros cocker spaniels de un año de edad deberían pesar “un poco más de 40 libras si han recibido una 
notrición paropiada”. Para probar la hipótesis Hill’s, productor de alimentos para la dieta de perros, pesa 15 
perros cockers de un año de edad y descubre una media de 41.17 libras, con s = 4.71 libras. Utilice un valor α del 1%.
"""

#Hipotesis nula media poblacional <= 40
#Hipotesis alternativa media poblacional > 40
#Dos colas

media_nula = 40
media_muestral = 41.17
s = 4.71
n = 15
nivel = 0.01

ph.medias_poblacionales_muestras_pequeñas_cola_derecha(media_muestral, media_nula, n, s, nivel)

"""
Valor t: 0.9620786656184043
Valor crítico: 2.6244940675602315
Regla de decisión:
No se rechaza la hipotesis nula si Z crítica 2.6244940675602315  >= Z  0.9620786656184043
Resultado:
No se rechaza la hipotesis nula
"""