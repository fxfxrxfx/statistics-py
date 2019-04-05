import dists

"""
Pruebas para parametros poblacionales
"""


"""
Pruebas para B1 
Si la pendiente de la recta de regresión poblacional real pero desconocida es cero, no existe
relación entre las variables (pasajeros y publicidad) contraria a los resultados muestrales.
Para esto, se debe probar la hipótesis
Sb1 => Error estándar de la distribución muestral de b1.
b1 => Pendiente de la recta de regresión 
Beta1 => Coeficiente de regresión para toda la población

H0: B1 = 0
Ha: B1 != 0
"""
def pruebaB1(Sb1, b1, Beta1, nivel, gL):
    t_nula = ( b1 - Beta1 ) / Sb1
    t_regla = abs(dists.valort(nivel / 2, gL))
    print("Valor t: " + str(t_nula))
    print("Valor crítico: +- " + str(t_regla))
    print("Regla de decisión: ")
    print("No se rechaza la hipotesis nula si ", -t_regla, " <= ", t_nula, " <= ", t_regla)
    print("Resultado:")
    print("No se rechaza la hipotesis nula" 
        if t_nula <= t_regla and t_nula >= -t_regla 
        else "Se rechaza la hipotesis nula")
    return t_regla


"""
Usar esto solo cuando se rechace la hipotesis nula
"""
def icB1(b1, t, Sb1):
    producto = Sb1 * t
    return [b1 - producto, b1 + producto]


"""
Pruebas para el coeficiente de correlación poblacional (p) 
Puede ser que la correlación a nivel poblacional sea cero y que una muestra engañosa hizo que se asumiera 
equivocadamente una relación. Por consiguiente se debe probar la hipótesis 
Ho: p = 0 
HA: p != 0 
Esta prueba emplea el estadístico t y tiene n - 2 grados de libertad. 
"""

def pruebap(r, p, Sr, nivel, gL):
    t_nula = ( r - p ) / Sr
    t_regla = abs(dists.valort(nivel / 2, gL))
    print("Valor t: " + str(t_nula))
    print("Valor crítico: +- " + str(t_regla))
    print("Regla de decisión: ")
    print("No se rechaza la hipotesis nula si ", -t_regla, " <= ", t_nula, " <= ", t_regla)
    print("Resultado:")
    print("No se rechaza la hipotesis nula" 
        if t_nula <= t_regla and t_nula >= -t_regla 
        else "Se rechaza la hipotesis nula")
    return t_regla