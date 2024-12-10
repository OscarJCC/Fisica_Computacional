"""
Nombre: P18a-OscarCastro El Movimiento Planetario 4 Sistema Sol-Marte-Jupiter
Fecha Inicio:
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:p

-------------Metodo de Euler----------------

"""

import numpy as np
import matplotlib.pyplot as plt

# Funciones------------------------------

def Grados_A_Radianes(A0):
     return (A0*np.pi)/180

def Metodo_De_Euler(x0m,y0m,vx0m,vy0m,mm,x0j,y0j,vx0j,vy0j,mj,ms,t0,tf,h,N):
     global i

     xgm = [] # Matriz para guardan las interaciones de posicion en x marte
     ygm = [] # Matriz para guardan las interaciones de posicion en y marte
     
     xgj = [] # Matriz para guardan las interaciones de posicion en x jupiter
     ygj = [] # Matriz para guardan las interaciones de posicion en y jupiter
     
     tg = [] # Matriz para guardar las interaciones de tiempo

     rm = np.sqrt(x0m**2 + y0m**2)                          # Radio sol marte
     rj = np.sqrt(x0j**2 + y0j**2)                          # Radio sol jupiter
     rmj = np.sqrt((x0m - x0j)**2 + (y0m - y0j)**2)    # Radio marte jupiter
     
     Cjs = mj/ms
     Cms = mm/ms
     
     while t0 < tf: # Metodo de Euler

          vx0m = vx0m - 4*(np.pi**2)*(x0m/(rm**3) + (Cjs)*((x0m-x0j)/(rmj**3)))*h # Iteracion de velocidad en x de la marte
          vx0j = vx0j - 4*(np.pi**2)*(x0j/(rj**3) + (Cms)*((x0j-x0m)/(rmj**3)))*h # Iteracion de velocidad en x de jupiter
          
          x0m = x0m + vx0m*h # Iteracion de la posicion en x de la marte
          x0j = x0j + vx0j*h # Iteracion de la posicion en x jupiter

          vy0m = vy0m - 4*(np.pi**2)*(y0m/(rm**3) + (Cjs)*((y0m-y0j)/(rmj**3)))*h # Iteracion de velocidad en x de la marte
          vy0j = vy0j - 4*(np.pi**2)*(y0j/(rj**3) + (Cms)*((y0j-y0m)/(rmj**3)))*h # Iteracion de velocidad en x de jupiter
          
          y0m = y0m + vy0m*h # Iteracion de la posicion en x de la marte
          y0j = y0j + vy0j*h # Iteracion de la posicion en x jupiter
          
          rm = np.sqrt(x0m**2 + y0m**2)
          rj = np.sqrt(x0j**2 + y0j**2)
          rmj = np.sqrt((x0m - x0j)**2 + (y0m - y0j)**2)
          
          t0 += h
          i += 1
          
          xgm.append(x0m)
          xgj.append(x0j)
          
          ygm.append(y0m)
          ygj.append(y0j)
          
          tg.append(t0)
          
     return Grafica(xgm,ygm,xgj,ygj,tg,N)

def Grafica(xgm,ygm,xgj,ygj,tg,N):     
     plt.style.use("dark_background") 
     fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     nom = ["Venus","marte","Marte","Jupiter","Saturno"]
     col = ["orange","brown","red","brown","white"]
     # Grafica
     l1.set_title(N+"\n"+r"$x$ vs $y$", fontsize = 12)
     l1.set_xlabel(r"$x(t)$")
     l1.set_ylabel("$y(t)$")
     l1.grid(color = "turquoise")
     l1.axhline(color = "red")
     l1.axvline(color = "red")
     l1.plot(0,0,"o",color = "yellow", label = "Sol",ms = 10)
     l1.plot(xgm[(i-1)//int(tf)*2],ygm[(i-1)//int(tf)*2],"o",color = "brown", label = "Marte",ms = 4)
     l1.plot(xgj[i-1],ygj[i-1],"o",color = "red",label = "Jupiter",ms = 6)
     l1.plot(xgm,ygm,"--", color = "brown",ms = 1,lw = 1)
     l1.plot(xgj,ygj,"--", color = "red",ms = 1,lw = 1)
     l1.set_xlim(-11.50,11.50)
     l1.set_ylim(-5.66,5.66)
     #l1.axis("equal") #Ajuatr ejes
     l1.legend(edgecolor = "red", fontsize = 10, labelcolor = col)
     
     plt.show()

#Variables------------------------------

x0m = 1.52     # Posicion incial en x de Marte
x0j = 5.20     # Posicion incial en x de Jupiter

vx0m = 0       # Velocidad incial en x de Marte
vx0j = 0       # Velocidad incial en x de Jupiter

vm = 24.08
vj = 13.07

ms = 1.98892e30     # Masa del Sol
mm = 6.421e23       # Masa de Marte
mj = 1.8986e27      # Masa de Jupiter

y0m = 0        # Posicion incial en y de Marte
y0j = 0        # Posicion incial en y de Jupiter

vy0m = (2*np.pi)*(vm/29.78)   # Velocidad incial en y de Marte
vy0j = (2*np.pi)*(vj/29.78)   # Velocidad incial en y de Jupiter

t0 = 0                        # Tiempo inicial
tf = 11.89                    # Tiempo final
h = .001                      # Tamaños de paso
i = 0

# Aplicacion del Metodo de Euler para encontrar la solucion numerica de la Ec. Dif.

Metodo_De_Euler(x0m,y0m,vx0m,vy0m,mm,x0j,y0j,vx0j,vy0j,mj,ms,t0,tf,h,f"El Movimiento Planetario 4\nSistema Sol-Marte-Jupiter")