# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 10:13:14 2019

@author: fxfxrxfx
"""
import math

def distBinomial(n, p, x):
    return (math.factorial(n) / (math.factorial(x) * math.factorial(n - x))) * math.pow(p, x) * math.pow(1 - p, n - x)
    
def distHiperG(N, r, n, x):
    return nCr(r, x) * nCr(N - r, n - x) / nCr(N, n)

def distPoisson(u, x):
    return math.pow(u, x) * math.pow(math.e, -u) / math.factorial(x)

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def distExp(u, t):
    return 1 - math.pow(math.e, -u * t)

def distUniforme():
    return 0


def distNormal(X, u, S):    
    #u poblationa
    #S standar err
    def normalDesviation(X, u, S):
        return (X - u) / S
    var = float(S)**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(X)-float(u))**2/(2*var))
    return num/denom
    
    
#print(distBinomial(20, 0.5, 5))
#print(distHiperG(N = 10, r = 4, x = 2, n = 3))
#print(distPoisson(u = 10, x = 5))
#print(distExp(u = 1.5, t = 2))
print(distNormal(150, 150, 15) - distNormal(125, 150, 15))



def oa(saludo = "HELLO"):
    return saludo

print(oa())