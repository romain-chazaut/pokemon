from pokemon import Pokemon

class Feu(Pokemon):                         #Création de la classe feu qui hérite de la classe Pokemon
    def __init__(self, nom, niveau):
        Pokemon.__init__(self, nom, niveau, attaque_base= 15, defense_base= 10)
