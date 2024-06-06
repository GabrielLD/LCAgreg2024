# -*- coding: utf-8 -*-
"""
Created on Tue May  2 16:26:07 2023

@author: Gabriel
"""

from pylab import * #import des bibliothèques

DHi = 29*1000 #en J/mol
DHj = 34.9*1000 #en J/mol
Tebi = 342 #en K
Tebj = 399 #en K
Ps = 1.0 #en bar
R = 8.314 #en J/K/mol

def Pi(T):#pression se vapeur saturante de i en bar
    return Ps*np.exp(DHi/R*(1/Tebi-1/T))
def Pj(T):#pression se vapeur saturante de j en bar
    return Ps*np.exp(DHj/R*(1/Tebj-1/T))
def xjliq(T):#fraction molaire de j dans la phase liquide
    return ((Ps-Pi(T))/(Pj(T)-Pi(T)))
def xjvap(T):#fraction molaire de j dans la phase vapeur
    return xjliq(T)*Pj(T)/Ps

T = np.linspace(Tebi,Tebj,200)#création d’une liste de 200 points
plt.plot(xjliq(T),T,'-', label = 'courbe d ébullition') #tracé courbe d’éb
plt.plot(xjvap(T),T, ':', label = 'courbe de rosée')#tracé courbe de rosée
plt.legend()#Affichage de la légende
plt.grid()#Affichage de la grille
plt.xlabel('$x_{n-octane}$')#Titre de l’axe des abscisses
plt.ylabel('T/K')#Titre de l’axe des ordonnées
plt.show()#Affichage d