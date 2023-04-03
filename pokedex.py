
from normal import Normal
from feu import Feu
from eau import Eau
from terre import Terre

class Pokedex:               # Création de la classe Pokédex
    def __init__(self):
        self.__pokemon_list = [
            Normal("Rattata", 20),                  
            Normal("Pikachu", 25),  
            Feu("Salamèche", 40),                       #Inisialisation de la liste des Pokemon disponibles
            Feu("Dracaufeu", 80),
            Eau("Carapuce", 24),
            Eau("Léviator", 70),
            Terre("Taupiqueur", 75),
            Terre("Golem", 67)
        ]

    def choisir_pokemon(self):                  #Métholde pour choisir un Pokemon à partir de la liste
        print("Voici la liste des Pokémon disponibles :")  
        for i, pokemon in enumerate(self.__pokemon_list):
            print(f"{i + 1}. {pokemon.get_nom()}")

        choix = int(input("Entrez le numéro du Pokémon choisi : "))  #Demande à l'utilisateur de choisir Pokemon.
        return self.__pokemon_list[choix - 1]