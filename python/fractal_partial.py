# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 14:49:34 2017

@author: gualandi

DESCRIZIONE:
-----------
Per poter eseguire l'animazione dovete sostiuire alla funzione JuliaRec quella scritta da voi.
Lo script non è molto pulito per ora, ma dovrebbe dare l'effetto di animazione visto a lezione.

Per eseguirlo si devi aprire la "PowerShell" di Windows (per trovarla fare "cerca applicazione" in windows),
oppure il terminale (Max e Linux) e poi dovete andare nella cartella dove 
avete copiato questo script e da li scrivere il comando:

% python ./fractal_partial.py

A quel punto dovrebbe aprirsi una finestra con l'animazione.
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def JuliaSetRec(z, c, it, maxit=64):
    # DA COMPLETARE
    return 0
    
def JuliaSet(z, c=-0.413):
    return JuliaSetRec(z, c, 0)

def Update(i):
    global c, n
    print(round(c, 3))
    c = c - 0.01
    data = [scale*i for i in range(-n,n)]
    m = np.matrix([[JuliaSet(complex(i, j), c) for i in data] for j in data])
    M.set_array(m)
    return M,
    
n = 200
c = 0.745
#c = (-0.423) :+ 0.745 -- Dust
#--c = (0.45) :+ (-0.1428)
#--c = (0.285 :+ 0.01)
scale = 0.01
data = [scale*i for i in range(-n,n)]
m = np.matrix([[JuliaSet(complex(i, j), c) for i in data] for j in data])
fig = plt.figure(figsize=(5,5))
M = plt.imshow(m, extent=(scale*n, -scale*n, scale*n, -scale*n), animated=True, cmap='jet')
ani = animation.FuncAnimation(fig, Update, interval=50, blit=True)
plt.show()