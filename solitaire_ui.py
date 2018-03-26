import os
import pygame
import colors
import solitaire_logic

import random

LEFT_MOUSE_BUTTON = 1
RIGHT_MOUSE_BUTTON = 3


class SolitaireGame:
    def __init__(self, init_width: int, init_height: int):
        self.init_width = init_width
        self.init_height = init_height
        self._clock = pygame.time.Clock()
        self._running = True

        self._game_state = solitaire_logic.GameState()

    def _init_pygame(self) -> None:
        '''
        Initializes pygame (font, caption, display)
        '''
        pygame.init()

        self.main_font = pygame.font.SysFont('arial', 16)
        self._images = self._load_images()

        pygame.display.set_caption('Solitaire2')
        self._resize_surface((self.init_width, self.init_height))

    def _load_images(self) -> {str: pygame.Surface}:
        '''
        Loads all the card images (including the card backs) into a 
        dictionary where the file name is the key and the image is
        the value
        '''
        images_dict = {}
        for pile in self._game_state.piles:
            for card in pile:
                path = os.path.join('resources', 'cards', card.image_filename)
                images_dict[card.image_filename] = pygame.image.load(path)
        images_dict['card_back.jpg'] = pygame.image.load(os.path.join('resources', 'card_back.jpg'))
        return images_dict

    def _resize_surface(self, size: (int, int)) -> None:
        '''
        Sets the mode of the pygame surface to the specified size with 
        the flag of RESIZABLE
        '''
        pygame.display.set_mode(size, pygame.RESIZABLE)

    def run(self) -> None:
        self._init_pygame()
        while self._running:
            self._handle_events()
            self._redraw()

    def _handle_events(self) -> None:
        '''
        Handles all of pygame's events
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit()
            elif event.type == pygame.VIDEORESIZE:
                self._resize_surface(event.size)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._handle_click(event.button)

    def _handle_click(self, button: int) -> None:
        '''
        Handles the mouse click, needs to know which mouse button is clicked
        '''
        mouse_position = pygame.mouse.get_pos()
        if button == LEFT_MOUSE_BUTTON:
            print('LEFT click at', mouse_position)
        elif button == RIGHT_MOUSE_BUTTON:
            print('RIGHT click at', mouse_position)

    def _redraw(self) -> None:
        '''
        Redraws the surface to display the solitaire table
        '''
        surface = pygame.display.get_surface()
        surface.fill(colors.BLUE)

        for pile in self._game_state.piles:
            for card in pile:
                surface.blit(self._images[card.image_filename], (random.randint(0, 1000), random.randint(0, 800)))

        pygame.display.flip()

    def _quit(self) -> None:
        self._running = False


if __name__ == '__main__':
    game = SolitaireGame(1000, 800)
    print(game._game_state)
    game.run()
