"""
Nombre: P38-OscarCastro Dinamica Molecular 4
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
def cV(lx,ly): # Funcion -> Concatenacion Vertical
     l = []
     
     for i in range(len(lx)):
          l.append([lx[i],ly[i]])
          
     return np.array(l)
     
def cFP(z): # Funcion -> Condiciones De Frontera Periodicas
     z -= L*np.round(z/L)
     
     return z

def gVI(): # Funcion -> Generador De Velocidades Iniciales
     vx = [0]*N
     vy = [0]*N
     
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
     
     return cV(vx,vy)

def gPI(): # Funcion -> Genrador De Posiciones Iniciales
     x = [0]*N
     y = [0]*N
     
     j = 1
     q = 1
     
     for i in range(N):
          
          x[i] = q*((L)/(np.sqrt(N))) - (L)/(2*np.sqrt(N))
          y[i] = j*((L)/(np.sqrt(N))) - (L)/(2*np.sqrt(N))
          
          if j >= np.sqrt(N):
               j = 0
               q += 1
               
          j += 1
     
     return cV(x,y)

def cA(p): # Funcion -> Caculo de Aceleraciones
     ax = np.array([0.0]*N)
     ay = np.array([0.0]*N)
     
     for i in range(N):
          for j in range(N):
               if i != j:
                    dx = cFP(p[i][0] - p[j][0])
                    dy = cFP(p[i][1] - p[j][1])

                    r = np.sqrt(dx**2+dy**2)
                    
                    fr = 24 * (2*(1/r)**12 - (1/r)**6) / r**2
                    fx = fr * dx/r
                    fy = fr * dy/r

                    ax[i] += fx
                    ay[i] += fy
                    ax[j] -= fx
                    ay[j] -= fy
     
     return cV(ax,ay)

def cT(v): # Funcion -> Calculo de Temperatura
     
     v2ST = 0
     for i in range(N):
          v2ST += ((v[i][0])**2 + (v[i][1])**2)
          
     return v2ST/(d*N)
     
def grafica(x,y): # Funcion -> Grafica
      
     plt.style.use("dark_background") 
     fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     l1.set_title(f"Dinamica Molecular\nGas De Argon Diluido\nTemperatura Promedio", fontsize = 15)
     l1.set_xlabel(r"$tiempo$")
     l1.set_ylabel(r"$Temperatura$")
     l1.grid(color = "turquoise")
     l1.axhline(color = "red")
     l1.axvline(color = "red")
     l1.plot(x,y,".",color = "white")#,label =f"Temperatura promedios = {texto}")
     l1.legend(edgecolor = "turquoise", fontsize = 10)
     plt.show()

def metodoVerlet(p,v,t0,tf,Tg): # Funcion -> Metodo De Verlet
     t = [t0]
     while t0 < tf:
          a0 = cA(p)

          p += v*h + (a0*h**2)/2
          p = cFP(p)

          a1 = cA(p)

          v += ((a0 + a1)*h)/2

          t0 += h

          Tg.append(cT(v))
          t.append(t0)
          
          Tp = 0
          for i in range(len(Tg)):
               Tp += Tg[i]

          Tgp.append(Tp/len(Tg))
          
     return grafica(t,Tgp)
     
# Variables------------------------------
d = 2 # Dimenciones
N = 64 # Numero de particulas
L = 10 # Longitud de la celda cuadrada
T = 1.0 # Temperatura inicial
h = 0.01 # Tamaño de paso
k = 1#1.38e-23 # Constante de Boltzmann
m = 1#6.69e-11 # Masa del Argon
e = 1#1.65e-21 # Parametro de energia del Argon de Lennard-Jones
s = 1#3.4e-12 # Parametro de distancia del Argon de Lennard-Jones
t0 = 0 # Tiempo inicial
tf = 1 # Tiempo final
Tg = [] # Lista de Temperaturas
Tgp = []
p = gPI()
v = gVI()
Tg.append(cT(v))
Tgp = [cT(v)]


metodoVerlet(p,v,t0,tf,Tg)
