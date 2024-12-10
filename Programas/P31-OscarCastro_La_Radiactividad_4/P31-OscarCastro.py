"""
Nombre: P31-OscarCastro La Radiactividad 4
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

def RegrecionExp(xg,Pg):
     e = np.polyfit(xg,np.log(Pg),1)
     
     ecu = np.exp(e[1]+e[0]*xg) 
     return [ecu,e]

def Radiactividad(N0,p,tf,R,T):
     
     y = []        # Matriz para guardar los pasos de las caminatas
     yg = []
     xg = np.arange(N0/100)
     xi = factorial(xg)
     Pr = 0
     Pro = 0
     i = 0
     
     while i < R:
          for j in range(N0):
               r = rm.uniform(0,1)
               y.append(r)
               
          for k in y:
               if k <= p:
                    N0 -= 1
          yg.append(1000-N0)
          y = []
          N0 = 1000
          i += 1
     
     for l in yg:
          Pr += l
     Pro = Pr/R
     
     P = []
     for i in range(len(xg)):
          Prom = ((Pro**xg[i])/(xi[i]))*np.exp(-1*Pro)
          P.append(Prom)
     
     print(P)
     
     return Grafica(xg,P,T)
     
def Grafica(xg,P,T):
     
     plt.style.use("dark_background") 
     fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     l1.set_title(T+"\n"+r"$N(t)$ vs $t$", fontsize = 10)
     l1.set_xlabel(r"$t$")
     l1.set_ylabel("$N(t)$")
     l1.grid(color = "turquoise")
     l1.axhline(color = "red")
     l1.axvline(color = "red")
     l1.plot(xg,P, color = "white", label = f"Promedio de Nucleos que decaen es {N0*p}\nLa probabilidad de que n nucleos decaigan el el primer intevalo es de {p}")
     #l1.plot(xg,ec1[0], color = "blue", label = "Regresion Exponencial\n\n" + f"{round(np.exp(ec1[1][1]),5)} " + r"$exp$ ^ " + f"({round(ec1[1][0],3)}x )\n\n" + r"$\lambda$ = " + f"{round(ec1[1][0],3)}")
     l1.legend(edgecolor = "red", fontsize = 10)#, labelcolor = "blue")
     
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

N0 = 1000
p = 0.001
tf = 1
R = 1000

T = "Radiactividad"

Radiactividad(N0,p,tf,R,T)