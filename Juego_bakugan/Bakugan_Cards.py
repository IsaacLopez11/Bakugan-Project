import random


#Crando clase bakugan
class Bakugan:
    def __init__(self, name, force_g, atribute):
        self.name = name
        self.force_g = force_g
        self.atribute = atribute
    
    #Añadir puntos de la carta de poder
    def add_points(self, power_card):
        for atributo, points in power_card.items():
            if atributo == self.atribute:
                self.force_g += points
        return self.force_g
    
    #imprimir el objeto
    def __str__(self):
        return (f"{self.name} tiene {self.force_g} y es atributo {self.atribute}" )

#Creando la clase carta de poder
class Power_card:
    def __init__(self, atributes, points):
        self.atributes = atributes
        self.points = points

    def create_card(self):
        self.final_card = {}

        for atribute in self.atributes:
            self.final_card[atribute] = random.choice(self.points)
        
        #final_card = dict(zip(self.atributes, random.choice( self.points)))
        return self.final_card


class Portal_card:
    def __init__(self, atributes, points):
        self.atributes = atributes
        self.points = points

    def create_portal_card(self):
        self.final_portal_card = {}

        for atribute in self.atributes:
            self.final_portal_card[atribute] = random.choice(self.points)
        
        #final_card = dict(zip(self.atributes, random.choice( self.points)))
        return self.final_portal_card
    


    def get_specifics(self):
        print(f'{self.atributes} \n {self.atributes}'
)


# podría crear un función para distribuir las cartas

atributes = ["Fuego", "Agua", "Tierra", ]
points = [50, 70, 20, 60, 80, 100] 

bakugan1 = Bakugan("Drago", 450, "Fuego")

#card1, card2, card3, card4 = power_card(atributes, points)

cardO = Power_card(atributes, points).create_card()
bakugan1.add_points(cardO)
print(bakugan1)



#juego.start_game()

"""
nombres_bakugan = [
    "Drago",
    "Tigrerra",
    "Preyas",
    "Skyress",
    "Gorem",
    "Hydranoid",
    "Wavern",
    "Siege",
    "Cycloid",
    "Robotallion",
    "Fear Ripper",
    "Serpenoid",
    "Reaper",
    "Thunder Wilda",
    "Lars Lion",
    "Wormquake",
    "Serpentoid",
    "Stinglash",
    "Mantris",
    "Juggernoid",
    "Centipoid",
    "Laserman",
    "Sirenoid",
    "Ravenoid",
    "Gargonoid",
    "Foxbat",
    "Tentaclear",
    "Siege",
    "Centorrior",
    "Dual Hydranoid",
    "Blade Tigrerra",
    "El Condor",
    "Harpus",
    "Robotallion",
    "Bee Striker",
    "Oberus",
    "Monarus",
    "Griffon",
    "Hynoid",
    "Dual Dragonoid",
    "Griffon",
    "Storm Skyress",
    "Lars Lion",
    "Serpenoid",
    "Siege",
    "Stinglash",
    "Centorrior",
    "Sirenoid",
    "Reaper",
    "El Condor",
    "Robotallion",
    "Warius",
    "Wormquake",
    "Jelldon",
    "Manion",
    "Centipoid",
    "Fortress",
    "Fencer",
    "Leefram",
    "Thunder Wilda"
]


nuevaLista = list(set(nombres_bakugan))

print(nuevaLista)
"""