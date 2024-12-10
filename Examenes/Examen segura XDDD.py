# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 13:29:31 2023

@author: Sergio Iglesias
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

G = 6.674e-11
m1 = 5.97e24
m2 = 7.342e22
m3 = 1.989e30
r0 = 1.495978707e11
v0 = 2.9783e4

x1 = r0
y1 = 0
x2 = r0 + 3.844e8
y2 = 0
vx1 = 0
vy1 = v0
vx2 = 0
vy2 = v0 + 1022

t = 0
dt = 60 * 60 * 24

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2.5e11, 2.5e11)
ax.set_ylim(-2.5e11, 2.5e11)
ax.set_aspect('equal')
ax.set_title('Orbita de la Tierra', fontsize=16)
ax.set_xlabel('x (m)', fontsize=14)
ax.set_ylabel('y (m)', fontsize=14)
ax.set_facecolor('#000022')

x1_list = []
y1_list = []
x2_list = []
y2_list = []

for j in range(365):
    r12 = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    r13 = np.sqrt(x1**2 + y1**2)
    r23 = np.sqrt(x2**2 + y2**2)
    
    ax1 = -G * m3 * x1 / r13**3 - G * m2 * (x1 - x2) / r12**3
    ay1 = -G * m3 * y1 / r13**3 - G * m2 * (y1 - y2) / r12**3
    ax2 = -G * m3 * x2 / r23**3 - G * m1 * (x2 - x1) / r12**3
    ay2 = -G * m3 * y2 / r23**3 - G * m1 * (y2 - y1) / r12**3
    
    vx1 += ax1 * dt
    vy1 += ay1 * dt
    vx2 += ax2 * dt
    vy2 += ay2 * dt
    
    x1 += vx1 * dt
    y1 += vy1 * dt
    x2 += vx2 * dt
    y2 += vy2 * dt

    t += dt
    
    x1_list.append(x1)
    y1_list.append(y1)
    x2_list.append(x2)
    y2_list.append(y2)

def animate(i):
    global x1, y1, x2, y2, vx1, vy1, vx2, vy2, t, dt

    ax.plot(x1_list[i], y1_list[i], 'bo', markersize=8)
    ax.plot(x2_list[i], y2_list[i], 'wo', markersize=4, markeredgecolor='k')
    ax.plot(x1_list[:i+1], y1_list[:i+1],'--', color ="b", markersize=8)
    ax.plot(x2_list[:i+1], y2_list[:i+1],'--', color ="w", markersize=4, markeredgecolor='k')
    
    ax.set_xlim(x1_list[i]-3.844e8*2, x1_list[i]+3.844e8*2)
    ax.set_ylim(y1_list[i]-3.844e8*2, y1_list[i]+3.844e8*2)

ani = FuncAnimation(fig, animate, range(len(x1_list)), interval=0)

plt.show()
