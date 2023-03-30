from pokemon import Pokemon

class Normal(Pokemon):
    def __init__(self, nom, niveau):
        Pokemon.__init__(self, nom, niveau, attaque=50, defense=10)
