class Pokemon:
    def __init__(self, nom, niveau, attaque, defense):
        self.__nom = nom
        self.__PV = 100
        self.niveau = niveau
        self.attaque = attaque
        self.defense = defense
        
    def afficher_infos(self):
        print(f'Nom: {self.__nom}\nPoints de vie: {self.__PV}\nAttaque: {self.attaque}\nDéfense: {self.defense}')

    def est_vivant(self):
        return self.__PV > 0

    def enlever_PV(self, degats):
        self.__PV -= degats
        if self.__PV < 0:
            self.__PV = 0

    def get_nom(self):
        return self.__nom
