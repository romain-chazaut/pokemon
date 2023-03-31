from pokemon import Pokemon


class Terre(Pokemon):
    def __init__(self, nom, niveau):
        Pokemon.__init__(self, nom, niveau, attaque_base = 15, defense_base = 15)
