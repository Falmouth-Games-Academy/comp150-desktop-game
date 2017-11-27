import sys
import pygame
import pickle

from sprite import Sprite
from button import Button
from get_images import GetImages

class CharacterCreation:

    # index checking to save the position is probably not necessary. Character creation menu doesn't really need to save user's position

    """
    CharacterCreation class. This class displays a character creation window and allows the user to edit the apperance
    of their character.

    Attributes:
        path_to_assets (string): The file path to the assets folder. This should later be added to the constructor so it can be passed in when the class is instantiated.
        blank_component (image): A blank image that is used as a placeholder
        blank_base (image): The image used for the base of the sprite

        main_screen (pygame.Display): The character creation window
        background_colour (pygame.Colour): The colour for the main window.
        buttons (list of Buttons): A list of the Buttons on the screen.

        char_position (tuple): The position of the player_char on the screen.
        player_char (Sprite): The player character's Sprite. player_char.image used to access the image

        body_choices (list of Surfaces): The images that the player can choose from for the body component.
        hair_choices (list of Surfaces): The images that the player can choose from for the hair component.
        legs_choices (list of Surfaces): The images that the player can choose from for the legs component.

        body_index (int): The position in the body_choices array. Used to save the user's place.
        hair_index (int): The position in the hair_choices array. Used to save the user's place.
        legs_index (int): The position in the legs_choices array. Used to save the user's place.

        # These are set in __init__ so that length only has to be calculated once.
        body_choices_length (int): The length of the body_choices list.
        hair_choices_length (int): The length of the hair_choices list.
        legs_choices_length (int): The length of the legs_choices list.

        running (bool): State of the pygame window. Window remains open while running is True.
    """

    # path_to_assets = "../Assets"
    path_to_assets = "SpriteGeneration/Assets"
    blank_component = pygame.image.load(path_to_assets + "/Sprites/blankComponent.png")
    blank_base = pygame.image.load(path_to_assets + "/Sprites/base/base1.png")

    main_screen = None
    background_colour = (222, 184, 135)
    buttons = []

    char_position = (326, 236)
    player_char = None

    body_choices = []
    hair_choices = []
    legs_choices = []

    body_index = -1
    hair_index = -1
    legs_index = -1

    body_choices_length = 0
    hair_choices_length = 0
    legs_choices_length = 0

    running = True

    def __init__(self, screen, hair_list, body_list, legs_list, sprite_size):
        """
        Constructor method.

        Args:
            screen (pygame.Display): The display to draw the creation screen on. This will likely be the main game screen.
            hair_list (list of images): The images that can be chosen for the character's head.
            body_list (list of images): The images that can be chosen for the character's body.
            legs_list (list of images): The images that can be chosen for the character's legs.
            sprite_size (tuple): The size the player sprite should be in game, in pixels.
        """

        self.screen = screen
        self.size = screen.get_size()

        self.hair_choices = hair_list
        self.body_choices = body_list
        self.legs_choices = legs_list

        self.body_choices_length = len(self.body_choices)
        self.hair_choices_length = len(self.hair_choices)
        self.legs_choices_length = len(self.legs_choices)

        self.sprite_size = sprite_size

        # Get the position in the component lists from the last session.
        self.read_component_index("char_creation_index.txt")
        self.player_char = self.load_blank_sprite()

    def draw_win(self):
        """Main method for the class. This creates the character creation window and checks for player input."""

        print("Drawing screen for first time")

        self.screen.fill(self.background_colour)

        self.create_buttons()
        self.update_screen()

        # Loop to keep window open and check for events
        while self.running:
            for event in pygame.event.get():

                # Each button checks if it was clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        button.check_click(pygame.mouse.get_pos())

                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit()

    def update_screen(self):
        """Updates the character creation screen. Blits the character sprite to the screen and updates it."""

        self.screen.blit(self.player_char.image, self.char_position)
        pygame.display.flip()

        print("Screen updated")

    def load_blank_sprite(self):
        """
        Instantiates a new Sprite with a blank base and blank components as placeholders and draws the sprite image.

        Returns:
            blank_sprite (Sprite): A Sprite with base image and blank components.
        """

        # Create and draw a new sprite with a base image and the last used components
        blank_sprite = Sprite((128, 128), self.background_colour, pygame.transform.scale(self.blank_base, (128, 128)), self.legs_choices[self.legs_index], self.body_choices[self.body_index],
                                                                                                                       self.hair_choices[self.hair_index], self.blank_component, 0)

        blank_sprite.draw()
        return blank_sprite

    def scroll_components(self, component, direction):

        """
        Scrolls in a direction (backwards or forwards) through a list of component images and updates the player's sprite

        Args:
            component (string): The component to change when the player gives input (presses a 'button')
            direction (int): 1 = scrolling forward in list, -1 = scrolling backwards in list.
        """

        # Get the index of the relevant component list
        index = getattr(self, component + "_index")
        list_length = getattr(self, component + "_choices_length")
        # list_length = len(getattr(self, component + "_choices"))

        # Move through list
        if direction == 1:
            index += 1

        elif direction == -1:
            index -= 1

        # If index exceeds list bounds, reset to 0
        if (index >= list_length) or (index <= -list_length):
            print("Index at max! " + str(list_length))
            index = 0
        else:
            print("Index = " + str(index))

        # Update the index of the relevant component
        setattr(self, component + "_index", index)

        # Update component of sprite with image from location in list
        self.player_char.update([component], [getattr(self, component + "_choices")[index]])
        self.update_screen()

    def create_buttons(self):

        """
        Instantiates all the buttons needed for the character creation window.
        The buttons are positioned based on the positioning of the player character.
        Each button is also appended to the list of buttons.
        """

        # Whole section is messy. Perhaps make ScrollButton an object that inherits from Button with initial size, colour, function etc?

        # Create new buttons
        center = (self.size[0] / 2), (self.size[1] / 2)
        right = (self.char_position[0] + 150)
        left = (self.char_position[0] - 100)
        y = self.char_position[1]

        # Hair options
        button_hair = Button((50, 50), (right, y - 100), (0, 255, 0), self.screen, [self.scroll_components], [["hair", 1]], "foo")
        button_hair_back = Button((50, 50), (left, y - 100), (255, 0, 0), self.screen, [self.scroll_components], [["hair", -1]], "foo")

        # Body options
        button_body = Button((50, 50), (right, y), (0, 255, 0), self.screen, [self.scroll_components], [["body", 1]], "foo")
        button_body_back = Button((50, 50), (left, y), (255, 0, 0), self.screen, [self.scroll_components], [["body", -1]], "foo")

        # Leg options
        button_legs = Button((50, 50), (right, y + 100), (0, 255, 0), self.screen, [self.scroll_components], [["legs", 1]], "foo")
        button_legs_back = Button((50, 50), (left, y + 100), (255, 0, 0), self.screen, [self.scroll_components], [["legs", -1]], "foo")

        # Save/finish button
        button_save = Button((100, 50), (center[0] - 50, center[1] + 200), (0, 0, 255), self.screen, [self.finalise_sprite, self.exit], [[], []], "foo")

        # Add new buttons to the list of buttons
        self.buttons.append(button_hair)
        self.buttons.append(button_hair_back)

        self.buttons.append(button_body)
        self.buttons.append(button_body_back)

        self.buttons.append(button_legs)
        self.buttons.append(button_legs_back)

        self.buttons.append(button_save)

    def save_component_index(self, save_file):
        """
        Creates or overwrites the save file, updating the index position when the player saved their sprite.

        Args:
            save_file (string): The name of the file in which to save the index.
        """

        with open(save_file, "w") as f:
            f.write("hair_index " + str(self.hair_index) + "\n")
            f.write("body_index " + str(self.body_index) + "\n")
            f.write("legs_index " + str(self.legs_index) + "\n")
            f.close()

    def read_component_index(self, save_file):
        """
        Reads the save file and sets the appropriate index value to the saved values.

        Args:
            save_file (string): The name of the file to read the index from.
        """

        try:
            with open(save_file) as f:
                for line in f:
                    (key, val) = line.split()
                    setattr(self, key, int(val))

        except IOError:
            print("No index file found.")

    def finalise_sprite(self):
        """Gets the sprite ready for serializing. Background is made transparent and the sprite is returned to its original size."""

        self.player_char.update(["background_colour"], [(0, 0, 0, 0)])
        self.player_char.resize(self.sprite_size)

        Sprite.serialize("player_sprite", self.player_char)

    def exit(self):
        """Closes the character creation window."""

        print("Window Closed")
        self.running = False


def load_creation_window(screen, PLAYER_SCALE):
    """
    Instantiates the character creation class and draws the creation window.

    Args:
        screen (pygame.Display): The display to draw the character creation window on. This will likely be the main game screen.
        PLAYER_SIZE (float): The size of the player. Used to scale the sprites to match the tiles.
    """

    sprite_size = (int(PLAYER_SCALE), int(PLAYER_SCALE))

    images = GetImages("SpriteGeneration/Assets", ".png", (128, 128))
    creation_window = CharacterCreation(screen, images.hair, images.body, images.legs, sprite_size)
    creation_window.draw_win()
    creation_window.save_component_index("char_creation_index.txt")

