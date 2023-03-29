class Pokemon:
    def __init__(self, nom, PV, niveau, puissance, defense):
        self.__nom = nom
        self.__PV = PV
        self.niveau = niveau
        self.puissance = puissance
        self.defense = defense

    def afficher_informations():
        print("Info-Pokemon:")
        