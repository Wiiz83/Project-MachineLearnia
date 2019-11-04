# association clé valeur
# la clé est unique dans le dictionnaire 
dictionnaire1 = {
        "chien": "dog",
        "chat": "cat",
        "souris": "mouse"
        }

dictionnaire2 = {
        "dog": "chien",
        "cat": "chat",
        "mouse": "souris"
        }

# nested dictionnaire
dictionnaire3 = {
        "dict1": dictionnaire1,
        "dict2": dictionnaire2
        }

print(dictionnaire3.values())

print(dictionnaire3.keys())

print(len(dictionnaire3))

dictionnaire2["dog"] = "ouaf"

print(dictionnaire2.values())

print(dictionnaire2.get("dog"))
print(dictionnaire2.get("oiseau")) # renvoi none car n'existe pas

for key, value in dictionnaire1.items():
    print(key, value)