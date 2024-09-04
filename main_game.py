from start_screen import StartScreen
from character_select import CharacterSelect





class MainContoller:
    def __init__(self):
        self.start_screen = StartScreen(self)
        self.character_select = CharacterSelect(self)
        self.current_screen = self.start_screen

    def switch_to_character_select(self):
        self.current_screen.main_game = False
        self.character_select.main_game = True
        self.current_screen = self.character_select

    def switch_to_start_screen(self):
        self.current_screen.main_game = False
        self.start_screen.main_game = True
        self.current_screen = self.start_screen

    def run(self):
        while True:
            self.current_screen.run()

    #def run(self):

        #while True:
            #Condition that activates the character select screen
            #if start_screen.main_game == False and start_screen.character_select == True:
                #self.character_select.main_game = True
                #self.character_select.start_screen = False


            #Condition that activates the start screen
            #if start_screen.main_game == True and start_screen.character_select == False:
               # self.character_select.main_game = False
                #self.character_select.start_screen = True

            #Activation of character select screen
            #if self.character_select.main_game == True and self.character_select.start_screen == False:
             #   self.character_select.run()

            #Activation of start screen
           # if self.character_select.main_game == False and self.character_select.start_screen == True:
                #self.start_screen.run()

           # if self.character_select.back_to_startscreen == True:
              #  self.character_select.main_game = False
              #  self.start_screen.main_game = True

main_controller = MainContoller()
main_controller.run()

