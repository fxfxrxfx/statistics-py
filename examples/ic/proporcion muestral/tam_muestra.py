import sys
sys.path.insert(0, '../../../lib/')
import ic
"""
Wally Simpleton está postulado para gobernador. Él desea estimar dentro de 1 punto porcentual la proporción 
de personas que votarán por él. También desea tener el 95% de confianza de sus hallazgos. ¿Qué tan grande debería 
ser el tamaño muestral?
"""


p = 0.5 # No lo dicen
nivel = 0.95

tam = ic.tamano_proporcion(0.01, 0.5, 0.95)
print(tam)