# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 10:13:14 2019

@author: fxfxrxfx
"""
import scipy.stats as scipy
import math

def distBinomial(n, p, x):
    return scipy.binom.pmf(x, n, p)

def distBinomialAcum(n, p, x):
    return scipy.binom.cdf(x, n, p)

#M = Tamaño de la muestra grande
#N = Tamaño de la muestra pequeña
#n = Tamaño de la parte de la muestra pequeña que coge
#x = Probabilidad buscada
def distHiperG(M, N, n, x):
    return scipy.hypergeom.pmf(x, M, n, N)

#M = Tamaño de la muestra grande
#N = Tamaño de la muestra pequeña
#n = Tamaño de la parte de la muestra pequeña que coge
#x = Probabilidad buscada
def distHiperGAcum(N, r, n, x):
    return scipy.hypergeom.cdf(x, M, n, N)

#u => Prop
#x => Expected
def distPoisson(u, x):
    return scipy.poisson.pmf(x, u)

#u => Prop
#x => Expected
def distPoissonAcum(u, x):
    return scipy.poisson.cdf(x, u)


#u => Prop
#x => Expected
def distExp(u, x):
    return (1 -  math.e ** (-u * x))



def distUniforme(m1, m2, x1, x2):
    return (x2 - x1) / (m2 - m1)


def distNormal(X, u, S):    
    return scipy.norm.cdf(X, u, S)


#Obtener valor Z para una probabilidad p
#p => probabilidad
def valorZNormal(p):
    return scipy.norm.ppf(p)

#Obtener valor t de una distribución t-student para una probabilidad p
#p => probabilidad
#grados => Grados de libertad ( n - 1 )
def valort(p, grados):
    return scipy.t.ppf(p, grados)


#Obtener un valor como si buscado en la tabla se tratara
#Ej1: 1.5 => 0.9331927987311419
#Ej2: 3.4 => 0.9996630707343231
#Ej3: 2.3 => 0.9892758899783242
#Ej4: 0.4 => 0.6554217416103242
def probabilidadZ(valor):
    return scipy.norm.cdf(valor)


def xi2(values, expected):
    return scipy.chisquare(values, expected)


