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

def main():
    while True:
        choix = menu()
        if choix == 1:
            pikachu = Normal("Pikachu", 5)
            carapuce = Eau("Carapuce", 5)
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

        elif choix == 0:
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
