from normal import Normal
from feu import Feu
from eau import Eau
from terre import Terre
from combat import Combat

def menu():
    print("1. Lancer une partie")
    print("0. Quitter")
    choix = int(input("Entrez votre choix: "))
    return choix

def menu_choix_pokemon():
    print()

def main():
    while True:
        choix = menu()
        if choix == 1:
            pikachu = Normal("Pikachu", 4)
            carapuce = Eau("Carapuce", 8)
            combat = Combat(pikachu, carapuce)

            while not combat.est_finie():
                print("Tour de :", pikachu.get_nom())
                combat.attaquer(pikachu, carapuce)
                carapuce.afficher_infos()
                if combat.est_finie():
                    break

                print("Tour de :", carapuce.get_nom())
                combat.attaquer(carapuce, pikachu)
                pikachu.afficher_infos()

            print("Le vainqueur est :", combat.vainqueur())
            print("Le perdant est :", combat.perdant())

         
        if choix == 2:
            salamèche = Feu("Salamèche", 1)
            bulbizar = Terre("Bulbizar", 10)
            combat = Combat(salamèche, bulbizar)

            while not combat.est_finie():
                print("Tour de :", salamèche.get_nom())
                combat.attaquer(salamèche, bulbizar)
                bulbizar.afficher_infos()
                if combat.est_finie():
                    break

                print("Tour de :", bulbizar.get_nom())
                combat.attaquer(bulbizar, salamèche)
                salamèche.afficher_infos()

            print("Le vainqueur est :", combat.vainqueur())
            print("Le perdant est :", combat.perdant())


        elif choix == 0:
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
