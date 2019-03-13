import sys
sys.path.insert(0, '../../../lib/')
import ph
"""
Se supone que el embotellador desea probar la hipótesis de que la media poblacional es
de 16 onzas y selecciona un nivel de significancia del 5% debido a que
se plantea la hipotesis de que u = 16

Si el embotellador selecciona una muestra de n = 50 botellas con una media de 16.357 onzas y una desviación
estandar de 0.866 onzas
"""

hip_nula = "u = 16"
hip_alternativa = "u != 16"
media_hip_nula = 16

n = 50
media = 16.357
sd = 0.866

#Nivel de confianza = 1 - nivel de significancia
nivel = 0.05

ph.media_poblacional_dos_colas(media, media_hip_nula, n, sd, nivel)


"""
Valor Z: 2.91497830119627
Valor crítico: +-1.6448536269514722
Regla de decisión:
No se rechaza la hipotesis nula si - 1.6448536269514722  <=  2.91497830119627  <=  1.6448536269514722
Resultado:
Se rechaza la hipotesis nula
"""