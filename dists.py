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


print(distNormal(250 * 31, 30 * 250, 250*12) - distNormal(250 * 30, 30 * 250, 250*12))
print(distNormal(32, 30, (12)/(250**0.5)) - distNormal(30, 30, (12)/(250**0.5)))
print(distNormal(31, 30, (12**2)/(250**0.5)) - distNormal(29, 30, (12**2)/(250**0.5)))
print(distNormal(32, 30, 12/(250**0.5)) - distNormal(29, 30, 12/(250**0.5)))

