"""
Nombre: P33-OscarCastro Numeros Aleatorios
Fecha Inicio:
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random as rm

# Funciones------------------------------

def myRandom(r):
     a = 106
     c = 1283
     m = 6075
     r = (a*r + c) % m
     return r

def listaRamdom(r,n,T):
     i = 0
     y = []
     x = []
     z = []
     x1 = range(n)
     
     while i < n:
          r = myRandom(r)
          y.append(r)
          r = myRandom(r)
          x.append(r)
          
          i += 1
     
     x = np.array(x)/max(x)
     y = np.array(y)/max(y)
     
     #grafica(x1,x,y,T)
     
     grafica3d(x,y,T)
          
def grafica(x1,x,y,T):
     
     plt.style.use("dark_background")
     fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     l1.set_title(T+"\n"+r"$r_i$ vs $i$", fontsize = 10)
     l1.set_xlabel(r"$i$")
     l1.set_ylabel("$r_i$")
     l1.grid(color = "turquoise")
     l1.axhline(color = "red")
     l1.axvline(color = "red")
     l1.plot(x1[:100],y[:100],".", color = "white")
     
     fig, l2 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     l2.set_title(T+"\n"+r"$x$ vs $y$", fontsize = 10)
     l2.set_xlabel(r"$x$")
     l2.set_ylabel("$y$")
     l2.grid(color = "turquoise")
     l2.axhline(color = "red")
     l2.axvline(color = "red")
     l2.plot(x,y,".", color = "white")
     #l1.legend(edgecolor = "red", fontsize = 10)
     plt.show()

def grafica3d(x,y,T):
     plt.style.use("dark_background")
     fig = plt.figure()
     l3 = fig.add_subplot(projection = "3d")
     
     thetar = x*np.pi/2
     phir = y*np.pi/2
     thetar, phir = np.meshgrid(thetar,phir)
     
     theta = np.arange(0,np.pi/2,0.01)
     phi = np.arange(0,np.pi/2,0.01)
     theta , phi = np.meshgrid(theta,phi)
     
     X = np.sin(phi)*np.cos(theta)
     Y = np.sin(phi)*np.sin(theta)
     Z = np.cos(phi)
     
     x = np.sin(phir)*np.cos(thetar)
     y = np.sin(phir)*np.sin(thetar)
     z = np.cos(phir)
     
     #l3.plot_surface(X,Y,Z, color="blue")
     l3.scatter(x, y, z,".", color = "blue",lw = .1)
     l3.grid(color = "turquoise")
     l3.set_title(T)
     l3.set_xlabel('X')
     l3.set_ylabel('Y')
     l3.set_zlabel('Z')

     plt.show()
     
# Variables------------------------------
r0 = 1234
n = 60
T = "Numeros Aleatorios"

listaRamdom(r0,n,T)