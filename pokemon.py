class Pokemon:
    def __init__(self, nom, niveau, attaque_base, defense_base):
        self.__nom = nom
        self.__PV = 100 
        self.niveau = niveau
        self.attaque_base = attaque_base
        self.defense_base = defense_base

        self.attaque = attaque_base
        self.defense = defense_base

        self.attaque = self.calculer_attaque()
        self.defense = self.calculer_defense()

        
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
    
    def calculer_attaque(self):
        return self.attaque + self.niveau
    
    def calculer_defense(self):
        return self.defense + self.niveau
    
    
    
