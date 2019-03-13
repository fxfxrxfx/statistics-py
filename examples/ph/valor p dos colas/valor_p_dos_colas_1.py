import sys
sys.path.insert(0, '../../../lib/')
import ph

"""
En mayo de 1997, el congreso aprobó un presupuesto federal que contenía varias partidas para recortes 
tributarios. Los analistas afirmaron que ahorraría al contribuyente, en promedio 800 USD por año. 
Calcule e interprete el valor p si una muestra de 500 contribuyentes presenta un ahorro promedio de 
785.10 con una desviación estándar de 187.33.
"""


#Hipotesis nula media poblacional = 800
#Hipotesis alternativa media poblacional != 800

n = 500
media_muestral = 785.10
s = 187.33

media_nula = 800



ph.valor_p_dos_colas(media_muestral, media_nula, n, s)
ph.media_poblacional_dos_colas(media_muestral, media_nula, n, s, 0.08)
 
"""
Valor Z:  -1.7785412301685162
Probabilidad de Z:  0.9623424966927349
Valor p:  0.07531500661453028
Puede bajar alfa hasta  0.07531500661453028  sin rechazar la hipotesis nula.
"""