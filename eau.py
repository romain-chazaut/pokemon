from pokemon import Pokemon

class Eau(Pokemon):
    def __init__(self, nom, niveau):
        Pokemon.__init__(self, nom, niveau, attaque_base = 10, defense_base = 15)
