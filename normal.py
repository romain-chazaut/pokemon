import pokemon
import feu
import eau
import terre
import combat

class Normal(pokemon.Pokemon):
    def __init__(self, nom, puissance, defense):
        self.__nom = nom
        self.type = "Normal"
        self.puissance = puissance
        self.defense = defense
        self.__PV = 100

normal_pokemon = Normal("Normal", 50, 30)
print("Nom", normal_pokemon.__nom)
print("Type:", normal_pokemon.type)
print("PV:", normal_pokemon.__PV)
print("Puissance:", normal_pokemon.puissance)
print("Défense:", normal_pokemon.defense)

normal = Normal
pokemon1 = normal.Normal("Pokemon", 50, 30)
pokemon2 = feu.Feu("Pokemon2", 60, 40)
     
