liste_1 = [1,4,2,7,35,84]
villes = ['Paris', 'Berlin']
liste_2 = [liste_1, villes]

# tuple, c'est comme une liste mais non modifiable !
# valeurs protégées 
# plus rapide en tant d'exécution si beaucoup de valeurs à parcourir 
tuple1 = (1, 2, 6, 7)

# INDEXING : acces valeur de sequence par index 
# debute par index 0 !
print(villes[0])
print(liste_1[-1]) # accès au dernier élément du tableau
print(liste_1[-2]) # accès à l'avant dernier élément du tableau 

# SLICING 
print(liste_1[0:3]) # peut s'écrire aussi print(liste_1[:3])
print(liste_1[2:]) # les élements après index 2 (2 inclus)
print(liste_1[::2]) # print par pas de 2
print(liste_1[::-1]) # print à l'envers 

# on peut faire pareil avec les string
prenom = 'Lucas'
print(prenom[:2])

# modification des valeurs
villes[0] = 'Dub'
print(*villes) # print les élements de la liste en séparant par espace

# manipulation des listes
villes.append('Londres') #ajout element à la fin
print(villes)
villes.insert(2, 'Madrid') # ajout element à un index spécifique 
print(villes)
villes_2 = ['Amsterdam', 'Rome']
villes.extend(villes_2)
print(villes) # insère les éléments d'une liste dans une autre
print(len(villes))  # nombre de valeurs dans la liste

# SORTING
villes.sort() # tri par ordre alphabétique
print(villes)
villes.sort(reverse=True) # trie par ordre inverse
print(villes)

print(villes.count('Madrid')) # nombre de fois où apparait Madrid 

if 'Madrid' in villes:
    print('Madrid is here')
else:
    print('Madrid is not here')

# affiche chaque index et élément de la liste
for index, valeur in enumerate(villes):
    print(index, valeur)


