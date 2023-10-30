import Bakugan_Cards 
#definir la clase battle
class Battle:
    def __init__(self, bakugan1, bakugan2):
        self.bakugan1 = bakugan1
        self.bakugan2 = bakugan2
    
    #Decidir el ganador
    def decide_winner(self):
        if self.bakugan1.force_g > self.bakugan2.force_g:
            print(get_winner(self.bakugan1))
            return (self.bakugan1, 1)
        
        elif self.bakugan1.force_g < self.bakugan2.force_g:
            print(get_winner(self.bakugan2))
            return (self.bakugan2, 2)
        elif self.bakugan1.force_g == self.bakugan2.force_g:
             return (0, 3)
        else:
            return False
    def _str_(self):
        return self.bakugan.name, self.bakugan.force_g

    

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
    def __init__(self, player1, cpu):
        self.player1 = player1
        self.player1_status_winner = False
        self.cpu = cpu
        self.cpu_status_winner = False
        self.cont_player1 = 0
        self.cont_player2 = 0
    
    def start_party(self):
        
        while self.player1_status_winner == False and self.cpu_status_winner == False:
            if self.cont_player1 == 3:
                self.player1_status_winner = True
                break

            elif self.cont_player2 ==  3:
                self.cpu_status_winner = True
                break
            
            for i in self.player1.bakugans:
                print(i)

            bakugan_choiced_player = self.player1.choice_bakugan(int(input("Elige un bakugan")))
            bakugan_choiced_cpu = self.cpu.choice_bakugan()
            
            print(self.player1.power_cards)
            power_card = self.player1.choice_power_card(int(input("elige una carta")))
            power_card_cpu = self.cpu.choice_power_card()


            bakugan_choiced_player.add_points(power_card)
            bakugan_choiced_cpu.add_points(power_card_cpu)

            print(bakugan_choiced_player, bakugan_choiced_cpu)


            battle = Battle(bakugan_choiced_player, bakugan_choiced_cpu)
            winner = battle.decide_winner()
            print(winner)
           

           

            if winner [1] == 3:
                print("empate")
            elif winner[1] == 1:
                self.cont_player1 += 1
                print(f"El contador de player1 va por {self.cont_player1}")

            elif winner[1] == 2:
                self.cont_player2 += 1
                print(f"El contador de cpu va por {self.cont_player2}")

    def __str__(self):
        return "Algo se ha iniciado"



