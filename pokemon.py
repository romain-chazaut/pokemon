class Pokemon:
    def __init__(self, nom, niveau, puissance, defense, PV=100):
        self.__nom = nom
        self.niveau = niveau
        self.puissance = puissance
        self.defense = defense
        self.__PV = PV

    def afficher_informations():
        print("Info-Pokemon:")
        