import sys
sys.path.insert(0, '../../../lib/')
import ic

""" Un investigador de la Administración Federan de Aviación (FAA) fue mencionado en una 
emisión de febrero de The Washington Post, en la que dijo que de los 112 accidentes de aerolíneas
“73 involucraban algún tipo de problema estructural con la aeronave”. Si tales cifras son representativas, 
¿Cuál es el intervalo de confianza para la proporción de accidentes que involucran tal defecto estructural? 
Sea α = 0.01."""

n = 112

m = 73

p = 73 / 112

nivel = 0.99

i = ic.proporcion_poblacional(n, p, nivel)

print(i)