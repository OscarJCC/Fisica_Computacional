"""
Nombre: P32-OscarCastro Metodos Variacionales
Fecha Inicio:
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

"""

import numpy as np
from scipy.special import factorial
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr
import random as rm

# Funciones------------------------------


def Rayos(N,n1,n2,T,k):
     
     xg = range(N)
     yg = np.array([[0.0]*N]*k)
     y = np.array([0.0]*N)
     j = 0
     m = 1
     
     for i in range(1,N-1):
          r = rm.random()
          y[i] = r
          
     y[N-1] = 1
     
     yg[0] = y
     
     print(yg)
     
     while m < k:
          while j < N-2:
               s = np.sqrt(y[j]**2+y[j+2]**2)
               s1 = np.sqrt(y[j]**2+y[j+1]**2)
               s2 = np.sqrt(y[j+1]**2+y[j+2]**2)

               if j < N//2-1:
                    L = n1*s1+n1*s2
               elif j == N//2-1:
                    L = n1*s1+n2*s2
               elif j > N//2-1:
                    L = n2*s1+n2*s2
               
               #print(s1,s2,L,s,L-s)
               
               if abs(L-s) < 0.5:
                    j += 1
                    
                    yg[m] = y
                    print(yg)
               else:
                    r = rm.random()
                    y[j+1] = r
               #     print(y)
          #print(yg)
          j = 0
          m += 1
     return Grafica(xg,yg,T)
     
def Grafica(xg,yg,T):
     
     color = ["white","blue","red","yellow","green"]
     
     plt.style.use("dark_background") 
     fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     l1.set_title(T+"\n"+r"$N(t)$ vs $t$", fontsize = 10)
     l1.set_xlabel(r"$t$")
     l1.set_ylabel("$N(t)$")
     l1.grid(color = "turquoise")
     l1.axhline(color = "red")
     l1.axvline(color = "red")
     for i in range(len(yg)):
          l1.plot(xg,yg[i], color = color[i])
     #l1.legend(edgecolor = "red", fontsize = 10)#, labelcolor = "blue")
     
     plt.show()

# Variables------------------------------

N = 5
n1 = 1
n2 = 1.5
k = 5

T = "Principio de Fermat y Ley de Snell"

Rayos(N,n1,n2,T,k)