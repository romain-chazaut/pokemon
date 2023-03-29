import normal
import feu
import eau
import terre
import combat




class Pokemon:
    def __init__(self, nom, type, niveau, puissance, defense, PV=100):
        self.__nom = nom
        self.type = type
        self.niveau = niveau
        self.puissance = puissance
        self.defense = defense
        self.__PV = PV

    def afficher_informations():
        print("Info-Pokemon:")

    def set_puissance(self, puissance):
        self.puissance = puissance

    def set_defense(self, defense):
        self.defense = defense
        

