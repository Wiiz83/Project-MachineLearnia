x = -3
print(abs(x)) # retourne la valeur absolue 

y = 3.94
print(round(y)) # retourne l'arrondie

liste = [0, 23, 14, -19]
print(max(liste)) # retourne le max de la liste
print(min(liste)) # retourne le min de la liste 
print(len(liste)) # retourne la longueur de la liste
print(sum(liste)) # retourne la somme des valeurs de la liste

liste2 = [True, True, False]
print(all(liste2)) # retourne true si toutes les valeurs = à true
print(any(liste2)) # retourne rue si il y a au moins un true 

x = 10 
print(type(x)) # retourne le type de la variable donc integer 
x = str(x)
print(type(x))
x = float(x)
print(type(x))

liste1 = [0, 61, 63, 243]
tuple1 = tuple(liste1)
print(tuple1) # conversation d'une liste en tuple 
liste1 = list(tuple1)
print(liste1) # conversation d'un tuple en liste 
print(type(liste1))

inventaire = {
        "bananes" : 5000,
        "pommes" : 2000,
        "fraises" : 1000
        }
list2 = list(inventaire.keys())
print(list2)
list3 = list(inventaire.values())
print(list3)

# input() pour demander à l'utilisateur d'écrire qq chose
z = int(input('Entrez un nombre : '))
i = z+10
print(i)

# format() pour ajouter des variables dans une string 
x = 25
ville = 'Paris'
message = "la température est de {} degC à {}".format(x, ville)
print(message)
message = f"la température est de {x} degC à {ville}"
print(message)

# manipulation de fichier 
f = open('fichier.txt', 'w')
f.write('bonjour')
f.close()

f = open('fichier.txt', 'r')
print(f.read())
f.close()

# pas besoin de f.close ici car fermeture auto
with open('fichier.txt', 'r') as f :
    print(f.read())

# écrire les carrés de 1 à 10 dans un fichier 
with open('fichier.txt', 'w') as f :
    for i in range(10):
        f.write('{}^2 = {}  \n'.format(i, i**2))

# retranscrire les carrés du fichier précédents dans une liste
liste1 = []
with open('fichier.txt', 'r') as f :
    liste1 = f.read()
print(liste1)

import glob

filenames = glob.glob('*.txt')
dico = {}
for file in filenames :
    with open(file, 'r') as f:
        dico[file] = f.read().splitlines()
print(dico) # la clé est le nom du fichier, le contenu sont les lignes du fichier