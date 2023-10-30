import Bakugan_Cards 

#definir la clase battle
class Battle:
    def _init_(self, bakugan1, bakugan2):
        self.bakugan1 = bakugan1
        self.bakugan2 = bakugan2
    
    #Decidir el ganador
    def decide_winner(self):
        if self.bakugan1.force_g > self.bakugan2.force_g:
            print(get_winner(self.bakugan1))
            return self.bakugan1
        
        elif self.bakugan1.force_g < self.bakugan2.force_g:
            print(get_winner(self.bakugan2))
            return self.bakugan2
        else:
            return False
    # def _str_(self):
    #     return f"{self.bakugan.name} con {self.bakugan.force_g}"

    

#obtener el ganador para mostrar en pantalla    
def get_winner(bakugan):
    #self.bakugan = bakugan
    return (f"el ganador es: {bakugan.name} con {bakugan.force_g}",bakugan)


bakugan1 = Bakugan_Cards.Bakugan("Drago", 40, "Fuego")
bakugan2 = Bakugan_Cards.Bakugan("Angel", 450, "Fuego")


# battle = Battle(bakugan1, bakugan2)

# winner = battle.decide_winner()
# get_winner(winner[0])


class Party:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.cont_player1 = 0
        self.cont_player2 = 0
    
    def start_party(self):
        while self.player1.status_winner == False & self.player1.status_winner == False:
            battle = Battle(bakugan1, bakugan2)
            winner = battle.decide_winner()
            get_winner(winner[1])

            if self.cont_player1 > 2:
                self.player1.status_winner == True

            elif self.cont_player2> 2:
                self.player1.status_winner == True

            elif winner.property == self.player1.name:
                self.cont_player1 += 1
            else:
                self.cont_player2 += 1



