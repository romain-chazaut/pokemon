import pokemon

class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def est_vivant(self, pokemon):
        return pokemon.PV > 0

    def nom_du_vainqueur(self):
        if not self.est_vivant(self.pokemon1):
            return self.pokemon2.nom
        elif not self.est_vivant(self.pokemon2):
            return self.pokemon1.nom
        else:
            return None

    def multiplier_puissance_attaque(self, attaquant, defenseur):
        multiplicateur = 1
        if attaquant.type == "Eau" and defenseur.type == "Terre":
            multiplicateur = 0.5
        return attaquant.puissance_attaque * multiplicateur

    def attaque(self, attaquant, defenseur):
        puissance_attaque = self.multiplier_puissance_attaque(attaquant, defenseur)
        degats = puissance_attaque - defenseur.defense
        if degats > 0:
            defenseur.PV -= degats

    def nom_du_perdant(self):
        if not self.est_vivant(self.pokemon1):
            return self.pokemon1.nom
        elif not self.est_vivant(self.pokemon2):
            return self.pokemon2.nom
        else:
            return None

def menu():
    print("Bienvenue dans le jeu de Pokémon !")
    print("1. Lancer une partie")

    choix = int(input("Choisissez une option : "))

    if choix == 1:
        # Créez ici les objets Pokémon et initialisez leurs attributs (nom, type, PV, puissance d'attaque, défense)
        # Exemple :
        tortank = pokemon.Pokemon("tortank", "eau", 100, 20, 10)
        dracofeu = pokemon.Pokemon("dracofeu", "feu", 100, 15, 12)

        combat = Combat(tortank, dracofeu)

        while combat.nom_du_vainqueur() is None:
            combat.attaque(tortank, dracofeu)
            if combat.nom_du_vainqueur() is not None:
                break

            combat.attaque(tortank, dracofeu)

        print("Le vainqueur est :", combat.nom_du_vainqueur())
        print("Le perdant est :", combat.nom_du_perdant())

if __name__ == "__main__":
    menu()
