import battle
import Bakugan_Cards as b
import jugador as ply
import Campo as camp

class Interface_game:
    def __init__(self, init):
        self.init = init

    def principal_menu(self):
        print("Bienvenido al juego de Bakugan\n")
        print("Elige una de las opciones\n")
        
        opcion = input("1.Jugar\n2.salir\n")

        if opcion == "1":
            print("Perfecto!! Juguemos!!")

        #1 crear cartas
            #Creo Cartas

            #Cartas de poder
            atributes = ["Fuego", "Agua", "Tierra", ]
            points = [50, 70, 20, 60, 80, 100] 
            power_card = b.Power_card(atributes, points)
        
        #2 Crear Bakugans
            #crear bakugans
            bakugan1 = b.Bakugan("Drago", 450, "Fuego")
            bakugan2 = b.Bakugan("Terrolclow", 250, "Fuego")
            bakugan3 = b.Bakugan("Robotalion", 300, "Fuego")
            mazo_bakugans =[bakugan1, bakugan2, bakugan3]
            
        #3 Crear player y pasarle el mazo y los bakugans
            power_card1 = power_card.create_card(),
            power_card2 = power_card.create_card(),
            power_card3 = power_card.create_card()
            mazo_power_card = [power_card1,power_card2,power_card3 ]

            #cartas portal
            portal_card = b.Portal_card(atributes, points)
            
            #mazo cartas portal
            portal_card1 = portal_card.create_portal_card(),
            portal_card2 = portal_card.create_portal_card(),
            portal_card3 = portal_card.create_portal_card()
            mazo_portal_card = [portal_card1, portal_card2, portal_card3]


            player1 = ply.Player("Isaac",mazo_portal_card, mazo_power_card, mazo_bakugans )
            cpu = ply.CPU_Player("Mascarade",mazo_portal_card, mazo_power_card, mazo_bakugans)
            

            #imprimir carta portal del jugador
            print(player1.portal_cards)

            #Elgir carta portal
            portal_card_choiced_player = player1.choice_portal_card(int(input("Escoge una carta portal: ")))
            portal_card_choiced_CPU = cpu.choice_portal_card()

            #crear campo

            campo = camp.Campo()

            #Elegir posicion
            campo.verify_position(portal_card_choiced_player, int(input("Escoge una posicion enel campo: ")) )
            cpu_position_choiced = cpu.choice_position_in_camp()
            #hay un bug por parte de la verificacion del campo al momento de que la cpu elija, porque el player elige pero si la cpu elige igual que el player se setea el 1 normal
            
            campo.verify_position(portal_card_choiced_CPU, cpu_position_choiced )
            
            
            # print(portal_card_choiced_CPU)
            




            print(campo)
        #iniciar partida
        #batallar
start = Interface_game
start.principal_menu(True)
        
        