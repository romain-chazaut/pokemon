from pokemon import Pokemon

class Eau(Pokemon):
    def __init__(self, nom, niveau):
        Pokemon.__init__(self, nom, niveau, attaque=40, defense=15)
