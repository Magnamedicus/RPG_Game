import random
import weakref
import pygame
import sys
import time

from player_classes import Player, Mage, Knight, Rogue, Brute,Hospitaller,Executioner,Bulwark,Champion,BloodMage,ShadowMage, LifeSpring,ElementalMage
from utilities import load_images, display_text, update_csv, Buttons,change_opacity,draw_text_one_letter_at_a_time


pygame.init()

class CharacterSelect:
    def __init__(self, main_controller):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, 32)
        self.info = pygame.display.Info()
        self.screen_width = self.info.current_w
        self.screen_height = self.info.current_h
        self.start_text_y = 100
        self.start_text_x = 700
        self.class_declaration = ''
        self.text_surface = ''
        self.text_displayed = False

        self.main_game = False
        #self.start_screen = False
        self.screen_rect = pygame.Surface((1600,900))


        self.main_controller = weakref.ref(main_controller)

        self.character_profile = {'class':None, 'alignment':None, 'subclass':None}
        self.character_profile_lst = []

        self.main_timer = 0

        self.class_select = True

        self.class_button_down = False
        self.class_button_up = True

        self.align_button_down = False
        self.align_button_up = True

        self.subclass_button_down = False
        self.subclass_button_up = True

        self.back_button_down = False
        self.back_button_up = True

        self.feed_forward_down = False
        self.feed_forward_up = True

        self.see_details_down = False
        self.see_details_up = True

        self.details_dismiss_down = False
        self.details_dismiss_up = True

        self.details_selected = False




        self.back_to_startscreen = False

            #screen states
        self.class_selection_state = True
        self.allignment_selection_state = False
        self.subclass_selection_state = False

        #fonts
        self.primitive_font = pygame.font.Font("assets/fonts/Primitive.ttf",32)

        # class ani switches
        self.mage_chosen = False
        self.knight_chosen = False
        self.rogue_chosen = False
        self.brute_chosen = False

        self.mage_counter = 0
        self.mage_counter_counter = 0

        self.knight_counter = 0
        self.knight_counter_counter = 0
        self.knight_cycles = 0

        self.optionsPanel_counter = 0
        self.optionsPanel_counter_counter = 0

        #subclass booleans
            #knight
        self.hospitaller_chosen = False
        self.executioner_chosen = False
        self.bulwark_chosen = False
        self.champion_chosen = False

            #mage
        self.bloodmage_chosen = False
        self.shadowmage_chosen = False
        self.lifespring_chosen = False
        self.elemental_chosen = False

        #subclass declarations
        self.knight_subclass_declaration = ''

        #subclass portraits

        self.champion_portrait = pygame.image.load('assets/images/subclass_buttons/knight/champion_portrait/champion_knight.png')
        self.champion_portrait = pygame.transform.scale(self.champion_portrait, (505, 550))
        self.champion_banner = pygame.image.load('assets/images/subclass_buttons/knight/champion_portrait/champion_banner.png')
        self.champion_banner = pygame.transform.scale(self.champion_banner, (650, 220))

        self.bulwark_portrait = pygame.image.load('assets/images/subclass_buttons/knight/bulwark_portrait/bulwark_knight.png')
        self.bulwark_portrait = pygame.transform.scale(self.bulwark_portrait, (1205, 820))
        self.bulwark_banner = pygame.image.load('assets/images/subclass_buttons/knight/bulwark_portrait/bulwark_banner.png')
        self.bulwark_banner = pygame.transform.scale(self.bulwark_banner, (650, 220))

        self.hospitaller_portrait = pygame.image.load('assets/images/subclass_buttons/knight/hospitaller_portrait/hospitaler_knight.png')
        self.hospitaller_banner = pygame.image.load('assets/images/subclass_buttons/knight/hospitaller_portrait/hospitaller_banner.png')
        self.hospitaller_banner = pygame.transform.scale(self.hospitaller_banner, (650, 220))

        self.executioner_portrait = pygame.image.load('assets/images/subclass_buttons/knight/executioner_portrait/executioner_knight.png')
        self.executioner_banner = pygame.image.load('assets/images/subclass_buttons/knight/executioner_portrait/executioner_banner.png')
        self.executioner_banner = pygame.transform.scale(self.executioner_banner, (650, 220))
        self.executioner_portrait = pygame.transform.scale(self.executioner_portrait, (1205, 820))

        self.bloodmage_portrait = pygame.image.load('assets/images/subclass_buttons/mage/bloodmage_portrait/blood_mage.png')
        self.bloodmage_portrait = pygame.transform.scale(self.bloodmage_portrait, (480, 720))
        self.bloodmage_banner = pygame.image.load('assets/images/subclass_buttons/mage/bloodmage_portrait/bloodmage_banner.png')
        self.bloodmage_banner = pygame.transform.scale(self.bloodmage_banner, (650, 220))

        self.shadowmage_portrait = pygame.image.load('assets/images/subclass_buttons/mage/shadowmage_portrait/shadow_mage.png')
        self.shadowmage_portrait = pygame.transform.scale(self.shadowmage_portrait, (480, 720))
        self.shadowmage_banner = pygame.image.load('assets/images/subclass_buttons/mage/shadowmage_portrait/shadowmage_banner.png')
        self.shadowmage_banner = pygame.transform.scale(self.shadowmage_banner, (650, 220))

        self.lifespringmage_portrait = pygame.image.load('assets/images/subclass_buttons/mage/lifespringmage_portrait/lifespring_mage.png')
        self.lifespringmage_portrait = pygame.transform.scale(self.lifespringmage_portrait, (480, 720))
        self.lifespringmage_banner = pygame.image.load('assets/images/subclass_buttons/mage/lifespringmage_portrait/lifespringmage_banner.png')
        self.lifespringmage_banner = pygame.transform.scale(self.lifespringmage_banner, (650, 220))

        self.elementalmage_portrait = pygame.image.load('assets/images/subclass_buttons/mage/elementalmage_portrait/elemental_mage.png')
        self.elementalmage_portrait = pygame.transform.scale(self.elementalmage_portrait, (580, 820))
        self.elementalmage_banner = pygame.image.load('assets/images/subclass_buttons/mage/elementalmage_portrait/elementalmage_banner.png')
        self.elementalmage_banner = pygame.transform.scale(self.elementalmage_banner, (650, 220))

        self.executioner_border = pygame.image.load('assets/images/executioner_border.png')
        self.executioner_border = pygame.transform.scale(self.executioner_border, (self.screen_width, self.screen_height))

        self.hospitaller_border = pygame.image.load('assets/images/hospitaller_border.png')
        self.hospitaller_border = pygame.transform.scale(self.hospitaller_border,(self.screen_width, self.screen_height))

        self.bulwark_border = pygame.image.load('assets/images/bulwark_border.png')
        self.bulwark_border = pygame.transform.scale(self.bulwark_border,(self.screen_width, self.screen_height))

        self.champion_border = pygame.image.load('assets/images/champion_border.png')
        self.champion_border = pygame.transform.scale(self.champion_border, (self.screen_width, self.screen_height))

        self.bloodmage_border = pygame.image.load('assets/images/bloodmage_border.png')
        self.bloodmage_border = pygame.transform.scale(self.bloodmage_border, (self.screen_width, self.screen_height))

        self.shadowmage_border = pygame.image.load('assets/images/shadowmage_border.png')
        self.shadowmage_border = pygame.transform.scale(self.shadowmage_border, (self.screen_width, self.screen_height))

        self.lifespringmage_border = pygame.image.load('assets/images/lifespring_border.png')
        self.lifespringmage_border = pygame.transform.scale(self.lifespringmage_border, (self.screen_width, self.screen_height))

        self.elementalmage_border = pygame.image.load('assets/images/elementalmage_border.png')
        self.elementalmage_border = pygame.transform.scale(self.elementalmage_border,(self.screen_width, self.screen_height))

        #banner booleans
        self.LG_banner = False
        self.NG_banner = False
        self.CG_banner = False
        self.LN_banner = False
        self.TN_banner = False
        self.CN_banner = False
        self.LE_banner = False
        self.NE_banner = False
        self.CE_banner = False


        #headings
        self.class_heading = pygame.image.load('assets/images/character_select_headings/class_select_heading.png').convert_alpha()
        self.class_heading = pygame.transform.scale(self.class_heading,(400,120))

        self.align_heading = pygame.image.load('assets/images/character_select_headings/alignment_select_heading.png').convert_alpha()
        self.align_heading = pygame.transform.scale(self.align_heading, (400, 120))

        self.subclass_heading = pygame.image.load('assets/images/character_select_headings/subclass_select_heading.png').convert_alpha()
        self.subclass_heading = pygame.transform.scale(self.subclass_heading, (400, 120))

        #allignment banners
        self.lawfulGood_banner = pygame.image.load('assets/images/alignment_banners/lawful_good_banner.png').convert_alpha()
        self.lawfulGood_banner = pygame.transform.scale(self.lawfulGood_banner,(600,240))

        self.neutralGood_banner = pygame.image.load('assets/images/alignment_banners/neutral_good_banner.png').convert_alpha()
        self.neutralGood_banner = pygame.transform.scale(self.neutralGood_banner, (600, 240))

        self.chaoticGood_banner = pygame.image.load('assets/images/alignment_banners/chaotic_good_banner.png').convert_alpha()
        self.chaoticGood_banner = pygame.transform.scale(self.chaoticGood_banner, (600, 240))

        self.lawfulNeutral_banner = pygame.image.load('assets/images/alignment_banners/lawful_neutral_banner.png').convert_alpha()
        self.lawfulNeutral_banner = pygame.transform.scale(self.lawfulNeutral_banner, (600, 240))

        self.trueNeutral_banner = pygame.image.load('assets/images/alignment_banners/true_neutral_banner.png').convert_alpha()
        self.trueNeutral_banner = pygame.transform.scale(self.trueNeutral_banner, (600, 240))

        self.chaoticNeutral_banner = pygame.image.load('assets/images/alignment_banners/chaotic_neutral_banner.png').convert_alpha()
        self.chaoticNeutral_banner = pygame.transform.scale(self.chaoticNeutral_banner, (600, 240))

        self.lawfulEvil_banner = pygame.image.load('assets/images/alignment_banners/lawful_evil_banner.png').convert_alpha()
        self.lawfulEvil_banner = pygame.transform.scale(self.lawfulEvil_banner, (600, 240))

        self.neutralEvil_banner = pygame.image.load('assets/images/alignment_banners/neutral_evil_banner.png').convert_alpha()
        self.neutralEvil_banner = pygame.transform.scale(self.neutralEvil_banner, (600, 240))

        self.chaoticEvil_banner = pygame.image.load('assets/images/alignment_banners/chaotic_evil_banner.png').convert_alpha()
        self.chaoticEvil_banner = pygame.transform.scale(self.chaoticEvil_banner, (600, 240))





        self.mage_ani = []
        load_images('assets/images/classes/mage_selection/', '.png', self.mage_ani)
        self.mage_ani = [pygame.transform.scale(x, (630, 500)) for x in self.mage_ani]

        self.knight_ani = []
        load_images('assets/images/classes/knight_selection/', '.png', self.knight_ani)
        self.knight_ani = [pygame.transform.scale(x, (550, 420)) for x in self.knight_ani]

        self.option_panel = []
        load_images('assets/images/CS_options_panel/', '.png', self.option_panel)
        self.option_panel = [pygame.transform.scale(x, (500, 700)) for x in self.option_panel]
        for i in self.option_panel:
            i.set_alpha(135)

        self.mage_button = []
        load_images('assets/images/mage_select_buttons/', '.png', self.mage_button)
        self.mage_button = [pygame.transform.scale(x, (225, 65)) for x in self.mage_button]
        for i in self.mage_button:
            i.set_alpha(145)

        self.knight_button = []
        load_images('assets/images/knight_select_buttons/', '.png', self.knight_button)
        self.knight_button = [pygame.transform.scale(x, (225, 85)) for x in self.knight_button]
        for i in self.knight_button:
            i.set_alpha(145)

        self.rogue_button = []
        load_images('assets/images/rogue_select_buttons/', '.png', self.rogue_button)
        self.rogue_button = [pygame.transform.scale(x, (265, 115)) for x in self.rogue_button]
        for i in self.rogue_button:
            i.set_alpha(145)

        self.brute_button = []
        load_images('assets/images/brute_select_buttons/', '.png', self.brute_button)
        self.brute_button = [pygame.transform.scale(x, (255, 105)) for x in self.brute_button]
        for i in self.brute_button:
            i.set_alpha(145)

        self.lawful_good_button = []
        load_images('assets/images/alignment_choices/lawful_good_button/', '.png', self.lawful_good_button)
        self.lawful_good_button = [pygame.transform.scale(x, (175, 120)) for x in self.lawful_good_button]

        self.neutral_good_button = []
        load_images('assets/images/alignment_choices/neutral_good_button/', '.png', self.neutral_good_button)
        self.neutral_good_button = [pygame.transform.scale(x, (175, 115)) for x in self.neutral_good_button]

        self.chaotic_good_button = []
        load_images('assets/images/alignment_choices/chaotic_good_button/', '.png', self.chaotic_good_button)
        self.chaotic_good_button = [pygame.transform.scale(x, (175, 115)) for x in self.chaotic_good_button]

        self.lawful_neutral_button = []
        load_images('assets/images/alignment_choices/lawful_neutral_button/', '.png', self.lawful_neutral_button)
        self.lawful_neutral_button = [pygame.transform.scale(x, (175, 115)) for x in self.lawful_neutral_button]

        self.true_neutral_button = []
        load_images('assets/images/alignment_choices/true_neutral_button/', '.png', self.true_neutral_button)
        self.true_neutral_button = [pygame.transform.scale(x, (175, 115)) for x in self.true_neutral_button]

        self.chaotic_neutral_button = []
        load_images('assets/images/alignment_choices/chaotic_neutral_button/', '.png', self.chaotic_neutral_button)
        self.chaotic_neutral_button = [pygame.transform.scale(x, (175, 115)) for x in self.chaotic_neutral_button]

        self.lawful_evil_button = []
        load_images('assets/images/alignment_choices/lawful_evil_button/', '.png', self.lawful_evil_button)
        self.lawful_evil_button = [pygame.transform.scale(x, (175, 115)) for x in self.lawful_evil_button]

        self.neutral_evil_button = []
        load_images('assets/images/alignment_choices/neutral_evil_button/', '.png', self.neutral_evil_button)
        self.neutral_evil_button = [pygame.transform.scale(x, (175, 115)) for x in self.neutral_evil_button]

        self.chaotic_evil_button = []
        load_images('assets/images/alignment_choices/chaotic_evil_button/', '.png', self.chaotic_evil_button)
        self.chaotic_evil_button = [pygame.transform.scale(x, (175, 115)) for x in self.chaotic_evil_button]

        #subclass button images
        self.hospitaller_button = []
        load_images('assets/images/subclass_buttons/knight/Hospitaller_buttons/', '.png', self.hospitaller_button)
        self.hospitaller_button = [pygame.transform.scale(x, (225, 165)) for x in self.hospitaller_button]

        self.executioner_button = []
        load_images('assets/images/subclass_buttons/knight/executioner_buttons/', '.png', self.executioner_button)
        self.executioner_button = [pygame.transform.scale(x, (225, 165)) for x in self.executioner_button]

        self.bulwark_button = []
        load_images('assets/images/subclass_buttons/knight/bulwark_buttons/', '.png', self.bulwark_button)
        self.bulwark_button = [pygame.transform.scale(x, (265, 195)) for x in self.bulwark_button]

        self.champion_button = []
        load_images('assets/images/subclass_buttons/knight/champion_buttons/', '.png', self.champion_button)
        self.champion_button = [pygame.transform.scale(x, (285, 215)) for x in self.champion_button]

        self.bloodmage_button = []
        load_images('assets/images/subclass_buttons/mage/bloodmage_buttons/', '.png', self.bloodmage_button)
        self.bloodmage_button = [pygame.transform.scale(x, (245, 155)) for x in self.bloodmage_button]

        self.shadowmage_button = []
        load_images('assets/images/subclass_buttons/mage/shadowmage_buttons/', '.png', self.shadowmage_button)
        self.shadowmage_button = [pygame.transform.scale(x, (245, 155)) for x in self.shadowmage_button]

        self.lifespringmage_button = []
        load_images('assets/images/subclass_buttons/mage/lifespringmage_buttons/', '.png', self.lifespringmage_button)
        self.lifespringmage_button = [pygame.transform.scale(x, (245, 155)) for x in self.lifespringmage_button]

        self.elementalmage_button = []
        load_images('assets/images/subclass_buttons/mage/elementalmage_buttons/', '.png', self.elementalmage_button)
        self.elementalmage_button = [pygame.transform.scale(x, (245, 155)) for x in self.elementalmage_button]

        self.back_button = []
        load_images('assets/images/back_button/', '.png', self.back_button)
        self.back_button = [pygame.transform.scale(x, (200, 85)) for x in self.back_button]

        self.details_button = []
        load_images('assets/images/details_button/', '.png', self.details_button)
        self.details_button = [pygame.transform.scale(x, (200, 85)) for x in self.details_button]

        self.details_dismiss_button = []
        load_images('assets/images/details_dismiss_button/', '.png', self.details_dismiss_button)
        self.details_dismiss_button = [pygame.transform.scale(x, (200, 85)) for x in self.details_dismiss_button]

        self.choose_alignment_button = []
        load_images('assets/images/choose_alignment_button/', '.png', self.choose_alignment_button)
        self.choose_alignment_button = [pygame.transform.scale(x, (200, 85)) for x in self.choose_alignment_button]

        self.choose_subclass_button = []
        load_images('assets/images/choose_subclass_button/', '.png', self.choose_subclass_button)
        self.choose_subclass_button = [pygame.transform.scale(x, (200, 85)) for x in self.choose_subclass_button]







        self.gauntlet_cursor = pygame.image.load('assets/images/guantlet_cursor.png').convert_alpha()
        self.gauntlet_cursor = pygame.transform.scale(self.gauntlet_cursor, (80, 50))

        self.choose_mage_button = Buttons(self, 280, 240, self.mage_button[0], 1000, False)
        self.choose_knight_button = Buttons(self, 280, 350, self.knight_button[0], 1000, False)
        self.choose_rogue_button = Buttons(self, 260, 460, self.rogue_button[0], 1000, False)
        self.choose_brute_button = Buttons(self,255, 600, self.brute_button[0], 1000, False)

        self.lawfulGood_button = Buttons(self,210, 158, self.lawful_good_button[0], 1000, False)
        self.neutralGood_button = Buttons(self, 420, 160, self.neutral_good_button[0], 1000, False)
        self.chaoticGood_button = Buttons(self, 210, 290, self.chaotic_good_button[0], 1000, False)
        self.lawfulNeutral_button = Buttons(self, 420, 290, self.lawful_neutral_button[0], 1000, False)
        self.trueNeutral_button = Buttons(self, 210, 420, self.true_neutral_button[0], 1000, False)
        self.chaoticNeutral_button = Buttons(self, 420, 423, self.chaotic_neutral_button[0], 1000, False)
        self.lawfulEvil_button = Buttons(self, 210, 550, self.lawful_evil_button[0], 1000, False)
        self.neutralEvil_button = Buttons(self, 420, 550, self.neutral_evil_button[0], 1000, False)
        self.chaoticEvil_button = Buttons(self, 310, 665, self.chaotic_evil_button[0], 1000, False)

        #subclass buttons
        self.see_details_button = Buttons(self, 850, 800, self.details_button[0], 1000, False)
        self.dismiss_details_button = Buttons(self, 650, 450, self.details_dismiss_button[0], 50, False)

        #knight buttons
        self.hospitaller_subclass_button = Buttons(self, 295, 145, self.hospitaller_button[0], 1000, False)
        self.executioner_subclass_button = Buttons(self, 275, 610, self.executioner_button[0], 1000, False)
        self.bulwark_subclass_button = Buttons(self, 255, 280, self.bulwark_button[0], 1000, False)
        self.champion_subclass_button = Buttons(self, 245, 425, self.champion_button[0], 1000, False)

        #mage buttons
        self.bloodmage_subclass_button = Buttons(self, 275, 610, self.bloodmage_button[0], 1000, False)
        self.shadowmage_subclass_button = Buttons(self, 275, 460, self.shadowmage_button[0], 1000, False)
        self.lifespringmage_subclass_button = Buttons(self, 275, 150, self.lifespringmage_button[0], 1000, False)
        self.elementalmage_subclass_button = Buttons(self, 275, 300, self.elementalmage_button[0], 1000, False)

        self.go_back_button = Buttons(self, 170, 800, self.back_button[0], 1000, False)
        self.feed_forward_button = Buttons(self, 420, 800, self.choose_alignment_button[0], 1000, False)

        self.class_button_group = pygame.sprite.Group()
        self.class_button_group.add(self.choose_mage_button)
        self.class_button_group.add(self.choose_knight_button)
        self.class_button_group.add(self.choose_rogue_button)
        self.class_button_group.add(self.choose_brute_button)


        self.alignment_button_group = pygame.sprite.Group()
        self.alignment_button_group.add(self.lawfulGood_button)
        self.alignment_button_group.add(self.neutralGood_button)
        self.alignment_button_group.add(self.chaoticGood_button)
        self.alignment_button_group.add(self.lawfulNeutral_button)
        self.alignment_button_group.add(self.trueNeutral_button)
        self.alignment_button_group.add(self.chaoticNeutral_button)
        self.alignment_button_group.add(self.lawfulEvil_button)
        self.alignment_button_group.add(self.neutralEvil_button)
        self.alignment_button_group.add(self.chaoticEvil_button)

        #subclass button groups
        self.subclass_screen_button_group = pygame.sprite.Group()
        self.subclass_screen_button_group.add(self.see_details_button)

        self.dismiss_button_group = pygame.sprite.Group()
        self.dismiss_button_group.add(self.dismiss_details_button)


        self.knight_subclass_group = pygame.sprite.Group()
        self.knight_subclass_group.add(self.hospitaller_subclass_button)
        self.knight_subclass_group.add(self.executioner_subclass_button)
        self.knight_subclass_group.add(self.bulwark_subclass_button)
        self.knight_subclass_group.add(self.champion_subclass_button)

        self.mage_subclass_group = pygame.sprite.Group()
        self.mage_subclass_group.add(self.bloodmage_subclass_button)
        self.mage_subclass_group.add(self.shadowmage_subclass_button)
        self.mage_subclass_group.add(self.lifespringmage_subclass_button)
        self.mage_subclass_group.add(self.elementalmage_subclass_button)

        self.back_button_group = pygame.sprite.Group()
        self.back_button_group.add(self.go_back_button)

        self.feed_forward_button_group = pygame.sprite.Group()
        self.feed_forward_button_group.add(self.feed_forward_button)


        self.bg = pygame.image.load('assets/images/character_select_bg.png').convert_alpha()

        # Initialize text-related attributes
        self.narrative_text = "Welcome to The Abyssal Kingdoms traveler............prepare yourself."
        self.current_line = 0
        self.char_index = 0

    def draw_text(self,screen,text,font_name,font_size,speed,start_x,start_y,max_line_length):
        displayed_text = draw_text_one_letter_at_a_time(screen, text, font_name, font_size, 0.01, start_x, start_y, max_line_length)
        return displayed_text
    def reset_text_animation(self, new_text):
        self.current_line = 0
        self.char_index = 0
        self.class_declaration = new_text

    def write_text(self,start_x,start_y, text, font_size, text_color, font_path, stop_width):


        font = pygame.font.Font(font_path,font_size)
        font.set_bold(True)

        text_lines = text.split(' ')
        line = ""
        text_to_display = []
        for word in text_lines:
            if font.size(line + word)[0] >= self.screen_width - stop_width:
                text_to_display.append(line)
                line = word + " "
            else:
                line += word + " "
        if line:
            text_to_display.append(line)

        y = start_y

        for i in range(self.current_line):
            display_text(self.screen, text_to_display[i], (start_x, y), font, text_color, self.screen_width)
            y += font.get_linesize()

        if self.current_line < len(text_to_display):
            line = text_to_display[self.current_line]
            display_text(self.screen, line[:self.char_index], (self.start_text_x, y), font, text_color, self.screen_width)
            self.char_index += 1
            if self.char_index > len(line):
                self.char_index = 0
                self.current_line += 1

    def run(self):
        while self.main_game:
            self.main_timer += 0.25
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.main_game = False
                        pygame.quit()
                        sys.exit()

                if event.type == pygame.MOUSEBUTTONUP:

                    self.back_button_down = False
                    self.class_button_down = False
                    self.feed_forward_down = False
                    self.align_button_down = False
                    self.subclass_button_down = False
                    self.see_details_down = False
                    self.details_dismiss_down = False

                    if self.class_selection_state:
                        if self.choose_mage_button.hover:
                            self.mage_chosen = True
                            self.knight_chosen = False
                            self.rogue_chosen = False
                            self.brute_chosen = False

                            #modify player class data
                            self.character_profile["class"] = "mage"

                            self.reset_text_animation(Mage.mage_declaration(self))
                            self.class_button_down = False
                            self.class_button_up = True

                        if self.choose_knight_button.hover:
                            self.knight_chosen = True
                            self.mage_chosen = False
                            self.rogue_chosen = False
                            self.brute_chosen = False


                            #modify player class data
                            self.character_profile["class"] = "knight"

                            self.reset_text_animation(Knight.knight_declaration(self))
                            self.class_button_down = False
                            self.class_button_up = True

                        if self.choose_rogue_button.hover:
                            self.rogue_chosen = True
                            self.knight_chosen = False
                            self.mage_chosen = False
                            self.brute_chosen = False

                            #modify player class data
                            self.character_profile["class"] = "rogue"

                            self.reset_text_animation(Rogue.rogue_declaration(self))
                            self.class_button_down = False
                            self.class_button_up = True

                        if self.choose_brute_button.hover:
                            self.brute_chosen = True
                            self.mage_chosen = False
                            self.rogue_chosen = False
                            self.knight_chosen = False

                            self.character_profile["class"] = "brute"

                            self.reset_text_animation(Brute.brute_declaration(self))
                            self.class_button_down = False
                            self.class_button_up = True

                    if self.allignment_selection_state:

                        if self.lawfulGood_button.hover:
                            # modify player class data
                            self.character_profile["alignment"] = "Lawful Good"

                            self.reset_text_animation(Player.explain_allignment(self,"Lawful Good"))
                            self.align_button_down = False
                            self.align_button_up = True

                            self.LG_banner = True
                            self.NG_banner = False
                            self.CG_banner = False
                            self.LN_banner = False
                            self.TN_banner = False
                            self.CN_banner = False
                            self.LE_banner = False
                            self.NE_banner = False
                            self.CE_banner = False

                        elif self.neutralGood_button.hover:
                            # modify player class data
                            self.character_profile["alignment"] = "Neutral Good"

                            self.reset_text_animation(Player.explain_allignment(self, "Neutral Good"))
                            self.align_button_down = False
                            self.align_button_up = True

                            self.LG_banner = False
                            self.NG_banner = True
                            self.CG_banner = False
                            self.LN_banner = False
                            self.TN_banner = False
                            self.CN_banner = False
                            self.LE_banner = False
                            self.NE_banner = False
                            self.CE_banner = False


                        elif self.chaoticGood_button.hover:
                            # modify player class data
                            self.character_profile["alignment"] = "Chaotic Good"

                            self.reset_text_animation(Player.explain_allignment(self, "Chaotic Good"))
                            self.align_button_down = False
                            self.align_button_up = True

                            self.CG_banner = True
                            self.LG_banner = False
                            self.NG_banner = False
                            self.LN_banner = False
                            self.TN_banner = False
                            self.CN_banner = False
                            self.LE_banner = False
                            self.NE_banner = False
                            self.CE_banner = False

                        elif self.lawfulNeutral_button.hover:
                            # modify player class data
                            self.character_profile["alignment"] = "Lawful Neutral"

                            self.reset_text_animation(Player.explain_allignment(self, "Lawful Neutral"))
                            self.align_button_down = False
                            self.align_button_up = True

                            self.LN_banner = True
                            self.LG_banner = False
                            self.NG_banner = False
                            self.CG_banner = False
                            self.TN_banner = False
                            self.CN_banner = False
                            self.LE_banner = False
                            self.NE_banner = False
                            self.CE_banner = False

                        elif self.trueNeutral_button.hover:
                            # modify player class data
                            self.character_profile["alignment"] = "True Neutral"

                            self.reset_text_animation(Player.explain_allignment(self, "True Neutral"))
                            self.align_button_down = False
                            self.align_button_up = True

                            self.LN_banner = False
                            self.LG_banner = False
                            self.NG_banner = False
                            self.CG_banner = False
                            self.TN_banner = True
                            self.CN_banner = False
                            self.LE_banner = False
                            self.NE_banner = False
                            self.CE_banner = False

                        elif self.chaoticNeutral_button.hover:
                            # modify player class data
                            self.character_profile["alignment"] = "Chaotic Neutral"

                            self.reset_text_animation(Player.explain_allignment(self, "Chaotic Neutral"))
                            self.align_button_down = False
                            self.align_button_up = True

                            self.LN_banner = False
                            self.LG_banner = False
                            self.NG_banner = False
                            self.CG_banner = False
                            self.TN_banner = False
                            self.CN_banner = True
                            self.LE_banner = False
                            self.NE_banner = False
                            self.CE_banner = False

                        elif self.lawfulEvil_button.hover:
                            # modify player class data
                            self.character_profile["alignment"] = "Lawful Evil"

                            self.reset_text_animation(Player.explain_allignment(self, "Lawful Evil"))
                            self.align_button_down = False
                            self.align_button_up = True

                            self.LN_banner = False
                            self.LG_banner = False
                            self.NG_banner = False
                            self.CG_banner = False
                            self.TN_banner = False
                            self.CN_banner = False
                            self.LE_banner = True
                            self.NE_banner = False
                            self.CE_banner = False

                        elif self.neutralEvil_button.hover:
                            # modify player class data
                            self.character_profile["alignment"] = "Neutral Evil"

                            self.reset_text_animation(Player.explain_allignment(self, "Neutral Evil"))
                            self.align_button_down = False
                            self.align_button_up = True

                            self.LN_banner = False
                            self.LG_banner = False
                            self.NG_banner = False
                            self.CG_banner = False
                            self.TN_banner = False
                            self.CN_banner = False
                            self.LE_banner = False
                            self.NE_banner = True
                            self.CE_banner = False

                        elif self.chaoticEvil_button.hover:
                            # modify player class data
                            self.character_profile["alignment"] = "Chaotic Evil"

                            self.reset_text_animation(Player.explain_allignment(self, "Chaotic Evil"))
                            self.align_button_down = False
                            self.align_button_up = True

                            self.LN_banner = False
                            self.LG_banner = False
                            self.NG_banner = False
                            self.CG_banner = False
                            self.TN_banner = False
                            self.CN_banner = False
                            self.LE_banner = False
                            self.NE_banner = False
                            self.CE_banner = True

                    #subclass button clicks
                    if self.subclass_selection_state:

                        if self.see_details_button.hover:
                            self.details_selected = True
                            self.see_details_down = False
                            self.see_details_up = True

                        elif self.dismiss_details_button.hover:
                            self.details_selected = False
                            self.text_displayed = False
                            self.details_dismiss_down = False
                            self.details_dismiss_up = True



                        if self.character_profile['class'] == 'knight':
                            if self.hospitaller_subclass_button.hover and not self.details_selected:
                                self.character_profile['subclass'] = 'hospitaller'
                                self.hospitaller_chosen = True
                                self.champion_chosen = False
                                self.executioner_chosen = False
                                self.bulwark_chosen = False

                                self.subclass_button_down = False
                                self.subclass_button_up = True

                                self.reset_text_animation(Hospitaller.quote(self))

                            if self.executioner_subclass_button.hover and not self.details_selected:
                                self.character_profile['subclass'] = 'executioner'
                                self.executioner_chosen = True
                                self.champion_chosen = False
                                self.hospitaller_chosen = False
                                self.bulwark_chosen = False

                                self.subclass_button_down = False
                                self.subclass_button_up = True

                                self.reset_text_animation(Executioner.quote(self))

                            if self.bulwark_subclass_button.hover and not self.details_selected:
                                self.character_profile['subclass'] = 'bulwark'
                                self.bulwark_chosen = True
                                self.champion_chosen = False
                                self.hospitaller_chosen = False
                                self.executioner_chosen = False

                                self.subclass_button_down = False
                                self.subclass_button_up = True

                                self.reset_text_animation(Bulwark.quote(self))

                            if self.champion_subclass_button.hover and not self.details_selected:
                                self.character_profile['subclass'] = 'champion'
                                self.champion_chosen = True
                                self.bulwark_chosen = False
                                self.hospitaller_chosen = False
                                self.executioner_chosen = False

                                self.subclass_button_down = False
                                self.subclass_button_up = True

                                self.reset_text_animation(Champion.quote(self))

                        elif self.character_profile['class'] == 'mage':
                            if self.bloodmage_subclass_button.hover and not self.details_selected:
                                self.character_profile['subclass'] = 'bloodmage'
                                self.bloodmage_chosen = True
                                self.shadowmage_chosen = False
                                self.lifespring_chosen = False
                                self.elemental_chosen = False
                                self.reset_text_animation(BloodMage.quote(self))

                            if self.shadowmage_subclass_button.hover and not self.details_selected:
                                self.character_profile['subclass'] = 'shadowmage'
                                self.shadowmage_chosen = True
                                self.bloodmage_chosen = False
                                self.lifespring_chosen = False
                                self.elemental_chosen = False
                                self.reset_text_animation(ShadowMage.quote(self))

                            if self.lifespringmage_subclass_button.hover and not self.details_selected:
                                self.character_profile['subclass'] = 'lifespring'
                                self.lifespring_chosen = True
                                self.shadowmage_chosen = False
                                self.bloodmage_chosen = False
                                self.elemental_chosen = False
                                self.reset_text_animation(LifeSpring.quote(self))

                            if self.elementalmage_subclass_button.hover and not self.details_selected:
                                self.character_profile['subclass'] = 'elemental'
                                self.elemental_chosen = True
                                self.lifespring_chosen = False
                                self.shadowmage_chosen = False
                                self.bloodmage_chosen = False
                                self.reset_text_animation(ElementalMage.quote(self))




                    if self.feed_forward_button.hover:
                        self.feed_forward_down = False
                        self.feed_forward_up = True
                        self.reset_text_animation('')
                        if self.class_selection_state:
                            if self.character_profile['class']:
                                self.class_selection_state = False
                                self.allignment_selection_state = True
                        elif self.allignment_selection_state:
                            if self.character_profile['alignment']:
                                self.allignment_selection_state = False
                                self.class_selection_state = False
                                self.subclass_selection_state = True
                                #self.details_selected = False


                        self.LG_banner = False
                        self.NG_banner = False
                        self.CG_banner = False
                        self.LN_banner = False
                        self.TN_banner = False
                        self.CN_banner = False
                        self.LE_banner = False
                        self.NE_banner = False
                        self.CE_banner = False

                    if self.go_back_button.hover:
                        self.details_selected = False
                        self.LG_banner = False
                        self.NG_banner = False
                        self.CG_banner = False
                        self.LN_banner = False
                        self.TN_banner = False
                        self.CN_banner = False
                        self.LE_banner = False
                        self.NE_banner = False
                        self.CE_banner = False


                        if self.class_selection_state:
                            self.main_game = False
                            self.main_controller().switch_to_start_screen()
                            self.character_profile['class'] = None
                            self.optionsPanel_counter = 0
                        elif self.allignment_selection_state:
                            self.class_selection_state = True
                            self.allignment_selection_state = False
                            self.character_profile['alignment'] = None
                            self.character_profile['class'] = None
                        elif self.subclass_selection_state:



                            self.class_selection_state = False
                            self.allignment_selection_state = True
                            self.character_profile['subclass'] = None
                            self.character_profile['alignment'] = None

                            self.hospitaller_chosen = False
                            self.executioner_chosen = False
                            self.bulwark_chosen = False
                            self.champion_chosen = False
                            self.bloodmage_chosen = False
                            self.shadowmage_chosen = False
                            self.lifespring_chosen = False
                            self.elemental_chosen = False
                            self.subclass_selection_state = False







                        self.back_button_down = False
                        self.back_button_up = True
                        self.mage_chosen = False
                        self.knight_chosen = False
                        self.rogue_chosen = False
                        self.brute_chosen = False
                        self.reset_text_animation('')



                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.class_selection_state:
                        if (self.choose_mage_button.hover or self.choose_knight_button.hover
                                or self.choose_rogue_button.hover or self.choose_brute_button.hover):
                            self.class_button_down = True
                            self.class_button_up = False
                    if self.allignment_selection_state:
                        if self.lawfulGood_button.hover:
                            self.align_button_down = True
                            self.align_button_up = False

                        if self.neutralGood_button.hover:
                            self.align_button_down = True
                            self.align_button_up = False

                        if self.chaoticGood_button.hover:
                            self.align_button_down = True
                            self.align_button_up = False

                        if self.lawfulNeutral_button.hover:
                            self.align_button_down = True
                            self.align_button_up = False

                        if self.trueNeutral_button.hover:
                            self.align_button_down = True
                            self.align_button_up = False

                        if self.chaoticNeutral_button.hover:
                            self.align_button_down = True
                            self.align_button_up = False

                        if self.lawfulEvil_button.hover:
                            self.align_button_down = True
                            self.align_button_up = False

                        if self.neutralEvil_button.hover:
                            self.align_button_down = True
                            self.align_button_up = False

                        if self.chaoticEvil_button.hover:
                            self.align_button_down = True
                            self.align_button_up = False

                    if self.subclass_selection_state:
                        if self.see_details_button.hover:

                            self.see_details_down = True
                            self.see_details_up = False

                        if self.dismiss_details_button.hover:
                            self.details_dismiss_down = True
                            self.details_dismiss_up = False


                        if self.character_profile['class'] == 'knight':
                            if self.hospitaller_subclass_button.hover:
                                self.subclass_button_down = True
                                self.subclass_button_up = False
                            if self.executioner_subclass_button.hover:
                                self.subclass_button_down = True
                                self.subclass_button_up = False
                            if self.bulwark_subclass_button.hover:
                                self.subclass_button_down = True
                                self.subclass_button_up = False
                            if self.champion_subclass_button.hover:
                                self.subclass_button_down = True
                                self.subclass_button_up = False

                        elif self.character_profile['class'] == 'mage':
                            if self.bloodmage_subclass_button.hover:
                                self.subclass_button_down = True
                                self.subclass_button_up = False
                            if self.shadowmage_subclass_button.hover:
                                self.subclass_button_down = True
                                self.subclass_button_up = False
                            if self.lifespringmage_subclass_button.hover:
                                self.subclass_button_down = True
                                self.subclass_button_up = False
                            if self.elementalmage_subclass_button.hover:
                                self.subclass_button_down = True
                                self.subclass_button_up = False


                    if self.feed_forward_button.hover:
                        self.feed_forward_down = True
                        self.feed_forward_up = False

                    if self.go_back_button.hover:
                        self.back_button_down = True
                        self.back_button_up = False

            # Class button animations
            if self.class_button_down and self.choose_mage_button.hover:
                self.choose_mage_button.image = self.mage_button[1]
            else:
                self.choose_mage_button.image = self.mage_button[0]

            if self.class_button_down and self.choose_knight_button.hover:
                self.choose_knight_button.image = self.knight_button[1]
            else:
                self.choose_knight_button.image = self.knight_button[0]

            if self.class_button_down and self.choose_rogue_button.hover:
                self.choose_rogue_button.image = self.rogue_button[1]
            else:
                self.choose_rogue_button.image = self.rogue_button[0]

            if self.class_button_down and self.choose_brute_button.hover:
                self.choose_brute_button.image = self.brute_button[1]
            else:
                self.choose_brute_button.image = self.brute_button[0]

            if self.back_button_down and self.go_back_button.hover:
                self.go_back_button.image = self.back_button[1]
            else:
                self.go_back_button.image = self.back_button[0]

            if self.class_selection_state:

                if self.feed_forward_down and self.feed_forward_button.hover:
                    self.feed_forward_button.image = self.choose_alignment_button[1]
                else:
                    self.feed_forward_button.image = self.choose_alignment_button[0]
            if self.allignment_selection_state:
                if self.feed_forward_down and self.feed_forward_button.hover:
                    self.feed_forward_button.image = self.choose_subclass_button[1]
                else:
                    self.feed_forward_button.image = self.choose_subclass_button[0]



                #Alignment button animations
            if self.align_button_down and self.lawfulGood_button.hover:
                self.lawfulGood_button.image = self.lawful_good_button[1]
            else:
                self.lawfulGood_button.image = self.lawful_good_button[0]

            if self.align_button_down and self.neutralGood_button.hover:
                self.neutralGood_button.image = self.neutral_good_button[1]
            else:
                self.neutralGood_button.image = self.neutral_good_button[0]

            if self.align_button_down and self.chaoticGood_button.hover:
                self.chaoticGood_button.image = self.chaotic_good_button[1]
            else:
                self.chaoticGood_button.image = self.chaotic_good_button[0]

            if self.align_button_down and self.lawfulNeutral_button.hover:
                self.lawfulNeutral_button.image = self.lawful_neutral_button[1]
            else:
                self.lawfulNeutral_button.image = self.lawful_neutral_button[0]

            if self.align_button_down and self.trueNeutral_button.hover:
                self.trueNeutral_button.image = self.true_neutral_button[1]
            else:
                self.trueNeutral_button.image = self.true_neutral_button[0]

            if self.align_button_down and self.chaoticNeutral_button.hover:
                self.chaoticNeutral_button.image = self.chaotic_neutral_button[1]
            else:
                self.chaoticNeutral_button.image = self.chaotic_neutral_button[0]

            if self.align_button_down and self.lawfulEvil_button.hover:
                self.lawfulEvil_button.image = self.lawful_evil_button[1]
            else:
                self.lawfulEvil_button.image = self.lawful_evil_button[0]

            if self.align_button_down and self.neutralEvil_button.hover:
                self.neutralEvil_button.image = self.neutral_evil_button[1]
            else:
                self.neutralEvil_button.image = self.neutral_evil_button[0]

            if self.align_button_down and self.chaoticEvil_button.hover:
                self.chaoticEvil_button.image = self.chaotic_evil_button[1]
            else:
                self.chaoticEvil_button.image = self.chaotic_evil_button[0]

            #subclass button animations
            if self.see_details_down and self.see_details_button.hover:
                self.see_details_button.image = self.details_button[1]

            else:
                self.see_details_button.image = self.details_button[0]

            if self.details_dismiss_down and self.dismiss_details_button.hover:
                self.dismiss_details_button.image = self.details_dismiss_button[1]
            else:
                self.dismiss_details_button.image = self.details_dismiss_button[0]

            if self.subclass_button_down and self.character_profile['class'] == 'knight' and self.hospitaller_subclass_button.hover:
                self.hospitaller_subclass_button.image = self.hospitaller_button[1]
            else:
                self.hospitaller_subclass_button.image = self.hospitaller_button[0]

            if self.subclass_button_down and self.character_profile['class'] == 'knight' and self.executioner_subclass_button.hover:
                self.executioner_subclass_button.image = self.executioner_button[1]
            else:
                self.executioner_subclass_button.image = self.executioner_button[0]

            if self.subclass_button_down and self.character_profile['class'] == 'knight' and self.bulwark_subclass_button.hover:
                self.bulwark_subclass_button.image = self.bulwark_button[1]
            else:
                self.bulwark_subclass_button.image = self.bulwark_button[0]

            if self.subclass_button_down and self.character_profile['class'] == 'knight' and self.champion_subclass_button.hover:
                self.champion_subclass_button.image = self.champion_button[1]
            else:
                self.champion_subclass_button.image = self.champion_button[0]

            if self.subclass_button_down and self.character_profile['class'] == 'mage' and self.bloodmage_subclass_button.hover:
                self.bloodmage_subclass_button.image = self.bloodmage_button[1]
            else:
                self.bloodmage_subclass_button.image = self.bloodmage_button[0]

            if self.subclass_button_down and self.character_profile['class'] == 'mage' and self.shadowmage_subclass_button.hover:
                self.shadowmage_subclass_button.image = self.shadowmage_button[1]
            else:
                self.shadowmage_subclass_button.image = self.shadowmage_button[0]

            if self.subclass_button_down and self.character_profile['class'] == 'mage' and self.lifespringmage_subclass_button.hover:
                self.lifespringmage_subclass_button.image = self.lifespringmage_button[1]
            else:
                self.lifespringmage_subclass_button.image = self.lifespringmage_button[0]

            if self.subclass_button_down and self.character_profile['class'] == 'mage' and self.elementalmage_subclass_button.hover:
                self.elementalmage_subclass_button.image = self.elementalmage_button[1]
            else:
                self.elementalmage_subclass_button.image = self.elementalmage_button[0]


            # Option panel animation
            self.optionsPanel_counter_counter += 1
            if self.optionsPanel_counter_counter % 1 == 0:
                self.optionsPanel_counter += 1
            if self.optionsPanel_counter > 5:
                self.optionsPanel_counter = 5

            self.optionsPanel = self.option_panel[self.optionsPanel_counter]

            # Mage animation
            if self.mage_chosen:
                self.mage_counter_counter += 1
                if self.mage_counter_counter % 2 == 0:
                    self.mage_counter += 1
                if self.mage_counter > 29:
                    self.mage_counter = 0

                self.mage_select = self.mage_ani[self.mage_counter]

            # Knight animation

            if self.knight_chosen:
                self.knight_counter_counter += 1
                if self.knight_counter_counter % 2 == 0:
                    self.knight_counter += 1
                if self.knight_counter > 22:
                    self.knight_counter = 0

                self.knight_select = self.knight_ani[self.knight_counter]

            mouse_pos = pygame.mouse.get_pos()
            self.mouse_pos = mouse_pos

            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(self.optionsPanel, (150, 110))

            if self.optionsPanel_counter == 5:
                self.back_button_group.update()
                self.feed_forward_button_group.update()


                self.back_button_group.draw(self.screen)
                self.feed_forward_button_group.draw(self.screen)

                if self.class_selection_state:
                    self.class_button_group.update()
                    self.class_button_group.draw(self.screen)
                elif self.allignment_selection_state:
                    self.alignment_button_group.update()
                    self.alignment_button_group.draw(self.screen)
                elif self.subclass_selection_state:

                    if self.character_profile['subclass']:
                        self.subclass_screen_button_group.update()
                        if not self.details_selected:
                            self.subclass_screen_button_group.draw(self.screen)

                    if self.character_profile['class'] == 'knight':
                        self.knight_subclass_group.update()
                        if not self.details_selected:
                            self.knight_subclass_group.draw(self.screen)
                    elif self.character_profile['class'] == 'mage':
                        self.mage_subclass_group.update()
                        if not self.details_selected:
                            self.mage_subclass_group.draw(self.screen)



            if self.class_selection_state:
                #self.feed_forward_button.image = self.choose_alignment_button[0]
                if self.mage_chosen:
                    self.screen.blit(self.mage_select, (700, 350))

                if self.knight_chosen:
                    self.screen.blit(self.knight_select, (720, 390))

            if (self.choose_mage_button.hover or self.choose_knight_button.hover
                    or self.choose_rogue_button.hover or self.choose_brute_button.hover or self.go_back_button.hover
                    or self.feed_forward_button.hover or self.lawfulGood_button.hover
                    or self.neutralGood_button.hover or self.chaoticGood_button.hover
                    or self.lawfulNeutral_button.hover or self.trueNeutral_button.hover
                    or self.chaoticNeutral_button.hover or self.lawfulEvil_button.hover
                    or self.neutralEvil_button.hover or self.chaoticEvil_button.hover
                    or self.hospitaller_subclass_button.hover or self.executioner_subclass_button.hover
                    or self.see_details_button.hover or self.bulwark_subclass_button.hover
                    or self.champion_subclass_button.hover or self.bloodmage_subclass_button.hover
                    or self.shadowmage_subclass_button.hover or self.lifespringmage_subclass_button.hover
                    or self.elementalmage_subclass_button.hover):

                pygame.mouse.set_visible(False)
                self.screen.blit(self.gauntlet_cursor, self.mouse_pos)
            else:
                pygame.mouse.set_visible(True)
            if self.class_selection_state:
                self.write_text(self.start_text_x,self.start_text_y,self.class_declaration, 34, (255, 255, 0),"assets/fonts/Primitive.ttf",900)

                self.screen.blit(self.class_heading,(205,10))

            if self.allignment_selection_state:
                self.details_selected = False
                #self.feed_forward_button.image = self.choose_subclass_button[0]
                self.write_text(700,300,self.class_declaration, 34, (255, 255, 0), "assets/fonts/Primitive.ttf",900)
                self.screen.blit(self.align_heading,(205,10))
                if self.LG_banner:
                    self.screen.blit(self.lawfulGood_banner,(750,30))
                elif self.NG_banner:
                    self.screen.blit(self.neutralGood_banner, (750, 30))
                elif self.CG_banner:
                    self.screen.blit(self.chaoticGood_banner, (750, 30))
                elif self.LN_banner:
                    self.screen.blit(self.lawfulNeutral_banner, (750, 30))
                elif self.TN_banner:
                    self.screen.blit(self.trueNeutral_banner, (750, 30))
                elif self.CN_banner:
                    self.screen.blit(self.chaoticNeutral_banner, (750, 30))
                elif self.LE_banner:
                    self.screen.blit(self.lawfulEvil_banner, (750, 30))
                elif self.NE_banner:
                    self.screen.blit(self.neutralEvil_banner, (750, 30))
                elif self.CE_banner:
                    self.screen.blit(self.chaoticEvil_banner, (750, 30))

            if self.subclass_selection_state:
                self.screen.blit(self.subclass_heading, (205, 10))



                if self.hospitaller_chosen and not self.details_selected:
                    self.screen.blit(self.hospitaller_portrait, (1050,200))
                    self.screen.blit(self.hospitaller_banner, (625, 40))
                   # self.screen_rect.fill((0,0,0))
                    #self.screen_rect.set_alpha(160)
                    #self.screen.blit(self.screen_rect, (0,0))



                    self.write_text(700,250,self.class_declaration,40,(255,255,0),"assets/fonts/Primitive.ttf",1100)

                if self.bulwark_chosen and not self.details_selected:
                    self.screen.blit(self.bulwark_portrait, (800,180))
                    self.screen.blit(self.bulwark_banner, (625, 40))

                    self.write_text(700,250,self.class_declaration,40,(255,255,0),"assets/fonts/Primitive.ttf",1100)

                if self.champion_chosen and not self.details_selected:
                    self.screen.blit(self.champion_portrait, (1090,350))
                    self.screen.blit(self.champion_banner, (625, 40))

                    self.write_text(700,250,self.class_declaration,40,(255,255,0),"assets/fonts/Primitive.ttf",1100)


                if self.executioner_chosen and not self.details_selected:
                    self.screen.blit(self.executioner_portrait, (800,200))
                    self.screen.blit(self.executioner_banner, (625, 40))
                    self.write_text(700, 250, self.class_declaration, 40, (255, 255, 0), "assets/fonts/Primitive.ttf",
                                    1100)

                if self.bloodmage_chosen and not self.details_selected:
                    self.screen.blit(self.bloodmage_portrait, (1070,240))
                    self.screen.blit(self.bloodmage_banner, (625, 40))
                    self.write_text(700, 250, self.class_declaration, 40, (255, 255, 0), "assets/fonts/Primitive.ttf",
                                    1100)
                if self.shadowmage_chosen and not self.details_selected:
                    self.screen.blit(self.shadowmage_portrait, (1070,280))
                    self.screen.blit(self.shadowmage_banner, (625, 40))
                    self.write_text(700, 250, self.class_declaration, 40, (255, 255, 0), "assets/fonts/Primitive.ttf",
                                    1100)
                if self.lifespring_chosen and not self.details_selected:
                    self.screen.blit(self.lifespringmage_portrait, (1070,280))
                    self.screen.blit(self.lifespringmage_banner, (625, 40))
                    self.write_text(700, 250, self.class_declaration, 40, (255, 255, 0), "assets/fonts/Primitive.ttf",
                                    1100)

                if self.elemental_chosen and not self.details_selected:
                    self.screen.blit(self.elementalmage_portrait, (1070, 280))
                    self.screen.blit(self.elementalmage_banner, (625, 40))
                    self.write_text(700, 250, self.class_declaration, 40, (255, 255, 0), "assets/fonts/Primitive.ttf",
                                    1100)


                elif self.details_selected:
                    self.screen.blit(self.screen_rect,(0,0))
                    self.screen_rect.set_alpha(200)

                    if self.character_profile['subclass'] == 'executioner':
                        self.screen.blit(self.executioner_border, (0, 0))


                        if not self.text_displayed:
                            draw_text_one_letter_at_a_time(self,self.screen,Executioner.explain_subclass(self),"assets/fonts/Primitive.ttf",
                                                           34,0.025,150,50,1300)
                        self.text_displayed = True

                        self.screen.blit(self.text_surface,(0,0))
                        self.dismiss_details_button.rect.y = 450
                        self.dismiss_button_group.update()
                        self.dismiss_button_group.draw(self.screen)

                    elif self.character_profile['subclass'] == 'hospitaller':
                        self.screen.blit(self.hospitaller_border, (0, 0))

                        if not self.text_displayed:
                            draw_text_one_letter_at_a_time(self, self.screen, Hospitaller.explain_subclass(self),
                                                           "assets/fonts/Primitive.ttf",
                                                           34, 0.025, 150, 50, 1300)
                        self.text_displayed = True

                        self.screen.blit(self.text_surface, (0, 0))
                        self.dismiss_details_button.rect.y = 450
                        self.dismiss_button_group.update()
                        self.dismiss_button_group.draw(self.screen)

                    elif self.character_profile['subclass'] == 'bulwark':
                        self.screen.blit(self.bulwark_border, (0, 0))

                        if not self.text_displayed:
                            draw_text_one_letter_at_a_time(self, self.screen, Bulwark.explain_subclass(self),
                                                           "assets/fonts/Primitive.ttf",
                                                           34, 0.025, 110, 20, 1450)
                        self.text_displayed = True
                        self.dismiss_details_button.y = 650
                        self.dismiss_details_button.x = 800
                        self.screen.blit(self.text_surface, (0, 0))
                        self.dismiss_details_button.rect.y = 450
                        self.dismiss_button_group.update()
                        self.dismiss_button_group.draw(self.screen)

                    elif self.character_profile['subclass'] == 'champion':
                        self.screen.blit(self.champion_border, (0, 0))

                        if not self.text_displayed:
                            draw_text_one_letter_at_a_time(self, self.screen, Champion.explain_subclass(self),
                                                           "assets/fonts/Primitive.ttf",
                                                           34, 0.025, 150, 50, 1300)
                        self.text_displayed = True

                        self.screen.blit(self.text_surface, (0, 0))
                        self.dismiss_details_button.rect.y = 450
                        self.dismiss_button_group.update()
                        self.dismiss_button_group.draw(self.screen)

                    elif self.character_profile['subclass'] == 'bloodmage':
                        self.screen.blit(self.bloodmage_border, (0, 0))

                        if not self.text_displayed:
                            draw_text_one_letter_at_a_time(self, self.screen, BloodMage.explain_subclass(self),
                                                           "assets/fonts/Primitive.ttf",
                                                           34, 0.025, 110, 20, 1400)
                        self.text_displayed = True

                        self.screen.blit(self.text_surface, (0, 0))
                        self.dismiss_details_button.rect.y = 620
                        self.dismiss_button_group.update()
                        self.dismiss_button_group.draw(self.screen)

                    elif self.character_profile['subclass'] == 'shadowmage':
                        self.screen.blit(self.shadowmage_border, (0, 0))

                        if not self.text_displayed:
                            draw_text_one_letter_at_a_time(self, self.screen, ShadowMage.explain_subclass(self),
                                                           "assets/fonts/Primitive.ttf",
                                                           34, 0.025, 110, 20, 1400)
                        self.text_displayed = True

                        self.screen.blit(self.text_surface, (0, 0))
                        self.dismiss_details_button.rect.y = 620
                        self.dismiss_button_group.update()
                        self.dismiss_button_group.draw(self.screen)

                    elif self.character_profile['subclass'] == 'lifespring':
                        self.screen.blit(self.lifespringmage_border, (0, 0))

                        if not self.text_displayed:
                            draw_text_one_letter_at_a_time(self, self.screen, LifeSpring.explain_subclass(self),
                                                           "assets/fonts/Primitive.ttf",
                                                           34, 0.025, 110, 20, 1400)
                        self.text_displayed = True

                        self.screen.blit(self.text_surface, (0, 0))
                        self.dismiss_details_button.rect.y = 620
                        self.dismiss_button_group.update()
                        self.dismiss_button_group.draw(self.screen)

                    elif self.character_profile['subclass'] == 'elemental':
                        self.screen.blit(self.elementalmage_border, (0, 0))

                        if not self.text_displayed:
                            draw_text_one_letter_at_a_time(self, self.screen, ElementalMage.explain_subclass(self),
                                                           "assets/fonts/Primitive.ttf",
                                                           34, 0.025, 110, 35, 1400)
                        self.text_displayed = True

                        self.screen.blit(self.text_surface, (0, 0))
                        self.dismiss_details_button.rect.y = 620
                        self.dismiss_button_group.update()
                        self.dismiss_button_group.draw(self.screen)

            print(f"allignment state: {self.allignment_selection_state}; details selected: {self.details_selected}; text displayed: {self.text_displayed}")
            pygame.display.flip()
            pygame.time.delay(50)

# Create game instance and run it
