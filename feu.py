import pokemon

class Feu(pokemon):
    def __init__(self, puissance, defense, PV=100):
        self.puissance = puissance
        self.defense = defense
        self.__PV = PV