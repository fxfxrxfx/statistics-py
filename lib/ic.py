import dists

#x => Media muestral
#S  =>  Desviación estandar poblacional
#n >= 30    => Tamaño de la muestra
#nivel   => nivel de confianza deseado
def media_poblacional_muestras_grandes(n, xm, S, nivel):
    error = S / n ** 0.5
    Z = dists.valorZNormal(1 - (1 - nivel) / 2 )
    print("Valor Z: " + str(Z))
    return [xm - Z * error, xm + Z * error]

#Condiciones
#n < 30 => Pequeña
#S (Poblacional) => Desconocida
#(Si S es conocida, use Z)
#Población normal

#Parametros
#n => Tamaño de la muestra
#xm => Media muestral
#s => Desviación estandar muestral
#nivel => nivel de confianza del intervalo muestral
def media_poblacional_muestras_pequenas(n, xm, s, nivel):
    t = dists.valort(p = 1 - (1 - nivel) / 2, grados = n - 1)
    error = s / n ** 0.5
    print("Valor t: " + str(t))
    return [xm - t * error, xm + t * error]


#Intervalo de confianza para una proporción muestral
#n => Tamaño de la muestra
#p => Proporción de la muestra
#nivel => NIvel de confianza del intervalo muestral
def proporcion_poblacional(n, p, nivel):
    error = ( (p) * ( 1 - p ) / n ) ** 0.5
    Z = dists.valorZNormal(1 - (1 - nivel) / 2 )
    print("Valor Z: " + str(Z))
    return [p - Z * error, p + Z * error]


#Obtener el tamaño de una muestra según el error de un intervalo con desviación estandar s y su nivel de confianza
def tamano_muestra(error, s, nivel):
    Z = dists.valorZNormal(1 - (1 - nivel) / 2 )
    print("Valor Z: " + str(Z))
    n = ( Z * s / error ) ** 2
    return n

#Obtener el tramaño de una muestra según el error de un intervalor de confianza para su proporción poblacional y un nivel de confianza
def tamano_proporcion(error, p, nivel):
    Z = dists.valorZNormal(1 - (1 - nivel) / 2 )
    print("Valor Z: " + str(Z))
    n = ( ( p ) * ( 1 - p ) * Z ** 2) / ( error ** 2 )
    return n


#Obtener el número de datos que se deben recolectar de una muestra para mantenerse en un margen de error
#sd => Desviación estandar de la muestra/población
#nivel => Nivel de confianza del intervalo
#error => Error de margen deseado
def numero_datos_para_error(sd, error, nivel):
    Z = dists.valorZNormal(1 - (1 - nivel) / 2 )
    n = (Z * sd / error ) ** 2
    return n

#Obtener el número de datos que se deben recolectar de una proporción muestral para mantenerse en un margen de error 
#p => Proporción de la muestra
#nivel => Nivel de confianza del intervalo
#error => Error de margen deseado
def numero_datos_para_error_proporcion(p, error, nivel):
    Z = dists.valorZNormal(1 - (1 - nivel) / 2 )
    n = (Z ** 2) * (p) * ( 1 - p ) / error ** 2
    return n