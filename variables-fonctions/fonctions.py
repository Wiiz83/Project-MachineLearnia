# lambda généralement utilisé pour des calculs mathématiques

# fonction f qui renvoi le carré d'un paramètre
f = lambda x: x**2
print(f(3))

# fonction g qui renvoi le carré d'un paramètre plus un second 
g = lambda x, y: x**2 + y
print(g(3, 2))

# autre type de déclaration de fonction plus complexe 

def e_potentielle(masse, hauteur, g = 9.81): # g est une constante
    E = masse * hauteur * g
    print(E, 'Joules') # séparateur de chaine dans print est virgule
    return E

resultat = e_potentielle(2, 2)
print(resultat, 'J')