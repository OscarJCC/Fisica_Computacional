"""
Nombre: P17-OscarCastro El Movimiento Planetario 4 Sistema Sol-Tierra-Jupiter
Fecha Inicio:
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

-------------Metodo de Euler----------------

"""

import numpy as np
import matplotlib.pyplot as plt

# Funciones------------------------------

def Grados_A_Radianes(A0):
     return (A0*np.pi)/180

def Metodo_De_Euler(x0t,y0t,vx0t,vy0t,mt,x0j,y0j,vx0j,vy0j,mj,ms,t0,tf,h,N):
     global i

     xgt = [] # Matriz para guardan las interaciones de posicion en x tierra
     ygt = [] # Matriz para guardan las interaciones de posicion en y tierra
     
     xgj = [] # Matriz para guardan las interaciones de posicion en x jupiter
     ygj = [] # Matriz para guardan las interaciones de posicion en y jupiter
     
     tg = [] # Matriz para guardar las interaciones de tiempo

     rt = np.sqrt(x0t**2 + y0t**2)                          # Radio sol tierra
     rj = np.sqrt(x0j**2 + y0j**2)                          # Radio sol jupiter
     rtj = np.sqrt((x0t - x0j)**2 + (y0t - y0j)**2)    # Radio tierra jupiter
     
     Cjs = mj/ms
     Cts = mt/ms
     
     while t0 < tf: # Metodo de Euler

          vx0t = vx0t - 4*(np.pi**2)*(x0t/(rt**3) + (Cjs)*((x0t-x0j)/(rtj**3)))*h # Iteracion de velocidad en x de la tierra
          vx0j = vx0j - 4*(np.pi**2)*(x0j/(rj**3) + (Cts)*((x0j-x0t)/(rtj**3)))*h # Iteracion de velocidad en x de jupiter
          
          x0t = x0t + vx0t*h # Iteracion de la posicion en x de la tierra
          x0j = x0j + vx0j*h # Iteracion de la posicion en x jupiter

          vy0t = vy0t - 4*(np.pi**2)*(y0t/(rt**3) + (Cjs)*((y0t-y0j)/(rtj**3)))*h # Iteracion de velocidad en x de la tierra
          vy0j = vy0j - 4*(np.pi**2)*(y0j/(rj**3) + (Cts)*((y0j-y0t)/(rtj**3)))*h # Iteracion de velocidad en x de jupiter
          
          y0t = y0t + vy0t*h # Iteracion de la posicion en x de la tierra
          y0j = y0j + vy0j*h # Iteracion de la posicion en x jupiter
          
          rt = np.sqrt(x0t**2 + y0t**2)
          rj = np.sqrt(x0j**2 + y0j**2)
          rtj = np.sqrt((x0t - x0j)**2 + (y0t - y0j)**2)
          
          t0 += h
          i += 1
          
          xgt.append(x0t)
          xgj.append(x0j)
          
          ygt.append(y0t)
          ygj.append(y0j)
          
          tg.append(t0)
          
     return Grafica(xgt,ygt,xgj,ygj,tg,N)

def Grafica(xgt,ygt,xgj,ygj,tg,N):     
     plt.style.use("dark_background") 
     fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     nom = ["Venus","Tierra","Marte","Jupiter","Saturno"]
     col = ["orange","green","red","brown","white"]
     # Grafica
     l1.set_title(N+"\n"+r"$x$ vs $y$", fontsize = 12)
     l1.set_xlabel(r"$x(t)$")
     l1.set_ylabel("$y(t)$")
     l1.grid(color = "turquoise")
     l1.axhline(color = "red")
     l1.axvline(color = "red")
     l1.plot(0,0,"o",color = "yellow", label = "Sol",ms = 10)
     l1.plot(xgt[(i-1)//int(tf)],ygt[(i-1)//int(tf)],"o",color = "green",label = "Tierra",ms = 4)
     l1.plot(xgj[i-1],ygj[i-1],"o",color = "red", label = "Jupiter",ms = 6)
     l1.plot(xgt,ygt,"--", color = "green",ms = 1,lw = 1)
     l1.plot(xgj,ygj,"--", color = "red",ms = 1,lw = 1)
     l1.set_xlim(-11.50,11.50)
     l1.set_ylim(-5.66,5.66)
     #l1.axis("equal") #Ajuatr ejes
     l1.legend(edgecolor = "red", fontsize = 10, labelcolor = col)
     
     plt.show()

#Variables------------------------------

x0t = 1        # Posicion incial en x de la Tierra
x0j = 5.20     # Posicion incial en x de Jupiter

vx0t = 0       # Velocidad incial en x de la Tierra
vx0j = 0       # Velocidad incial en x de Jupiter

vt = 29.78
vj = 13.07

ms = 1.98892e30     # Masa del Sol
mt = 5.9742e24      # Massa de la Tierra
mj = 1.8986e27*1000      # Masa de Jupiter

y0t = 0        # Posicion incial en y de la Tierra
y0j = 0        # Posicion incial en y de Jupiter

vy0t = (2*np.pi)*(vt/29.78)   # Velocidad incial en y de la Tierra
vy0j = (2*np.pi)*(vj/29.78)   # Velocidad incial en y de Jupiter

t0 = 0                        # Tiempo inicial
tf = 11.89                    # Tiempo final
h = .001                      # Tamaños de paso
i = 0

# Aplicacion del Metodo de Euler para encontrar la solucion numerica de la Ec. Dif.

Metodo_De_Euler(x0t,y0t,vx0t,vy0t,mt,x0j,y0j,vx0j,vy0j,mj,ms,t0,tf,h,f"El Movimiento Planetario 4\nSistema Sol-Tierra-Jupiter")