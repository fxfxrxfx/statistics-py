import dists

def media_poblacional_dos_colas(media_muestral, media_H0, n, S, nivel):
    Z_nula = (media_muestral - media_H0) / (S / n ** 0.5)
    #Valor Z de la regla de decisión de acuerdo al nivel de confianza
    Z_regla = abs(dists.valorZNormal(nivel / 2))
    print("Valor Z: " + str(Z_nula))
    print("Valor crítico: +- " + str(Z_regla))
    print("Regla de decisión: ")
    print("No se rechaza la hipotesis nula si ", -Z_regla, " <= ", Z_nula, " <= ", Z_regla)
    print("Resultado:")
    print("No se rechaza la hipotesis nula" 
        if Z_nula <= Z_regla and Z_nula >= -Z_regla 
        else "Se rechaza la hipotesis nula")


def valor_p_dos_colas(media_muestral, media_H0, n, S):
    Z_nula = (media_muestral - media_H0) / (S / n ** 0.5)
    valorZ = dists.probabilidadZ(abs(Z_nula))
    p = (1 - valorZ) * 2
    print("Valor Z: ", Z_nula)
    print("Probabilidad de Z: ", valorZ)
    print("Valor p: ", p)
    print("Puede bajar alfa hasta ", p, " sin rechazar la hipotesis nula. ")


def media_poblacional_cola_izquierda(media_muestral, media_H0, n, S, nivel):
    Z_nula = (media_muestral - media_H0) / (S / n ** 0.5)
    #Valor Z de la regla de decisión de acuerdo al nivel de confianza
    Z_regla = dists.valorZNormal(nivel)
    print("Valor Z: " + str(Z_nula))
    print("Valor crítico: " + str(Z_regla))
    print("Regla de decisión: ")
    print("No se rechaza la hipotesis nula si Z crítica: ", Z_regla, " <= Z:", Z_nula)
    print("Resultado:")
    print("No se rechaza la hipotesis nula" 
        if Z_nula >= Z_regla 
        else "Se rechaza la hipotesis nula")


def valor_p_cola_izquierda(media_muestral, media_H0, n, S):
    Z_nula = (media_muestral - media_H0) / (S / n ** 0.5)
    valorZ = dists.probabilidadZ(Z_nula)
    p = valorZ
    print("Valor Z: ", Z_nula)
    print("Probabilidad de Z: ", valorZ)
    print("Valor p: ", p)
    print("Puede subir alfa hasta ", p, " sin rechazar la hipotesis nula. ")


def media_poblacional_cola_derecha(media_muestral, media_H0, n, S, nivel):
    Z_nula = (media_muestral - media_H0) / (S / n ** 0.5)
    #Valor Z de la regla de decisión de acuerdo al nivel de confianza
    Z_regla = dists.valorZNormal(1 - nivel)
    print("Valor Z: " + str(Z_nula))
    print("Valor crítico: " + str(Z_regla))
    print("Regla de decisión: ")
    print("No se rechaza la hipotesis nula si Z crítica", Z_regla, " >= Z ", Z_nula)
    print("Resultado:")
    print("No se rechaza la hipotesis nula" 
        if Z_nula <= Z_regla 
        else "Se rechaza la hipotesis nula")


def valor_p_cola_derecha(media_muestral, media_H0, n, S):
    Z_nula = (media_muestral - media_H0) / (S / n ** 0.5)
    valorZ = dists.probabilidadZ(Z_nula)
    p = 1 - valorZ
    print("Valor Z: ", Z_nula)
    print("Probabilidad de Z: ", valorZ)
    print("Valor p: ", p)
    print("Puede subir alfa hasta ", p, " sin rechazar la hipotesis nula. ")


def medias_poblacionales_muestras_pequeñas_dos_colas(media_muestral, media_H0, n, S, nivel):
    t_nula = ( media_muestral - media_H0 ) / ( S / n ** 0.5 )
    gL = n - 1
    t_regla = abs(dists.valort(nivel / 2, gL))
    print("Valor t: " + str(t_nula))
    print("Valor crítico: +- " + str(t_regla))
    print("Regla de decisión: ")
    print("No se rechaza la hipotesis nula si ", -t_regla, " <= ", t_nula, " <= ", t_regla)
    print("Resultado:")
    print("No se rechaza la hipotesis nula" 
        if t_nula <= t_regla and t_nula >= -t_regla 
        else "Se rechaza la hipotesis nula")


def medias_poblacionales_muestras_pequeñas_cola_derecha(media_muestral, media_H0, n, S, nivel):
    t_nula = ( media_muestral - media_H0 ) / ( S / n ** 0.5 )
    gL = n - 1
    t_regla = abs(dists.valort(nivel, gL))
    print("Valor t: " + str(t_nula))
    print("Valor crítico: " + str(t_regla))
    print("Regla de decisión: ")
    print("No se rechaza la hipotesis nula si Z crítica", t_regla, " >= Z ", t_nula)
    print("Resultado:")
    print("No se rechaza la hipotesis nula" 
        if t_nula <= t_regla 
        else "Se rechaza la hipotesis nula")


def pruebas_para_proporcion_dos_colas(proporcion, n, proporcion_planteada, nivel):
    error_estandar = ( ( proporcion_planteada * ( 1 - proporcion_planteada) ) / n) ** 0.5
    Z_nula = (proporcion - proporcion_planteada) / error_estandar
    print("Error estandar: ", error_estandar)
    print("Valor de Z", Z_nula)
    Z_regla = abs(dists.valorZNormal(nivel / 2))
    print("Valor Z: " + str(Z_nula))
    print("Valor crítico: +- " + str(Z_regla))
    print("Regla de decisión: ")
    print("No se rechaza la hipotesis nula si ", -Z_regla, " <= ", Z_nula, " <= ", Z_regla)
    print("Resultado:")
    print("No se rechaza la hipotesis nula" 
        if Z_nula <= Z_regla and Z_nula >= -Z_regla 
        else "Se rechaza la hipotesis nula")


def valor_p_para_proporcion_dos_colas(proporcion, n, proporcion_planteada):
    error_estandar = ( ( proporcion_planteada * ( 1 - proporcion_planteada) ) / n) ** 0.5
    Z_nula = (proporcion - proporcion_planteada) / error_estandar
    valorZ = dists.probabilidadZ(abs(Z_nula))
    p = (1 - valorZ) * 2
    print("Valor Z: ", Z_nula)
    print("Probabilidad de Z: ", valorZ)
    print("Valor p: ", p)
    print("Puede bajar alfa hasta ", p, " sin rechazar la hipotesis nula. ")


def pruebas_para_proporcion_cola_izquierda(proporcion, n, proporcion_planteada, nivel):
    error_estandar = ( ( proporcion_planteada * ( 1 - proporcion_planteada) ) / n) ** 0.5
    Z_nula = (proporcion - proporcion_planteada) / error_estandar
    print("Error estandar: ", error_estandar)
    print("Valor de Z", Z_nula)
    Z_regla = dists.valorZNormal(nivel)
    print("Valor Z: " + str(Z_nula))
    print("Valor crítico: " + str(Z_regla))
    print("Regla de decisión: ")
    print("No se rechaza la hipotesis nula si Z crítica: ", Z_regla, " <= Z:", Z_nula)
    print("Resultado:")
    print("No se rechaza la hipotesis nula" 
        if Z_nula >= Z_regla 
        else "Se rechaza la hipotesis nula")


def valor_p_proporcion_cola_izquierda(proporcion, n, proporcion_planteada):
    error_estandar = ( ( proporcion_planteada * ( 1 - proporcion_planteada) ) / n) ** 0.5
    Z_nula = (proporcion - proporcion_planteada) / error_estandar
    valorZ = dists.probabilidadZ(Z_nula)
    p = valorZ
    print("Valor Z: ", Z_nula)
    print("Probabilidad de Z: ", valorZ)
    print("Valor p: ", p)
    print("Puede subir alfa hasta ", p, " sin rechazar la hipotesis nula. ")


def pruebas_para_proporcion_cola_derecha(proporcion, n, proporcion_planteada, nivel):
    error_estandar = ( ( proporcion_planteada * ( 1 - proporcion_planteada) ) / n) ** 0.5
    Z_nula = (proporcion - proporcion_planteada) / error_estandar
    print("Error estandar: ", error_estandar)
    print("Valor de Z", Z_nula)
    Z_regla = dists.valorZNormal(1 - nivel)
    print("Valor Z: " + str(Z_nula))
    print("Valor crítico: " + str(Z_regla))
    print("Regla de decisión: ")
    print("No se rechaza la hipotesis nula si Z crítica", Z_regla, " >= Z ", Z_nula)
    print("Resultado:")
    print("No se rechaza la hipotesis nula" 
        if Z_nula <= Z_regla 
        else "Se rechaza la hipotesis nula")


def valor_p_proporcion_cola_derecha(proporcion, n, proporcion_planteada):
    error_estandar = ( ( proporcion_planteada * ( 1 - proporcion_planteada) ) / n) ** 0.5
    Z_nula = (proporcion - proporcion_planteada) / error_estandar
    valorZ = dists.probabilidadZ(Z_nula)
    p = 1 - valorZ
    print("Valor Z: ", Z_nula)
    print("Probabilidad de Z: ", valorZ)
    print("Valor p: ", p)
    print("Puede subir alfa hasta ", p, " sin rechazar la hipotesis nula. ")