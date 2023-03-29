import pokemon
import normal
import feu
import eau
import terre

class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def verif(self, pokemon1, pokemon2):
        return pokemon1.__PV > 0 and pokemon2.__PV > 0
    
combat = Combat(pokemon1=0, pokemon2=0)
print("Les deux pokemon sont en vie :", combat.verif())


    

        
