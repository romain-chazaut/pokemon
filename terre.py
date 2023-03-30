from pokemon import Pokemon

class Terre(Pokemon):
    def __init__(self, nom, niveau):
        Pokemon.__init__(self, nom, niveau, attaque=15, defense=15)
