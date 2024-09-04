import random
import weakref
import pygame
import sys
from player_classes import Player, Mage
from utilities import load_images, display_text, Buttons

mage_1 = Mage("Magna", 34, "New Vegas", "Neutral Evil", "Crazy",
              "slave", "alchemist", 100, 100, 8,
              5, 7, 6,5,8,4,6,10,10,10)

# Initialize Pygame
pygame.init()


class StartScreen:
    def __init__(self, main_controller):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, 32)
        self.info = pygame.display.Info()
        self.screen_width = self.info.current_w
        self.screen_height = self.info.current_h


        self.main_game = True
        self.character_select = False
        self.main_controller = weakref.ref(main_controller)


        self.main_timer = 0
        self.start_screen_collide = False
        self.options_menu = False
        self.close_options_menu = False
        self.mouse_pos = pygame.mouse.get_pos()
        self.open_and_close = 0

        self.start_text_y = 80
        self.start_text_x = 200
        self.start_text_active = True

        # ani counters
        self.BG_counter = 0
        self.BG_counter_counter = 0
        self.options_counter = 0
        self.options_counter_counter = 0

        self.start_screen = []
        load_images('assets/images/start_bg/', '.jpeg', self.start_screen)
        self.start_screen = [pygame.transform.scale(x, (self.screen_width, self.screen_height)) for x in
                             self.start_screen]

        self.options_scroll = []
        load_images('assets/images/options_scroll/', '.png', self.options_scroll)
        self.options_scroll = [pygame.transform.scale(x, (self.screen_width * 0.6, self.screen_height * 0.5)) for x in
                               self.options_scroll]

        self.gauntlet_cursor = pygame.image.load('assets/images/guantlet_cursor.png').convert_alpha()
        self.gauntlet_cursor = pygame.transform.scale(self.gauntlet_cursor, (80, 50))

        self.create_new_character_button = pygame.image.load(
            'assets/images/Create_new_character_button.png').convert_alpha()
        self.create_new_character_button = pygame.transform.scale(self.create_new_character_button, (300, 85))

        self.load_game_button = pygame.image.load('assets/images/load_game_button.png').convert_alpha()
        self.load_game_button = pygame.transform.scale(self.load_game_button, (300, 85))

        self.exit_button = pygame.image.load('assets/images/exit_menu_button.png').convert_alpha()
        self.exit_button = pygame.transform.scale(self.exit_button, (300, 85))

        self.create_new = Buttons(self, 660, 350, self.create_new_character_button, 1000, False)
        self.load_button = Buttons(self, 660, 450, self.load_game_button, 1000, False)
        self.exit_menu = Buttons(self, 660, 550, self.exit_button, 1000, False)

        self.button_group = pygame.sprite.Group()
        self.button_group.add(self.create_new)
        self.button_group.add(self.load_button)
        self.button_group.add(self.exit_menu)

        #start screen music
        pygame.mixer.init()
        pygame.mixer.music.load("assets/audio/Vopna.mp3")
        pygame.mixer.music.play(-1, 0.0)

        self.bg = self.start_screen[0]

    def run(self):
        start_screen_animations = False
        if self.start_text_active:
            self.start_text_x = 300
            font_size = 65
            text_color = (255, 155, 15)
        else:
            self.start_text_x = 10
            font_size = 32
            text_color = (255, 0, 55)

        narrative_text = "Welcome to The Abyssal Kingdoms traveler............prepare yourself."

        font = pygame.font.Font("assets/fonts/bloodcrow.ttf", font_size)
        text_lines = narrative_text.split(' ')
        line = ""
        text_to_display = []
        for word in text_lines:
            if font.size(line + word)[0] >= self.screen_width - 100:
                text_to_display.append(line)
                line = word + " "
            else:
                line += word + " "
        if line:
            text_to_display.append(line)

        current_line = 0
        char_index = 0

        while self.main_game:
            self.main_timer += 0.25
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.main_game = False
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    #print(
                        #f"Mouse Button Up: options_menu={self.options_menu}, close_options_menu={self.close_options_menu}")
                    if self.start_sign_collide and not self.options_menu and not self.close_options_menu:
                        self.options_menu = True
                        self.options_counter = 0
                        self.options_counter_counter = 0
                        #print("Opening options menu")
                    elif self.exit_menu.hover and self.options_menu:
                        self.close_options_menu = True
                        self.options_menu = False
                        #print("Closing options menu")
                    elif self.create_new.hover:
                        self.main_game=False
                        self.main_controller().switch_to_character_select()


            mouse_pos = pygame.mouse.get_pos()
            self.mouse_pos = mouse_pos
            if start_screen_animations:
                self.BG_counter_counter += 1
                if self.BG_counter_counter % 2 == 0:
                    self.BG_counter += 1
                if self.BG_counter > 25:
                    self.BG_counter = 0
            start_screen_animation_switch = random.randint(0, 1000)
            if start_screen_animation_switch > 950 and self.BG_counter == 0:
                start_screen_animations = True
            elif start_screen_animation_switch <= 950 and self.BG_counter == 0:
                start_screen_animations = False
            self.bg = self.start_screen[self.BG_counter]
            self.screen.blit(self.bg, (0, 0))  # Draw the scaled background image

            if self.options_menu:
                self.options_counter_counter += 1
                if self.options_counter_counter % 1 == 0:
                    self.options_counter += 1
                if self.options_counter > 6:
                    self.options_counter = 6

                self.options = self.options_scroll[self.options_counter]

                self.screen.blit(self.options, (320, 275))
                if self.options_counter == 6:
                    self.button_group.update()
                    self.button_group.draw(self.screen)
                if self.options_counter == 5:
                    self.open_and_close += 1

            elif not self.options_menu and self.close_options_menu and self.options_counter >= 0:
                self.options_counter_counter += 1
                if self.options_counter_counter % 1 == 0:
                    self.options_counter -= 1
                if self.options_counter <= 0:
                    self.options_counter = 0
                    self.close_options_menu = False
                    #print("Options menu closed fully")

                self.options = self.options_scroll[self.options_counter]
                self.screen.blit(self.options, (320, 275))

                # Reset hover state when closing options menu
                self.create_new.hover = False
                self.load_button.hover = False
                self.exit_menu.hover = False

            y = self.start_text_y  # Initialize y position for text

            cursor_area = pygame.Rect(135, 630, 210, 112)  # Example area: (x, y, width, height)

            # Change cursor based on position
            if cursor_area.collidepoint(mouse_pos) or (self.options_menu and (self.create_new.hover or self.load_button.hover or self.exit_menu.hover)):
                pygame.mouse.set_visible(False)  # Hide the system cursor
                self.screen.blit(self.gauntlet_cursor, mouse_pos)
                self.start_sign_collide = True
            else:
                pygame.mouse.set_visible(True)
                self.start_sign_collide = False

            for i in range(current_line):
                display_text(self.screen, text_to_display[i], (self.start_text_x, y), font, text_color,
                             self.screen_width)
                y += font.get_linesize()  # Increment y position by line height

            if current_line < len(text_to_display):
                line = text_to_display[current_line]
                display_text(self.screen, line[:char_index], (self.start_text_x, y), font, text_color,
                             self.screen_width)
                char_index += 1
                if char_index > len(line):
                    char_index = 0
                    current_line += 1
                    y += font.get_linesize()  # Increment y position for the next line

            pygame.display.flip()
            pygame.time.delay(50)



    # Create game instance and run it
#startscreen = StartScreen()
#startscreen.run()
