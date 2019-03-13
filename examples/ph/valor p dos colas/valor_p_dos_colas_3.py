import sys
sys.path.insert(0, '../../../lib/')
import ph

"""
Forbes (septiembre de 1996) reportó que Freddie McMann, representante de la cantante de pop Mdonna, 
estimó que las ventas diarias de su nuevo álbum excedería las de su éxito más grande de 1994, like a virgen,
el cual tuvo un promedio de ventas de 27400 copias. ¿Freddie rstá en lo cierto a un nivel de significancia 
del 10% si 50 observaciones (días) poseen una media de 28788 copias con una desviación estándar de 3776? 
Calcule e interprete el valor de p.
"""

#Hipotesis nula u <= 27400
#Hipotesis alternativa u > 27400 

n = 50
media_muestral = 28788
s = 3776

media_nula = 27400

nivel = 0.1


ph.valor_p_cola_derecha(media_muestral, media_nula, n, s)
ph.media_poblacional_cola_derecha(media_muestral, media_nula, n, s, nivel)
ph.media_poblacional_cola_derecha(media_muestral, media_nula, n, s, 0.003)
 
"""
Valor Z: 2.5992166638954664
Valor crítico: 1.2815515655446004
Regla de decisión:
No se rechaza la hipotesis nula si Z crítica 1.2815515655446004  >= Z  2.5992166638954664
Resultado:
Se rechaza la hipotesis nula
Entonces Freddie puede estar seguro de que superará su más grande exito
"""

"""
Valor Z:  2.5992166638954664
Probabilidad de Z:  0.9953281611046682
Valor p:  0.004671838895331848
Puede subir alfa hasta  0.004671838895331848  sin rechazar la hipotesis nula.
Hasta un nível de 0.04% de significancia, el nuevo álbum excedería las de su más grande éxito
"""