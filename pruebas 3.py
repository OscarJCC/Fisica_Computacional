"""
Nombre: P35-OscarCastro Dinamica Molecular
Fecha Inicio:
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random as rm

# Funciones------------------------------
def gVI():
     vxS = 0
     vyS = 0
     for i in range(N):
          vx[i] = rm.random() - 0.5
          vy[i] = rm.random() - 0.5
          vxS += vx[i]
          vyS += vy[i]
          
     vxM = vxS/N
     vyM = vyS/N
     for i in range(N):
          vx[i] -= vxM
          vy[i] -= vyM
          
     v2S = 0
     for i in range(N):
          v2S += vx[i]**2 + vy[i]**2
     
     kep = v2S/(d*N)
     rcl = np.sqrt((k*T)/kep)
     for i in range(N):
          vx[i] *= rcl
          vy[i] *= rcl
     
def gPI():
     
     j = 1
     q = 1
     
     for i in range(N):
          
          x[i] = j*((L)/(np.sqrt(N))) - (L)/(2*np.sqrt(N))
          y[i] = q*((L)/(np.sqrt(N))) - (L)/(2*np.sqrt(N))
          
          if j >= np.sqrt(N):
               j = 0
               q += 1
               
          j += 1

def cA(x,y):
     a = np.array([[0.0,0.0]]*N)
     
     p = []
     for i in range(N):
          p.append([x[i],y[i]])
     
     p = np.array(p)
     
     for i in range(N):
          for j in range(N):
               if i != j:             
                    d = p[i]%L - p[j]%L
                    
                    r= np.linalg.norm(d)
                    
                    fr = 24 * (2*(1/r)**12 - (1/r)**6) / r**2
                    f = fr * d/r
                    
                    a[i] += f
                    a[j] -= f
                    
     return a

def grafica(xgt,ygt):
     plt.style.use("dark_background") 
     fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     l1.grid(color = "turquoise")
     l1.axhline(color = "red")
     l1.axvline(color = "red")
     for i in range(N):
          l1.plot(xgt[i],ygt[i],"--", color = "red")
     #l1.set_xlim(0,L)
     #l1.set_ylim(0,L)
     
     plt.show()

def metodoVerlet(t0,tf):
     global xgt # Matriz para guardar trayectoria de cada particula en x
     global ygt # Matriz para guardar trayectoria de cada particula en x
     
     xgt = []
     ygt = []
     gVI()
     gPI()
     
     for i in range(N):
          
          x0 = x[i]
          y0 = y[i]
          
          xn = x
          yn = y
          
          vx0 = vx[i]
          vy0 = vy[i]
          
          a0 = cA(x,y)
          ax0 = a0[i][0]
          ay0 = a0[i][1]
          
          xg = [x0]
          yg = [y0]

          while t0 < tf:
               #print(t0)
               x0 += vx0*h + (ax0*h**2)/2
               x0 %= L
               y0 += vy0*h + (ay0*h**2)/2
               y0 %= L
               
               xn[i] = x0
               yn[i] = y0
               
               a1 = cA(xn,yn)
               ax1 = a1[i][0]
               ay1 = a1[i][1]
               
               vx0 += ((ax1+ax0)*h)/2
               vy0 += ((ay1+ay0)*h)/2
               
               t0 += h

               xg.append(x0)
               yg.append(y0)
          
          xgt.append(xg)
          ygt.append(yg)
          t0 = 0
     
     #print(xgt[0])
     #grafica(xgt,ygt)
     
# Variables------------------------------
d = 2 # Dimenciones
N = 64 # Numero de particulas
L = 10 # Longitud de la celda cuadrada
T = 1.0 # Temperatura inicial
h = 0.001 # Tamaño de paso
k = 1#1.38e-23 # Constante de Boltzmann
m = 1#6.69e-11 # Masa del Argon
e = 1#1.65e-21 # Parametro de energia del Argon de Lennard-Jones
s = 1#3.4e-12 # Parametro de distancia del Argon de Lennard-Jones
t0 = 0 # tiempo inicial
tf = 0.02 # tiempo final

x = [0]*N
y = [0]*N

vx = [0]*N
vy = [0]*N

ax = [0]*N
ay = [0]*N

metodoVerlet(t0,tf)

plt.style.use("dark_background")
fig, l = plt.subplots(facecolor = "blue")

def update(i):
     l.clear()
     for i in range(N):
          l.plot(xgt[:i],ygt[:i],".", color = "red")
     l.set_xlim(0,L)
     l.set_ylim(0,L)
     
ani = animation.FuncAnimation(fig,update,frames=1000,interval = 10)

plt.show()