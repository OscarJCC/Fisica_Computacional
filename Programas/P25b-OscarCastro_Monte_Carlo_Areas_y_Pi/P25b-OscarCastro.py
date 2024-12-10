"""
Nombre: P25b-OscarCastro Monte Carlo, Areas y Pi
Fecha Inicio:
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

"""

import numpy as np
import matplotlib.pyplot as plt
import random as rm

# Funciones------------------------------
def Grafica(xgd,ygd,xgf,ygf,x,y,T):

     plt.style.use("dark_background") 
     fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     l1.set_title(T+"\n"+r"$N(t)$ vs $t$", fontsize = 10)
     l1.set_xlabel(r"$t$")
     l1.set_ylabel("$N(t)$")
     l1.grid(color = "turquoise")
     l1.axhline(color = "red")
     l1.axvline(color = "red")
     l1.plot(xgf,ygf,".", color = "white", label = "Area cuadrado = 1\n\n"+r"$\frac{Area Circulo/4}{Area cuadrado} = \frac{(\pi)(R^2)}{4(R^2)} = \frac{\pi}{4}$"+"\n\nArea circulo ="+r" $\frac{\pi}{4}$ = "+f"{round(np.pi/4,3)}")
     l1.plot(xgd,ygd,".", color = "orange", label = f"\n\n{cd}/{N} ="+r" $\frac{\pi}{4} \rightarrow \pi $" + f" = 4({cd}/{N})")
     l1.plot(x,y,"-", color = "blue", label = r"$\pi$"+f" = {(4*cd)/N}"+"\n\nLa incertidubre es de "+r"$\pm$"+f"{abs(((4*cd)/N)-np.pi)}")
     l1.legend(edgecolor = "red", fontsize = 10)#, labelcolor = "blue")
     l1.axis("equal")
     plt.show()
#
# Variables------------------------------

N = 1000

T = "Calculo De Areas"

xg = []
yg = []

xgd = []
ygd = []

xgf = []
ygf = []

x = np.linspace(0,1,N)
y = np.sqrt(1-x**2)

cd = 0
cf = 0

for i in range(N):
     rx = rm.uniform(0,1)
     ry = rm.uniform(0,1)

     yg.append(ry)
     xg.append(rx)

for j in range(len(xg)):
     r = np.sqrt(xg[j]**2 + yg[j]**2)
     if r <= 1:
          cd += 1
          xgd.append(xg[j])
          ygd.append(yg[j])
     else:
          cf += 1
          xgf.append(xg[j])
          ygf.append(yg[j])
          
Grafica(xgd,ygd,xgf,ygf,x,y,T)
