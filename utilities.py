import pygame
import os
import sys
import time


def change_opacity(self,img):
    for opacity in range(255, 0, -15):
        work_img = img.copy()
        pygame.draw.rect(work_img, (0, 0, 0, opacity), (0, 0, 640, 480))
        self.screen.blit(work_img, (0, 0))
        pygame.display.flip()
        pygame.time.delay(100)



def load_images(path, suffix, lst):

    for image in os.listdir(str(path)):
        if image.endswith(str(suffix)):
            lst.append(pygame.image.load(str(path) + str(image)).convert_alpha())

import csv
from typing import Dict, List

def update_csv(filename: str, data: List[Dict[str, str]], rewrite: bool = False, unique_key: str = 'Name'):
    """
    Update or write data to a CSV file.

    Args:
        filename (str): The name of the CSV file.
        data (List[Dict[str, str]]): A list of dictionaries containing the data to write or update.
        rewrite (bool): If True, rewrites the entire CSV file. If False, updates specific values.
        unique_key (str): The key used to identify unique rows for updating. Default is 'Name'.
    """
    if rewrite:
        # Rewrite the entire CSV file with the new data
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = data[0].keys()  # Use the keys from the first dictionary as the fieldnames
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    else:
        # Read existing data from the CSV file
        existing_data = []
        try:
            with open(filename, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                existing_data = [row for row in reader]
        except FileNotFoundError:
            # If the file does not exist, initialize it with the new data
            existing_data = []

        # Update the existing data with the new data
        for new_row in data:
            found = False
            for existing_row in existing_data:
                if existing_row.get(unique_key) == new_row.get(unique_key):
                    existing_row.update(new_row)
                    found = True
                    break
            if not found:
                existing_data.append(new_row)

        # Write the updated data back to the CSV file
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = existing_data[0].keys() if existing_data else data[0].keys()  # Ensure we have fieldnames
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(existing_data)



def display_text(screen, text, pos, font, color, screen_width):
    """Displays text on the screen with word wrapping."""
    words = text.split(' ')
    space_width, _ = font.size(' ')
    x, y = pos
    line_height = font.get_linesize()

    for word in words:
        word_surface = font.render(word, True, color)
        word_width, _ = word_surface.get_size()

        if x + word_width >= screen_width:
            x = pos[0]
            y += line_height

        for char in word:
            char_surface = font.render(char, True, color)
            char_width, _ = char_surface.get_size()
            screen.blit(char_surface, (x, y))
            x += char_width

        x += space_width  # Add space after the word

def draw_text_one_letter_at_a_time(game,screen, text, font_name, font_size, speed, start_x, start_y, max_line_length):
    counter = 0
    """
    Draws text on the Pygame screen one character at a time with specified parameters.

    Parameters:
    - screen: The Pygame screen surface where the text will be drawn.
    - text: The string of text to be drawn.
    - font_name: The name of the font file (e.g., 'assets/fonts/Primitive.ttf').
    - font_size: The size of the font.
    - speed: The speed at which the text is written (in seconds between each character).
    - start_x: The x-coordinate of the starting position for the text.
    - start_y: The y-coordinate of the starting position for the text.
    - max_line_length: The maximum length (in pixels) of each line of text before wrapping to the next line.
    """

    pygame.font.init()
    font = pygame.font.Font(font_name, font_size)
    x, y = start_x, start_y
    current_line = ""
    words = text.split(' ')

    # List to store each character to be displayed later
    display_chars = []
    for word in words:
        test_line = f"{current_line} {word}".strip()
        test_surface = font.render(test_line, True, (255, 255, 255))

        if test_surface.get_width() > max_line_length and current_line:
            # Add current line to display_chars
            display_chars.append(current_line)
            current_line = word
        else:
            current_line = test_line

    # Add the last line to display_chars
    display_chars.append(current_line)

    # Create a new surface for the text
    text_surface = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
    #text_surface = game.screen_rect
    #text_surface.set_alpha(200)
    text_surface.fill((0, 0, 0, 0))  # Make it transparent
    #text_surface.set_alpha(0)


    # Draw text one character at a time

    for line in display_chars:
        for char in line:
            char_surface = font.render(char, True, (255, 255, 255))
            text_surface.blit(char_surface, (x, y))
            screen.blit(text_surface, (0, 0))
            pygame.display.flip()
            x += char_surface.get_width()
            time.sleep(speed)

            # Event handling to allow exiting
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()

        # Move to next line
        x = start_x
        y += font.get_height()
    game.text_surface = text_surface

    #game.text_surface.set_alpha(0)
    # Keep the final text surface on the screen without clearing it
    #screen.blit(text_surface, (0, 0))


class Buttons(pygame.sprite.Sprite):
    def __init__(self,game,x,y,image,alpha,fade):
        super().__init__()
        self.game = game
        self.image = image
        self.alpha = alpha
        self.image.set_alpha(self.alpha)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.hover = False
        self.alpha_velocity = 0.2
        self.fade = fade




    def update(self):
        self.game.screen.blit(self.image,(self.rect.x,self.rect.y))






        print(self.alpha_velocity)

        if self.rect.collidepoint(self.game.mouse_pos):
            self.hover = True
            print("Contact!")
        else:
            self.hover = False
            print("No Contact!")


