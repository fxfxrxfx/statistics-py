import sys
sys.path.insert(0, '../../../lib/')
import ph

"""
Chuck Cash también sospecha que los empleados invierten un promedio de 100 UDD mensuales en el plan de 
opción de compra de acciones de la compañía. Al tomar como muestra 100 empleados, Chuck descubre una media 
de 106.81 USD con una desviación estándar de 36.60 USD. Ahora desea determinar el valor p relacionado con la 
prueba de hipótesis.
"""


#Hipotesis nula media poblacional = 100
#Hipotesis alternativa media poblacional != 100

n = 100
media_muestral = 106.81
s = 36.60

media_nula = 100



ph.valor_p_dos_colas(media_muestral, media_nula, n, s)
"""
Valor Z:  1.8606557377049187
Probabilidad de Z:  0.968603595882121
Valor p:  0.06279280823575806
Puede bajar alfa hasta  0.06279280823575806  sin rechazar la hipotesis nula.
"""