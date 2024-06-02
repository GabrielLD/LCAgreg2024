#### Définition de la procédure de recherchedu réactif limitant ####
#### pour l'équation de réaction : aA A + aB B = aC C + aD D
#MnO4 = #input('quantité initiale de A en mol :')
nMnO4 = 2E-4# mol/L
#Fe = #input('quantité initiale de B en mol :')
nFe = 5E-4# mol/L
#aMnO4 = input('a:')
aMnO4 = 1#float(a)
#b = input('b :')
aFe = 5#float(b)
def react_lim(aA,aB,nA,nB) :
    x=0             # Initialisation de l'avancement
    dx=0.00001      # Incrément d'avancement
    qA=[nA]         # Liste stockant les quantités de matière successives de A
    qB=[nB]         # Idem pour B
    RL=[]           # Liste qui stockera le nom du réactif limitant
    while qA[-1]>0 and qB[-1]>0 :
        x=x+dx
        qA.append(nA-aA*x)
        qB.append(nB-aB*x)
    if qA[-1]<=0 :
        RL.append("[MnO4]")
        print("Le réactif limitant est le permanganate")
    if qB[-1]<=0 :
        RL.append("[Fe]")
        print("Le réactif limitant est le Fer")
    return(RL,round(x,4))
print(react_lim(aMnO4,aFe,nMnO4,nFe))