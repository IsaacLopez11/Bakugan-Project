from Bakugan_Cards import *



class Campo:
    def __init__(self):
        self.campo = [[0,0],[0,0]]
    

    def verify_position(self,portal_card, position):
        self.portal_card = portal_card
        self.position= position

        if self.position == 1:
            if self.campo[0][0] == 0:
                self.campo[0][0] = 1 #{"ocuped": 1 ,"card":self.portal_card }
        elif self.position == 2:
            if self.campo[0][1] == 0:
                self.campo[0][1] = 1 #{"ocuped": 1 ,"card":self.portal_card }
        elif self.position == 3:
            if self.campo[1][0] == 0:
                self.campo[1][0] = 1 #{"ocuped": 1 ,"card":self.portal_card }
        elif self.position == 4:
            if self.campo[1][1] == 0:
                self.campo[1][1] = 1 #{"ocuped": 1 ,"card":self.portal_card }
        else: 
            self.verify_position()
        #podía intentar hacer varias sentencias if para probar
       

        # for row in self.campo:
        #     for column in row:
        #         if column == 0:
        #             return self.set_portal_card()
        #         elif column == 1:
        #             print(f"Intentalo de nuevo")
        #             return f"Intentalo de nuevo"

    def set_portal_card(self):
        

        if self.position == 1:
            self.campo[0][0] = 1 #{"ocuped": 1 ,"card":self.portal_card }
        elif self.position == 2:
            self.campo[0][1] = 1 #{"ocuped": 1 ,"card":self.portal_card }
        elif self.position == 3:
            self.campo[1][0] =1 #{"ocuped": 1 ,"card":self.portal_card }
        elif self.position == 4:
            self.campo[1][1] = 1 #{"ocuped": 1 ,"card":self.portal_card }

    def __str__(self):
        for fila in self.campo:
            print(fila)
        return f""
    """def __str__(self) :
        
        for casilla in self.campo:
            for elemento in casilla:
                print(elemento["ocuped"])
        return f"""""

atributes = ["Fuego", "Agua", "Tierra", ]
points = [50, 70, 20, 60, 80, 100] 

portal_card = Portal_card(atributes, points)

camp = Campo()
camp.verify_position(portal_card, 1)