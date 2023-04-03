from normal import Normal
from feu import Feu
from eau import Eau
from terre import Terre
from pokedex import Pokedex
from pokemon import Pokemon

class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.__pokedex = Pokedex()  # Initialise une instance de Pokedex
        self.pokemon1 = pokemon1    # Initialise les 2 Pokemon en combat
        self.pokemon2 = pokemon2

    def est_finie(self):
        return not (self.pokemon1.est_vivant() and self.pokemon2.est_vivant())     #Vériefie si le combat est terminé (l'1 des pokemon n'a plus de PV)

    def vainqueur(self):                        
        if self.pokemon1.est_vivant():                  
            return self.pokemon1.get_nom()                  #Retourne le nom du vainqueur (Le Pokemon encore en vie)
        else:
            return self.pokemon2.get_nom()

    def perdant(self):
        if self.pokemon1.est_vivant():
            return self.pokemon2.get_nom()              # Retourne le nom du perdant (Le Pokemon ayant perdu tous ses PV)
        else:
            return self.pokemon1.get_nom()

    def calculer_degats(self, attaquant, defenseur):
        multiplicateur = 1

                                                                                            #Calcule des dégats infligés en prenant en compte les types de Pokémon.
        if isinstance(attaquant, Eau) and isinstance(defenseur, Terre):
            multiplicateur = 0.5
        elif isinstance(attaquant, Terre) and isinstance(defenseur, Eau):           
            multiplicateur = 2
        if isinstance(attaquant, Feu) and isinstance(defenseur, Terre):
            multiplicateur = 2
        elif isinstance(attaquant, Terre) and isinstance(defenseur, Feu):
            multiplicateur = 0.5
        if isinstance(attaquant, Eau) and isinstance(defenseur, Feu):
            multiplicateur = 2
        elif isinstance(attaquant, Feu) and isinstance(defenseur, Eau):
            multiplicateur = 0.5
        if isinstance(attaquant, Normal) and isinstance(defenseur, Eau):
            multiplicateur = 0.75
        elif isinstance(attaquant, Eau) and isinstance(defenseur, Normal):
            multiplicateur = 1
        if isinstance(attaquant, Normal) and isinstance(defenseur, Feu):
            multiplicateur = 0.75
        elif isinstance(attaquant, Feu) and isinstance(defenseur, Normal):
            multiplicateur = 1
        if isinstance(attaquant, Normal) and isinstance(defenseur, Terre):
            multiplicateur = 0.75
        elif isinstance(attaquant, Terre) and isinstance(defenseur, Normal):
            multiplicateur = 1

        min_degats = 50
        attaque = attaquant.calculer_attaque()
        defense = defenseur.calculer_defense()
        
        
        return max((attaque * multiplicateur - defense) + 10, min_degats)  #Retourne les dégats infligés, en tenant compte du multiplicateur et des statistiques d'attaque et de défense.

    def attaquer(self, attaquant, defenseur):
        degats = self.calculer_degats(attaquant, defenseur)       #Calcule les dégats infligés par l'attaquant au défenseur
        degats_reduits = max(degats - defenseur.defense, 0)       #Réduit les dégats en fonction de la défense du défenseur
        defenseur.enlever_PV(degats_reduits)                      #En lève les PV du défenseur en fonction des dégats infligés



