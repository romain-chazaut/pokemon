from normal import Normal
from feu import Feu
from eau import Eau
from terre import Terre
from combat import Combat
from pokedex import Pokedex
import time


def menu():
    print("1. Lancer une partie")
    print("2. Choisir son Pokemon")
    print("0. Quitter")
    choix = int(input("Entrez votre choix: "))
    return choix
    
def choisir_pokemon(pokedex):
    print("Voici la liste des Pokemons disponibles :")
    for i, pokemon in enumerate(pokedex.pokemon_list):
        print(f"{i + 1}. {pokemon.get_nom()}")

    choix = int(input("Entrez le numéro du Pokemon choisi : "))
    return pokedex.pokemon_list[choix - 1]



def main():
    pokedex = Pokedex()
    pokemon_joueur = None
    while True:
        choix = menu()

        if choix == 1:
            if pokemon_joueur is None:
                pokemon_joueur = pokedex.choisir_pokemon()

            combat = Combat(pokemon_joueur, pokedex.choisir_pokemon())

            while not combat.est_finie():
                print("Tour de :", combat.pokemon1.get_nom())
                combat.attaquer(combat.pokemon1, combat.pokemon2)
                combat.pokemon2.afficher_infos()
                time.sleep(1)
                if combat.est_finie():
                    break

                print("Tour de :", combat.pokemon2.get_nom())
                combat.attaquer(combat.pokemon2, combat.pokemon1)
                combat.pokemon1.afficher_infos()
                time.sleep(1)

            print("Le vainqueur est :", combat.vainqueur())
            print("Le perdant est :", combat.perdant())

            pokemon_joueur = None

        elif choix == 2:
            pokemon_joueur = pokedex.choisir_pokemon()

        elif choix == 0:
            print("Au revoir !")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()
