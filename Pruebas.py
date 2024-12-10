import matplotlib.pyplot as plot
import random as rm
import numpy as np

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
     
     return np.abs(vx)

N = 64
d = 2
k = 1
T = 1
     
intervalos = np.linspace(0,3,N) #calculamos los extremos de los intervalos

print(intervalos)

plot.hist(x=gVI(), bins=intervalos, color='#F2AB6D', rwidth=0.85)
plot.title('Histograma de edades - matplotlib - codigopiton.com')
plot.xlabel('Edades')
plot.ylabel('Frecuencia')
plot.xticks(intervalos)

plot.show() #dibujamos el histograma