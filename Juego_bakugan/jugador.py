import random 
import Campo

#Crear clase Jugador
class Player:
    def __init__(self, name, portal_cards, power_cards, bakugans):
        self.name = name
        self.power_cards = power_cards
        self.portal_cards = portal_cards
        self.bakugans = bakugans
#elegir carta portal
    def choice_portal_card(self, opc):
        self.opc = opc

        if self.opc == 1:
            return self.portal_cards[0]
        elif self.opc == 2:
            return self.portal_cards[1]
        elif self.opc == 3:
            return self.portal_cards[2]
  #Elegir carta de poder      
    def choice_power_card(self, opc):
        self.opc = opc

        if self.opc == 1:
            return self.power_cards[0]
        elif self.opc == 2:
            return self.power_cards[1]
        elif self.opc == 3:
            return self.power_cards[2]
        
#Elegir Bakugan
    def choice_bakugan(self):
        if self.opc == 1:
            return self.bakugans[0]
        elif self.opc == 2:
            return self.bakugans[1]
        elif self.opc == 3:
            return self.bakugans[2]

        #Crear cpu player
class CPU_Player:
    def __init__(self, name, portal_cards, power_cards, bakugans):
        self.name = name
        self.power_cards = power_cards
        self.portal_cards = portal_cards
        self.bakugans = bakugans
#elegir carta portal
    def choice_portal_card(self):
        self.selection = random.choice(self.portal_cards)

        return self.selection
       #Elegir carta de poder    
    def choice_power_card(self):
        return random.choice(self.power_cards)
    #Elegir Bakugan
    def choice_bakugan(self):
        return random.choice(self.bakugans)
    
    def choice_position_in_camp(self):
        return random.choice([0,1,2,3])
    
    def __str__(self):
        return f""
