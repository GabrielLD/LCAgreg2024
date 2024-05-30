# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 11:41:41 2023

@author: ledou
"""

import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.animation as anim
from matplotlib.widgets import Slider, Button, RadioButtons
##### (1) DÃ©finition de la fonction
def U(x):
    y = np.zeros(x.size)
    for i in range(x.size):
        
        y = A/x**12-C/x**6
    return y

def attractif(x):
    y = np.zeros(x.size)
    for i in range(x.size):
        y = -C/x**12
    return y

def repulsif(x):
    y = np.zeros(x.size)
    for i in range(x.size):
        y = A/x**12
    return y


##### (2) DÃ©finition des paramÃ¨tres A et B
# valeur extremales
Amin = 0.0001
Amax = 0.001
Cmin = 10
Cmax = 1000000
# Valeur initiale
A0 = Amax/2
C0 = Cmax/2
A = A0
C = C0
# Nom des paramÃ¨tres
Anom = "repulsif"
Bnom = "attractif"


##### (2) DÃ©finition de l'axe des x
# N est l nombre de points sur l'axe
xmin = 0.1
xmax = .15
N = 100000
x = np.linspace(xmin,xmax,N)

##### (3) DÃ©finition du graphique et des courbes

# le cadre
fig = plt.figure()
# ax=plt.axes(xlim=(0,1.),ylim=(-1.2,2.05))  #Axes x et y


# le graph A et ses courbes :

#ax_A = plt.subplot(211) #axes()
# nom des axes
plt.xlabel('LÃ©gende axe x (A)')
plt.ylabel('LÃ©gende axe y (A)')

courbe_A1, = plt.plot(x,U(x))
courbe_A2, = plt.plot(x,attractif(x))
courbe_B1, = plt.plot(x,repulsif(x))
# lÃ©gende
courbe_A1.set_label('courbe 1')
courbe_A2.set_label('courbe 2')

# le graph B et ses courbes :

#ax_B = plt.subplot(212) #axes()
# nom des axes
plt.xlabel('LÃ©gende axe x (B)')
plt.ylabel('LÃ©gende axe y (B)')

courbe_B1, = plt.plot(x,repulsif(x))
# lÃ©gende
courbe_B1.set_label('courbe 3')

plt.subplots_adjust(left = 0.1,bottom=0.25)
plt.legend()
# les curseurs
# premier slider
A_axSlider = plt.axes([0.2,0.07,0.7,0.05])
A_Slider = Slider(A_axSlider,Anom,Amin,Amax,A0)
# deuxiÃ¨me slider
B_axSlider = plt.axes([0.2,0.12,0.7,0.05])
B_Slider = Slider(B_axSlider,Bnom,Cmin,Cmax,C0)

##### fonction pour modifier les paramÃ¨tres et actulaiser la courbe
def update(val):
    global A, C
    # on change la valeur des paramÃ¨tres
    A = A_Slider.val
    C = B_Slider.val
    # on recalcul et on affiche la fonction
    courbe_A1.set_ydata(U(x))
    courbe_A2.set_ydata(attractif(x))
    courbe_B1.set_ydata(repulsif(x))
    plt.relim()
    plt.autoscale_view()
    plt.relim()
    plt.autoscale_view()

plt.ylim(-1,1)
A_Slider.on_changed(update)
B_Slider.on_changed(update)


plt.show()