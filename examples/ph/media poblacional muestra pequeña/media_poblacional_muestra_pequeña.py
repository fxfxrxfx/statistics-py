import sys
sys.path.insert(0, '../../../lib/')
import ph

"""
Los estudiantes de una clase de estadística en State University cuestionan la afirmación de que McDonalds 
coloca 0.25 libras de carne en sus “Habueguesas de cuarto de libra”. Algunos estudiantes argumentan que en 
realidad se utiliza más, mientras otros insisten que menos. Para probar la afirmación publicitaria que el 
peso promedio es es de 0.25 libras, cada estudiante compra una hamburguesa de cuarto y la lleva a clase, en 
donde la pesan en una balanza suministrada por el instructor. Los resultados de la muestra son una media de 
0.22 libras y una desviación estándar de 0.09. Si hay 25 estudiantes en clase, ¿a que conclusión llegarían a 
un nivel de significancia del 5%?
"""

#Hipotesis nula media poblacional = 0.25
#Hipotesis alternativa media poblacional != 0.25
#Dos colas

media_nula = 0.25
media_muestral = 0.22
s = 0.09
n = 25
nivel = 0.05

ph.medias_poblacionales_muestras_pequeñas_dos_colas(media_muestral, media_nula, n, s, nivel)

"""
Valor t: -1.6666666666666667
Valor crítico: +- 2.063898561628021
Regla de decisión:
No se rechaza la hipotesis nula si  -2.063898561628021  <=  -1.6666666666666667  <=  2.063898561628021
Resultado:
No se rechaza la hipotesis nula
"""