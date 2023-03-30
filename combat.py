from normal import Normal
from feu import Feu
from eau import Eau
from terre import Terre

class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def est_finie(self):
        return not (self.pokemon1.est_vivant() and self.pokemon2.est_vivant())

    def vainqueur(self):
        if self.pokemon1.est_vivant():
            return self.pokemon1.get_nom()
        else:
            return self.pokemon2.get_nom()

    def perdant(self):
        if self.pokemon1.est_vivant():
            return self.pokemon2.get_nom()
        else:
            return self.pokemon1.get_nom()

    def calculer_degats(self, attaquant, defenseur):
        multiplicateur = 1

        # Ajouter les autres conditions ici en fonction des types de Pokémon
        if isinstance(attaquant, Eau) and isinstance(defenseur, Terre):
            multiplicateur = 0.5
        elif isinstance(attaquant, Terre) and isinstance(defenseur, Eau):
            multiplicateur = 2

        return attaquant.attaque * multiplicateur

    def attaquer(self, attaquant, defenseur):
        degats = self.calculer_degats(attaquant, defenseur)
        degats_reduits = max(degats - defenseur.defense, 0)
        defenseur.enlever_PV(degats_reduits)
