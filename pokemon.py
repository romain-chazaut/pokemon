class Pokemon:
    def __init__(self, nom, niveau, attaque_base, defense_base):
        self.__nom = nom
        self.__PV = 100 
        self.niveau = niveau
        self.attaque_base = attaque_base
        self.defense_base = defense_base

        self.attaque = attaque_base
        self.defense = defense_base

        self.attaque = self.calculer_attaque()    #Calculer l'attaque et la défnese en fonction du niveau
        self.defense = self.calculer_defense()

        
    def afficher_infos(self):           #Méthode pour afficher les informations du Pokemon
        print(f'Nom: {self.__nom}\nPoints de vie: {self.__PV}\nAttaque: {self.attaque}\nDéfense: {self.defense}')

    def est_vivant(self):           #Méthode pour vérifier si le Pokemon est toujours vivant
        return self.__PV > 0

    def enlever_PV(self, degats):   #Méthode pour enlever des points de vie
        self.__PV -= degats
        if self.__PV < 0:
            self.__PV = 0

    def get_nom(self):              #Méthode pour obtenir le nom du Pokemon
        return self.__nom
    
    def calculer_attaque(self):     #Méthode pour calculer l'attaque du Pokemon en fonction du niveau
        return self.attaque + self.niveau
    
    def calculer_defense(self):     #Méthode pour calculer la défense du pokemon en fonction du niveau.
        return self.defense + self.niveau
    
    
    
