"""
Nombre: P38-OscarCastro Dinamica Molecular 4
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
     rcl = np.sqrt(T/kep)
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

def cP(p,Tg,a1): # Funcion -> Calculo de Presion
     rijS = 0
     for i in range(N):
          for j in range(N):
               if i != j:
                    ri = np.sqrt((p[i][0])**2 + (p[i][1])**2)
                    rj = np.sqrt((p[j][0])**2 + (p[j][1])**2)
                    rij = ri-rj
                    rijS += cFP(rij)
                    
     a1S = 0
     for i in range(N):
          a1S += np.sqrt((a1[i][0])**2 + (a1[i][1])**2)
     
     pS = rijS*a1S
          
     return (N*Tg + pS/d)/(L**2)

def metodoVerlet(p,v,t0,Tg): # Funcion -> Metodo De Verlet
     a0 = cA(p)
     
     p += v*h + (a0*h**2)/2
     p = cFP(p)
     
     a1 = cA(p)
     
     v += ((a0 + a1)*h)/2
     
     t0 += h
     
     Tg = cT(v)
     
     pr = cP(p,Tg,a1)
     
     return p,Tg,pr,t0 

#Variables------------------------------

d = 2 # Dimenciones
N = 64 # Numero de particulas
L = 10 # Longitud de la celda cuadrada
T = 1.0 # Temperatura inicial
h = 0.01 # Tamaño de paso
k = 1#1.38e-23 # Constante de Boltzmann
m = 1#6.69e-11 # Masa del Argon
e = 1.65e-21 # Parametro de energia del Argon de Lennard-Jones
s = 3.4e-12 # Parametro de distancia del Argon de Lennard-Jones
t0 = 0 # tiempo inicial

p = gPI()
v = gVI()
Tg = cT(v)
prM = 0
j = 1

# Grafica
plt.style.use("dark_background")
fig = plt.figure(facecolor = "blue")

l1=fig.add_subplot(121)
for i in range(N):
     l1.plot(cFP(p[i][0]),cFP(p[i][1]),"o", color = "purple",lw = 10, ms = 10)

l2=fig.add_subplot(222)

l3=fig.add_subplot(224)

#plt.tight_layout()

l1.set_title(f"Dinamica Molecular\nGas De Argon Diluido\nTiempo = {round(t0,3)}s", fontsize = 10)
l2.set_title(f"Presion media UR", fontsize = 10)
l3.set_title(f"Presion media Pa", fontsize = 10)

# Funcion es para animacion, Bones y deslizadores
def update(i):
     global p,v,t0,Tg,prM,j
     j += 1
     
     p,Tg,pr,t0 = metodoVerlet(p,v,t0,Tg)
     
     l1.clear()
     l1.set_title(f"Dinamica Molecular\nGas De Argon Diluido\nTiempo = {round(t0,3)}s", fontsize = 10)
     l1.set_xlabel(r"x(t)")
     l1.set_ylabel(r"y(t)")
     l1.plot(p[:i,0],p[:i,1],"o", color = "purple",lw = 10, ms = 10)
     l1.set_xlim(-L/2,L/2)
     l1.set_ylim(-L/2,L/2)
     
     prM += pr
     
     l2.set_title(f"Presion media UR = {round(prM/j,3)}", fontsize = 10)
     l2.set_ylabel(r"$Presion (UR)$")
     l2.axhline(color = "red")
     l2.axvline(color = "red")
     l2.plot(t0,prM/j,".", color = "Purple")
     
     l3.set_title(f"Presion media Pa = {round((prM/j)*((e)/(s**2)),4)}", fontsize = 10)
     l3.set_xlabel(r"$Tiempo$")
     l3.set_ylabel(r"$Presion (Pa)$")
     l3.axhline(color = "red")
     l3.axvline(color = "red")
     l3.plot(t0,(prM/j)*((e)/(s**2)),".", color = "Purple")
     
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
raiz.config(background = "blue")

#Funciones de Menu o de ventanas emergentes
def InfoAcercaDe():
     messagebox.showinfo("Creador", "Oscar Joel Castro Contreras\n------ Ingeniero Físico -------\n----------  UA de C  -----------")

def InfoProducto():
     messagebox.showinfo("Programa", "Dinamica Molecular, Gas De Argon Diluido")

def Descripcion():
     messagebox.showinfo("Descripción", "Este programa usa el método de Verlet para simular en 2D, el movimiento de las partículas que interaccionan entre si del gas de Argón diluido, por medio del potencial de Lennard Jones y también en el transcurso de la simulación va calculando la presión del sistema de partículas.")

def Instrucciones():
     messagebox.showinfo("Instrucciones", "1.- Pulse el botón “Iniciar”, se observará como inicia la animación, si desea pausar o reanudar la animación pulse los botones “Pausar” o “Reanudar”")

def AccionSalir():
     v = messagebox.askokcancel("Salir", "¿Deseas salir de la animacion?")
     if v == True:
          raiz.destroy()

# Menu
BarraMenu = Menu(raiz, background = "blue", fg = "#03f943")
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