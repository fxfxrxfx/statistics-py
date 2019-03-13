import sys
sys.path.insert(0, '../../../lib/')
import ph
"""
A comienzos de los años 90 Sony Corporation introdujo su PlayStation de 32 bits en el mercado de los juegos 
de video. La gerencia esperaba que el nuevo producto incrementara las ventas mensuales en Estados Unidos por 
encima de los 283 millones de dólares que Sonu había experimentado en la década anterior. Una muestra de 40
meses reportó una media de 297 millones de dólares. Se asume una desviación estándar de 97 millones de dólares. 
Pruebe la hipótesis a un nivel de significancia del 1%. Calcule e interprete el valor p.
"""

#Hipotesis nula u <= 282
#Hipotesis alternativa u > 282 

n = 40
media_muestral = 297
s = 97

media_nula = 282



ph.valor_p_cola_derecha(media_muestral, media_nula, n, s)
ph.media_poblacional_cola_derecha(media_muestral, media_nula, n, s, 0.16)
 
"""
Valor Z:  0.9780240186087772
Probabilidad de Z:  0.8359687775272024
Valor p:  0.16403122247279756
Puede subir alfa hasta  0.16403122247279756  sin rechazar la hipotesis nula.
"""