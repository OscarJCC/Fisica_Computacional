"""
Nombre: P21-OscarCastro El Movimiento Planetario 7
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

def Metodo_De_Euler(x0,y0,vx0,vy0,t0,tf,h,N):
     global i,m,xi,yi
     xi = x0
     yi = y0
     xg = [xi] # Lista para guardan las interaciones de posicion en x
     yg = [yi] # Lista para guardan las interaciones de posicion en x
     tg = [t0] # Lista para guardar las interaciones de tiempo
     r = np.sqrt(x0**2 + y0**2)
     while t0 < tf: # Metodo de Euler
          vy0 = vy0 - ((4*(np.pi**2)*yi)/(r**3))*h
          yi = yi + vy0*h
          
          vx0 = vx0 - ((4*(np.pi**2)*xi)/(r**3))*h
          xi = xi + vx0*h

          t0 += h
          r = np.sqrt(xi**2 + yi**2)
          
          xg.append(xi)
          yg.append(yi)
          tg.append(t0)

     return Grafica(xg,yg,tg,N)
     
def Grafica(xg,yg,tg,N):
          
     plt.style.use("dark_background") 
     fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     l1.set_title(N+"\n"+r"$x$ vs $y$", fontsize = 12)
     l1.set_xlabel(r"$x(t)$")
     l1.set_ylabel("$y(t)$")
     l1.grid(color = "turquoise")
     l1.axhline(color = "red")
     l1.axvline(color = "red")
     l1.plot(0,0,"o",color = "yellow", label = "Sol",ms = 10)
     l1.plot(xg,yg,"--", color = "blue",ms = 1,lw = 1)
     l1.plot(xi,yi,"o", color = "white", label = "Mercurio",ms = 5)
     l1.axis("equal") #Ajuatr ejes
     l1.legend(edgecolor = "red", fontsize = 15)
     plt.show()

#Variables------------------------------

a = 0.39       # Distancia del Semieje Mayor
e = 0.206      # Excentricidad
x0 = a*(1+e)
vx0 = 0
y0 = 0
vy0 = np.sqrt((4*np.pi**2)*((1-e)/(a*(1+e))))
t0 = 0                        # Tiempo inicial
tf = .25                      # Tiempo final
h = .001                      # Tamaños de paso
i = 0
m = 10

# Aplicacion del Metodo de Euler para encontrar la solucion numerica de la Ec. Dif.

Metodo_De_Euler(x0,y0,vx0,vy0,t0,tf,h,f"Órbita Elíptica\nEl Movimiento Planetario 7")