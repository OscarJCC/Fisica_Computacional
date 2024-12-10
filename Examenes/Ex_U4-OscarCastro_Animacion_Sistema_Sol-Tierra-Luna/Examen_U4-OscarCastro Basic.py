"""
Nombre: P17-OscarCastro El Movimiento Planetario 3
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

def Metodo_De_Euler(x0t,y0t,vx0t,vy0t,mt,x0l,y0l,vx0l,vy0l,ml,ms,t0,tf,h,N):
     global i

     xgt = [x0t] # Matriz para guardan las interaciones de posicion en x tierra
     ygt = [y0t] # Matriz para guardan las interaciones de posicion en y tierra
     
     xgl = [x0l] # Matriz para guardan las interaciones de posicion en x de la Luna
     ygl = [y0l] # Matriz para guardan las interaciones de posicion en y de la Luna
     
     tg = [] # Matriz para guardar las interaciones de tiempo

     rts = np.sqrt(x0t**2 + y0t**2)                          # Radio sol tierra
     rls = np.sqrt(x0l**2 + y0l**2)                          # Radio sol Luna
     rtl = np.sqrt((x0t - x0l)**2 + (y0t - y0l)**2)    # Radio tierra Luna
     
     Cls = ml/ms
     Cts = mt/ms
     
     while t0 < tf: # Metodo de Euler

          vx0t = vx0t - 4*(np.pi**2)*(x0t/(rts**3) + (Cls)*((x0t-x0l)/(rtl**3)))*h # Iteracion de velocidad en x de la tierra
          vx0l = vx0l - 4*(np.pi**2)*(x0l/(rls**3) + (Cts)*((x0l-x0t)/(rtl**3)))*h # Iteracion de velocidad en x de la Luna
          
          x0t = x0t + vx0t*h # Iteracion de la posicion en x de la tierra
          x0l = x0l + vx0l*h # Iteracion de la posicion en x de la Luna

          vy0t = vy0t - 4*(np.pi**2)*(y0t/(rts**3) + (Cls)*((y0t-y0l)/(rtl**3)))*h # Iteracion de velocidad en x de la tierra
          vy0l = vy0l - 4*(np.pi**2)*(y0l/(rls**3) + (Cts)*((y0l-y0t)/(rtl**3)))*h # Iteracion de velocidad en x de la Luna
          
          y0t = y0t + vy0t*h # Iteracion de la posicion en x de la tierra
          y0l = y0l + vy0l*h # Iteracion de la posicion en x de la Luna
          
          rts = np.sqrt(x0t**2 + y0t**2)
          rls = np.sqrt(x0l**2 + y0l**2)
          rtl = np.sqrt((x0t - x0l)**2 + (y0t - y0l)**2)
          
          t0 += h
          i += 1
          
          xgt.append(x0t)
          xgl.append(x0l)
          
          ygt.append(y0t)
          ygl.append(y0l)
          
          tg.append(t0)   
     return Grafica(xgt,ygt,xgl,ygl,tg,N)

def Grafica(xgt,ygt,xgl,ygl,tg,N):     
     plt.style.use("dark_background") 
     fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     # Grafica
     l1.set_title(N+"\n"+r"$x$ vs $y$", fontsize = 15)
     l1.set_xlabel(r"$x(t)$")
     l1.set_ylabel(r"$y(t)$")
     l1.grid(color = "turquoise")
     l1.axhline(color = "red")
     l1.axvline(color = "red")
     l1.plot(0,0,"o",color = "yellow", label = "Sol",ms = 10)
     l1.plot(xgt[i-1],ygt[i-1],"o",color = "green", label = "Tierra",ms = 6)
     l1.plot(xgl[i-1],ygl[i-1],"o",color = "white", label = "Luna",ms = 4)
     l1.plot(xgt,ygt,"--", color = "green",ms = 1,lw = 1)
     l1.plot(xgl,ygl,"--", color = "white",ms = 1,lw = 1)
     l1.axis("equal") #Ajuatr ejes
     l1.legend(edgecolor = "red", fontsize = 10)
     
     plt.show()

#Variables------------------------------

x0t = 1                  # Posicion incial en x de la Tierra
x0l = x0t + 2.56267e-3     # Posicion incial en x de la Luna

vx0t = 0       # Velocidad incial en x de la Tierra
vx0l = 0       # Velocidad incial en x de la Luna

vt = 29.78
vl = vt + 1.022

ms = 1.98892e30     # Masa del Sol
mt = 5.9742e24      # Massa de la Tierra
ml = 7.349e22      # Masa de la Luna

y0t = 0        # Posicion incial en y de la Tierra
y0l = 0        # Posicion incial en y de la Luna

vy0t = (2*np.pi)*(vt/29.78)   # Velocidad incial en y de la Tierra
vy0l = (2*np.pi)*(vl/29.78)   # Velocidad incial en y de la Luna

t0 = 0                        # Tiempo inicial
tf = 1                        # Tiempo final
h = .0001                     # Tamaños de paso
i = 0

# Aplicacion del Metodo de Euler para encontrar la solucion numerica de la Ec. Dif.

Metodo_De_Euler(x0t,y0t,vx0t,vy0t,mt,x0l,y0l,vx0l,vy0l,ml,ms,t0,tf,h,f"Sistema Sol-Tierra-Luna")