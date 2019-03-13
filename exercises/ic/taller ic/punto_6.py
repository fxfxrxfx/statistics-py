import sys
sys.path.insert(0, '../../../lib/')
import ic

""" La división de créditos de un banco comercial grande desea estimar con un nivel de confianza del 99% 
la proporción de sus créditos que están en mora. Si el ancho del intervalo es del 7%, ¿Cuántos créditos deben 
revisarse? ¿cuál es el error tolerable? """

nivel = .99

error = 0.07 / 2

proporcion = 0.5 #NO NOS DAN LA PROPORCIÓN: USAMOS 0.5

n = ic.tamano_proporcion(error, proporcion, nivel)

print(n)