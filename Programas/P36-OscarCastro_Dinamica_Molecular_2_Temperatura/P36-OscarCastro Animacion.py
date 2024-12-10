"""
Nombre: P36-OscarCastro Dinamica Molecular 2 Temperatura
Fecha Inicio:
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

-------------Metodo de Euler----------------

"""

# Librerias
from tkinter import *
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random as rm

# Funciones de Calculos Matematicos

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
          v2ST += (v[i][0])**2 + (v[i][1])**2
          
     return v2ST/(d*N)

def metodoVerlet(p,v,t0,Tg): # Funcion -> Metodo De Verlet
     a0 = cA(p)
     
     p += v*h + (a0*h**2)/2
     p = cFP(p)
     
     a1 = cA(p)
     
     v += ((a0 + a1)*h)/2
     
     t0 += h
     
     Tg = cT(v)
     
     return p,Tg,t0 

#Variables------------------------------

d = 2 # Dimenciones
N = 64 # Numero de particulas
L = 10 # Longitud de la celda cuadrada
T = 1.0 # Temperatura inicial
h = 0.01 # Tamaño de paso
k = 1#1.38e-23 # Constante de Boltzmann
m = 1#6.69e-11 # Masa del Argon
e = 1#1.65e-21 # Parametro de energia del Argon de Lennard-Jones
s = 1#3.4e-12 # Parametro de distancia del Argon de Lennard-Jones
t0 = 0 # tiempo inicial

p = gPI()
v = gVI()
Tg = cT(v)
Tp = Tg
j = 1

# Grafica
plt.style.use("dark_background")
fig, (l1,l2) = plt.subplots(1,2,facecolor = "blue")
l1.set_title(f"Dinamica Molecular\nGas De Argon Diluido\nTiempo = {round(t0,3)}s", fontsize = 15)
l2.set_title(f"Dinamica Molecular\nGas De Argon Diluido\nTemperatura", fontsize = 15)

# Funcion es para animacion, Bones y deslizadores
def update(i):
     global p,v,t0,Tg,Tp,j
     j += 1
     
     p,Tg,t0 = metodoVerlet(p,v,t0,Tg)
     
     l1.clear()
     l1.set_title(f"Dinamica Molecular\nGas De Argon Diluido\nTiempo = {round(t0,3)}s", fontsize = 15)
     l1.set_xlabel(r"x(t)")
     l1.set_ylabel(r"y(t)")
     l1.plot(p[:i,0],p[:i,1],"o", color = "purple",lw = 10, ms = 10)
     l1.set_xlim(-L/2,L/2)
     l1.set_ylim(-L/2,L/2)
     
     Tp += Tg
     
     l2.set_title(f"Dinamica Molecular\nGas De Argon Diluido\nTemperatura - Temp. Prom = {round(Tp/j,3)}", fontsize = 15)
     l2.set_xlabel(r"$Tiempo$")
     l2.set_ylabel(r"$Temperatura$")
     l2.axhline(color = "red")
     l2.axvline(color = "red")
     l2.plot(t0,Tg,".", color = "Purple")
     
def Iniciar(): # Funcion del boton Iniciar
     global ani 
     ani = animation.FuncAnimation(fig,update,range(0,int(N*60e3),N), interval = 0)
     canvas.draw()
     
def Pausar(): # Funcion del boton Pausar
     ani.event_source.stop()
     
def Reanudar(): # Funcion del boton Reanudar
     ani.event_source.start()

# Creacion de ventana
raiz = Tk()
raiz.title("Dinamica Molecular")

wtotal = raiz.winfo_screenwidth()
htotal = raiz.winfo_screenheight()

raiz.geometry(str(wtotal-10)+"x"+str(htotal))
raiz.config(bg = "blue")

#Funciones de Menu o de ventanas emergentes
def InfoAcercaDe():
     messagebox.showinfo("Creador", "Oscar Joel Castro Contreras\n------ Ingeniero Físico -------\n----------  UA de C  -----------")

def InfoProducto():
     messagebox.showinfo("Programa", "Dinamica Molecular, Gas De Argon Diluido")

def Descripcion():
     messagebox.showinfo("Descripción", "Este programa usa el método de Verlet para simular en 2D, el movimiento de las partículas que interaccionan entre si del gas de Argón diluido, por medio del potencial de Lennard Jones y también en el transcurso de la simulación va calculando la energía del sistema de partículas.")

def Instrucciones():
     messagebox.showinfo("Instrucciones", "1.- Pulse el botón “Iniciar”, se observará como inicia la animación, si desea pausar o reanudar la animación pulse los botones “Pausar” o “Reanudar”")

def AccionSalir():
     v = messagebox.askokcancel("Salir", "¿Deseas salir de la animacion?")
     if v == True:
          raiz.destroy()

# Menu
BarraMenu = Menu(raiz, bg = "blue", fg = "#03f943")
raiz.config(menu = BarraMenu, width = wtotal, height = htotal)

InformacionMenu = Menu(BarraMenu, tearoff = 0)
BarraMenu.add_cascade(label = "Información", menu = InformacionMenu)

InformacionMenu.add_command(label = "Acerca de...", command = InfoAcercaDe)
InformacionMenu.add_command(label = "Programa", command = InfoProducto)
InformacionMenu.add_command(label = "Descripcion", command = Descripcion)
InformacionMenu.add_command(label = "Instrucciones", command = Instrucciones)
InformacionMenu.add_command(label = "Salir", command = AccionSalir)

# Creacion del cuadro de la ventana o widget
frame = Frame(raiz)
frame.pack(fill = "both", expand = "True")
frame.config(bg = "blue")

# Variable para botones
RadBot = IntVar()

# Colocacion de la grafica en el frame
canvas = FigureCanvasTkAgg(fig, master = frame)
canvas.get_tk_widget().pack(padx = 5, pady = 5, fill = "both", expand = "True")

# Creacion de botones
BotonIniciar = Button(frame, text = "Iniciar", width = 30, border = 0 , height = 5 ,command = Iniciar)
BotonIniciar.pack(pady = 5, side = "left", expand = "True")
BotonIniciar.config(fg = "#03f943", bg = "black")

BotonPausar = Button(frame, text = "Pausar", width = 30, border = 0 , height = 5 ,command = Pausar)
BotonPausar.pack(pady = 5, side = "left", expand = "True")
BotonPausar.config(fg = "#03f943", bg = "black")

BotonReanudar = Button(frame, text = "Reanudar", width = 30, border = 0 , height = 5 ,command = Reanudar)
BotonReanudar.pack(pady = 5, side = "left", expand = "True")
BotonReanudar.config(fg = "#03f943", bg = "black")

raiz.mainloop()