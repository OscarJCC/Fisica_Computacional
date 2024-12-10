"""
Nombre: P07-OscarCastro Movimiento De Proyectiles Con Friccion Variable
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

def Metodo_De_Euler(x0,y0,v0,t0,tf,A0,h,N):
     global i, j, Bm, g, a, alp, tem
     
     xg = [] # Matriz para guardar las interaciones de la lista x
     yg = [] # Matriz para guardar las interaciones de la lista y
     vxg = [] # Matriz para guardar las interaciones de la lista vx
     vyg = [] # Matriz para guardar las interaciones de la lista vy
     tg = [] # Matriz para guardar las interaciones de la lista t
     vg = [] # Matriz para guardar las interaciones de la lista v
     
     for j in range(len(A0)):
          tf = 100000000
          vx0 = v0*np.cos(Grados_A_Radianes(A0[j]))
          vy0 = v0*np.sin(Grados_A_Radianes(A0[j]))
          v = np.sqrt((vx0)**2 + (vy0)**2)
          x = [x0]   # Lista para guardar las interaciones de x(t)
          y = [y0]   # Lista para guardar las interaciones de y(t)
          vx = [vx0] # Lista para guardar las interaciones de v_x(t)
          vy = [vy0] # Lista para guardar las interacionde de v_y(t)
          t = [t0]  # Lista para guardar las interaciones del tiempo
          vt = [v]  # Lista para guardar las interaciones del v(t)
          
          while t0 < tf: # Metodo de Euler
               vx0 = vx0 - Bm*v*vx0*((1-((a*y0)/(Tem)))**alp)*h
               x0 = x0 + vx0*h
               
               vy0 = vy0 - g*h - Bm*v*vy0*((1-((a*y0)/(Tem)))**alp)*h
               y0 = y0 + vy0*h
               
               t0 += h
               v = np.sqrt((vx0)**2 + (vy0)**2)
               vx.append(vx0)
               vy.append(vy0)
               x.append(x0)
               y.append(y0)
               t.append(t0)
               vt.append(v)
               if y0 < 0: # Criterio de paro cuando el proyectil cae
                    tf = t0
               i += 1
               
          t0 = 0
          i = 0
          x0 = 0
          y0 = 0 
          v0 = 700
          
          xg.append(x)
          yg.append(y)
          vxg.append(vx)
          vyg.append(vy)
          tg.append(t)
          vg.append(vt)
          
          x = [] 
          y = [] 
          vx = []
          vy = []
          t = []
          vt = []
         
     return Grafica(xg,yg,vxg,vyg,vg,tg,N)
     
def Grafica(xg,yg,vxg,vyg,vg,tg,N):
     j = 0
     color = ["white","gray","brown","purple","blue","green","yellow","orange","pink"]
     
     plt.style.use("dark_background")
     
     #Grafica de la v_x vs t
     fig, l3 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     l3.set_title(N+r"$v_x$ vs $t$", fontsize = 15)
     l3.set_xlabel(r"$t(s)$")
     l3.set_ylabel("$v_x(t)$")
     l3.grid(color = "turquoise")
     l3.axhline(color = "red")
     l3.axvline(color = "red")
     for j in range(len(A0)):
          l3.plot(tg[j],vxg[j], color = color[j], label = f"Angulo = {A0[j]}°")
     l3.legend(edgecolor = "red", fontsize = 10, labelcolor = color)
     
     #Grafica de la v_y vs t
     fig, l2 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     l2.set_title(N+r"$v_y$ vs $t$", fontsize = 15)
     l2.set_xlabel(r"$t(s)$")
     l2.set_ylabel("$v_y(t)$")
     l2.grid(color = "turquoise")
     l2.axhline(color = "red")
     l2.axvline(color = "red")
     for j in range(len(A0)):
          l2.plot(tg[j],vyg[j], color = color[j], label = f"Angulo = {A0[j]}°")
     l2.legend(edgecolor = "red", fontsize = 10, labelcolor = color)
     
     #Grafica de la v vs t
     fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     l1.set_title(N+r"$v$ vs $t$", fontsize = 15)
     l1.set_xlabel(r"$t(s)$")
     l1.set_ylabel("$v(t)$")
     l1.grid(color = "turquoise")
     l1.axhline(color = "red")
     l1.axvline(color = "red")
     for j in range(len(A0)):
          l1.plot(tg[j],vg[j], color = color[j], label = f"Angulo = {A0[j]}°")
     l1.legend(edgecolor = "red", fontsize = 10, labelcolor = color)
     
     # Grafica de la y vs x
     fig, l0 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     l0.set_title(N+r"$y$ vs $x$", fontsize = 15)
     l0.set_xlabel(r"$x(t)$")
     l0.set_ylabel(r"$y(t)$")
     l0.grid(color = "turquoise")
     l0.axhline(color = "red")
     l0.axvline(color = "red")
     for j in range(len(A0)):
          l0.plot(xg[j],yg[j], color = color[j], label = f"Angulo = {A0[j]}°")
     l0.legend(edgecolor = "red", fontsize = 10, labelcolor = color)
     
     plt.show()

#Variables------------------------------

x0 = 0    # Posicion inicial
y0 = 0    # Altura inicial
v0 = 700  # Velocidad inicial
t0 = 0    # Tiempo inicial
tf = 0
Bm = 4e-5
g = 9.81  # Aceleracion de la gravedad
a = 6.5e-3
Tem = 293.15 # Temperatura al nivel del mar (K)
alp = 2.5
h = .1  # Tamaño de paso

#Iteradores
i = 0
j = 0

# Angulos de proyeccion inicial
A0 = [10,20,30,40,50,60,70,80,85]

# Aplicacion del Metodo de Euler para encontrar la solucion numerica de las Ec. Dif.
Metodo_De_Euler(x0,y0,v0,t0,tf,A0,h,f"Metodo de Euler\nMovimiento De Proyectiles Con Friccion Variable\n")