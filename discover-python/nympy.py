import numpy as np
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html

tableau = np.array([1,2,3])
print(tableau)
print(tableau.ndim) # affiche la dimension du tableau : 1 
print(tableau.shape) # affiche un tuple (3,) car 3 lignes et 0 colonne 

tab2 = np.zeros((3,4))
print(tab2.shape)
print(tab2)
print(type(tab2.shape))

tab3 = np.ones((3,4))
print(tab3)

tab4 = np.full((6,4), 2)
print(tab4)

np.random.seed(0) # générer toujours le même aléatoire 
tab5 = np.random.randn(3,4) # génère un tableau de nombres aléatoires respectant une loi normale centrée en 0
print(tab5)

tab6 = np.eye(4) # création d'une matrice identité (valeurs en diagonales)
print(tab6)

tab7 = np.linspace(0,10,20) # début, fin, quantité - 20 éléments réparties entre 0 et 10
print(tab7)

tab8 = np.arange(0,10,0.5) # début, fin, pas - de 0 à 10 avec un pas spécifique pour l'incrémentation 
print(tab8)

# des valeurs float plus précises mais plus longues à créer et à manipuler 
tab9 = np.linspace(0,10,20,dtype=np.float16)
print(tab9)

# fusion de tableaux de façon horizontale 
tab10 = np.hstack((tab2, tab3))
print(tab10)

# fusion de tableaux de façon verticale 
tab11 = np.vstack((tab2, tab3))
print(tab11)

# pour la fusion de deux tableaux peu importe leurs dimensions 
tab12 = np.concatenate((tab2, tab3), axis=1)
print(tab12)

# remaniement de la forme du tableau : changer les dimensions 
tab12 = tab12.reshape((6, 4))
print(tab12)

tab13 = np.array([1,2,3])
print(tab13.shape) # affiche (3,)
tab13 = tab13.reshape((tab13.shape[0], 1))
print(tab13.shape) # affiche (3,1) : meilleur pour la manipulation 
tab13 = tab13.squeeze() # enleve les dimensions 1
print(tab13.shape) # affiche (3,)

# aplatir un tableau à une seule dimension 
print(tab12)
tab12 = tab12.ravel();
print(tab12)

# créer une matrice aléatoire de dimensions m x n
def initialisation(m,n) :
    # m : nombre de lignes
    # n : nombre de colonnes
    # retourne une matrice aléatoire (m, n+1)
    # avec une colonne biaire remplie de 1 tout à droite
    # conseils : utiliser random.randn, concatenate
    tableauRandom = np.random.randn(m, n)
    tabOnlyOnes = np.ones((m,1))
    tabConcatenate = np.concatenate((tableauRandom, tabOnlyOnes), axis=1)
    return tabConcatenate

print(initialisation(2, 2))


