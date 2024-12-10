
import numpy as np
import matplotlib.pyplot as plt
def F(ecuacion,r):
     global s,E,m
     s = 3.4e-10
     E = 1.65e-21
     m = 6.69e-26
     return eval(str(ecuacion))

r = np.linspace(0,3,10000)

u = "4*((1/r)**12 - (1/r)**6)"

fu = "24/(r**2)*(2*(1/r)**12 - (1/r)**6)"

plt.style.use("dark_background") 
fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")

l1.set_title("Potencial De Lennard-Jones", fontsize = 12)
l1.set_xlabel(r"$r/\sigma$")
l1.set_ylabel(r"$u(r)/\epsilon$")
l1.grid(color = "turquoise")
l1.axhline(color = "red")
l1.axvline(color = "red")
l1.plot(r,F(u,r), color = "yellow")
l1.set_ylim(-1.1,5)
l1.set_xlim(-0.05,3)

fig, l2 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
l2.set_title(r"Fuerza Correspondiente Al Potencial De Lennard-Jones", fontsize = 12)
l2.set_xlabel(r"$r/\sigma$")
l2.set_ylabel(r"$f(r)/\epsilon$")
l2.grid(color = "turquoise")
l2.axhline(color = "red")
l2.axvline(color = "red")
l2.plot(r,F(fu,r), color = "yellow")
l2.set_ylim(-6,10)
l2.set_xlim(0,3)

plt.show()