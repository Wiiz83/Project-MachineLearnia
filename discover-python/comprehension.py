# tous les carrés de 0 à 9
# algo prennant 7.44sec
liste1 = []
for i in range(10):
    liste1.append(i**2)
print(liste1)

# même chose en une seule ligne 
# processus plus rapide que la méthode au dessus
# algo prennant 6.02secs
liste2 = [i**2 for i in range(10)]
print(liste2)

# création d'une nested liste
liste3 = [[i for i in range(3)] for j in range(3)]
print(liste3)


prenoms = ['Pierre', 'Jean', 'Julie', 'Sophie']
dico = {key:value for key, value in enumerate(prenoms)}
print(dico)
print(dico.keys())
print(dico.values())

# création d'un dictionnaire d'association prenom age si l'age est supérieur à 30
ages = [24, 62, 10, 23]
dico2 = {prenom: age for prenom, age in zip(prenoms, ages) if age > 30}
print(dico2)

# tuple comprehension
tuple1 = (i**2 for i in range(10))
print(tuple1) # affiche <generator object <genexpr> at 0x000002C69BE9E948> qui est un générateur 

# attention les termes tuple, list et dict sont des termes protégés par Python

def trier(classeur, nombre):
    if nombre > 0:
        classeur['positif'].append(nombre)
    else:
        classeur['negatif'].append(nombre)
    return classeur

classeur = {
        "positif" : [],
        "negatif" : [],
        }
print(trier(classeur, -4))


# créer un dictionnaire avec technique dict comprehenstion 
# dictionnaire k:v
# k = 0 - 20
# v = k**2
listkeys = [i for i in range(0, 20)]
listvalues = [i**2 for i in range(0, 20)]
dicocarres = {key:value for key, value in zip(listkeys, listvalues)}
print(dicocarres)

# plus rapide, plus court, plus efficace :
dicocarres2 = {
            str(k) : k**2 for k in range(0, 20)
        }
print(dicocarres2)
