from pokemon import Pokemon

class Feu(Pokemon):
    def __init__(self, nom, niveau):
        Pokemon.__init__(self, nom, niveau, attaque=60, defense=5)
