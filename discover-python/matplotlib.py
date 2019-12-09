# Matplotlib propose 2 méthodes à ne pas mélanger :
# - prog orientée objet 
# - méthode plus basique plt.plot 

import matplotlib.pyplot as plt 
import numpy as np

x = np.linspace(0, 2, 10) # 10 points allant de 0 à 2
y = x**2 # carré de x

# graphique courbe, x et y doivent avoir les mêmes dimensions !
# c = couleur de la ligne 
# lw = épaisseur de la ligne
# ls = style de la ligne 
plt.figure(figsize=(12, 8)) # création de la fenêtre de travail 
plt.plot(x, y, c='red', lw=3, ls='--')  # création du graphique 
plt.show()

