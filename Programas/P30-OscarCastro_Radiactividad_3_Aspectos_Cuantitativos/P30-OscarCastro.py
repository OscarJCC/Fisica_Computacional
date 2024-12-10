"""
Nombre: P30-OscarCastro La Radiactividad 3 Aspectos Cuantitativos
Fecha Inicio:
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

"""

import numpy as np
import matplotlib.pyplot as plt
#from scipy.stats.stats import pearsonr
import random as rm

# Funciones------------------------------

def RegrecionExp(xg,Pg):
     e = np.polyfit(xg,np.log(Pg),1)
     
     ecu = np.exp(e[1]+e[0]*xg) 
     return [ecu,e]

def Radiactividad(n,p,h,tf,R,N):
     p
     y = []
     yg = [n]
     ygp = []
     xg = np.arange(tf)
     P = 0
     Pg = []
     i = 0
     m = 0
     
     while m < R:
          #print(i)
          while i < tf:
               for j in range(n):
                    r = rm.uniform(0,1)
                    y.append(r)

               for k in y:
                    if k <= p:
                         n -= 1
               yg.append(n)
               y = []
               i += 1
          ygp.append(yg)
          n = 10000
          yg = [n]
          i = 0
          m += 1
     
     for w in range(R):
          for l in range(R):
               P += ygp[l][w]
          Pg.append(P/R)
          P = 0   
     
     ec1 = RegrecionExp(xg,Pg)
     
     print(ec1)
     
     return Grafica(xg,Pg,ec1,N)
     
def Grafica(xg,yg,ec1,N):
     
     plt.style.use("dark_background") 
     fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     l1.set_title(N+"\n"+r"$N(t)$ vs $t$", fontsize = 10)
     l1.set_xlabel(r"$t$")
     l1.set_ylabel("$N(t)$")
     l1.grid(color = "turquoise")
     l1.axhline(color = "red")
     l1.axvline(color = "red")
     l1.bar(xg,yg, color = "white")
     l1.plot(xg,ec1[0], color = "blue", label = "Regresion Exponencial\n\n" + f"{round(np.exp(ec1[1][1]),5)} " + r"$exp$ ^ " + f"({round(ec1[1][0],3)}x )\n\n" + r"$\lambda$ = " + f"{round(ec1[1][0],3)}")
     l1.legend(edgecolor = "red", fontsize = 10, labelcolor = "blue")
     
#     fig, l2 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
#     l2.set_title(N+"\n"+r"$t$ vs $Promedio^2$", fontsize = 15)
#     l2.set_xlabel(r"$t$")
#     l2.set_ylabel("$Promedio^2$")
#     l2.grid(color = "turquoise")
#     l2.axhline(color = "turquoise")
#     l2.axvline(color = "turquoise")
#     l2.plot(xg,yg2,"--", color = "white", label = "Regresion lineal")
#     l2.plot(xg,ec2(xg), color = "blue", label = f"Ecuacion:\n {str(ec2)}"+f"\n\nR = {pearsonr(yg,ec2(xg))[0]}")
#     l2.legend(edgecolor = "turquoise", fontsize = 10, labelcolor = col)
     plt.show()
#
# Variables------------------------------

n = 10000
p = 0.01
h = 1
tf = 100
R = 100

N = "Radiactividad"

Radiactividad(n,p,h,tf,R,N)