import pokemon

class Normal(pokemon):
    def __init__(self, PV, puissance, defense):
        self.__PV = PV
        self.puissance = puissance
        self.defense = defense

        