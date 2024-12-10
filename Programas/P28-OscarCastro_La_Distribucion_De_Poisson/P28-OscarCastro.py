"""
Nombre: P28-OscarCastro La Distribucion De Poisson
Fecha Inicio:
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

"""

import numpy as np
import matplotlib.pyplot as plt
import random as rm

# Funciones------------------------------

def Regrecion(xg,yg,g):
     ecu = np.poly1d(np.polyfit(xg,yg,g))
     
     return ecu

def RegrecionExp(xg,yg):
     ecu = (np.polyfit(xg,np.log(yg),1))
     print(ecu)
     return ecu

def Caminata(N,M,R,T):
     
     y = [0]*M
     yg = []
     xg = range(R)
     j = 0
     m = 0
     c = 0
     cg = []
     d = [0]*R
     dg = []
     P = 0
     Pg = []
     
     while j < R:
          for i in xg:
               r = rm.randint(0,M-1)
               if y[r] == 0:
                    c += 1
               y[r] += 1
               
          while m < R:
               for k in y:
                    #print(k)
                    if k == m:
                         d[m] += 1
               m += 1
               
          yg.append(y)
          dg.append(d)   
          cg.append(c)
          d = [0]*R
          y = [0]*M          
          c = 0
          m = 0
          j += 1

     for w in range(R):
          for l in range(R):
               P += dg[l][w]
          Pg.append((P/R)/M)
          
          P = 0
     
     Pg = np.array(Pg)
     
     return Grafica(xg,Pg,T)
     
def Grafica(xg,Pg,T):
     
     plt.style.use("dark_background") 
     fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     l1.set_title(T+"\n"+r"$P(n)$ vs $n$", fontsize = 15)
     l1.set_xlabel(r"$n$")
     l1.set_ylabel(r"$P(n)$")
     l1.grid(color = "turquoise")
     l1.axhline(color = "red")
     l1.axvline(color = "red")
     l1.plot(xg[:10],Pg[:10],".",color = "white")#, color = col[i], label = f"Caminata {i+1}\nDistancia Recorrida = {round(np.sqrt((yg[i][-1])**2 + (xg[i][-1])**2),3)}\nPosicion final = {(yg[i][-1],xg[i][-1])}")
     #l1.legend(edgecolor = "turquoise", fontsize = 10)
     plt.show()

# Variables------------------------------

N = 50    # Numero de dardos
M = 500   # Numero de regiones
R = M     # Numero de experimentos

T = "Lanzamiento De Dardo"

Caminata(N,M,R,T)