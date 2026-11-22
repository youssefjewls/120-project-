# ------------------------------------------
# Atom Catcher - CHE120 Final Project
# University of Waterloo, Ontario
#
# Group members:
#   - Emerson Eliuk
#   - Kiera Yoon
#   - Umar Rawther
#   - Youssef Elgendy
#
# main.py | starts the game and runs the game loop.
# Written by: Umar Rawther (UR)
# ------------------------------------------

import pygame
import random

def main():

    """ () -> NoneType

    Open the game window and run the game loop until the player closes it.
    """
    
    # Pygame initialization
    pygame.init() # Calls the pygame library to initialize all imported pygame modules
    pygame.display.set_caption("Atom Catcher") # Sets the title of the window to "Atom Catcher"
    screen = pygame.display.set_mode((800, 600), pygame.SCALED | pygame.RESIZABLE) # SCALED keeps the game 800x600 inside but stretches it to fit the window; RESIZABLE adds the maximize button
    clock = pygame.time.Clock() # Variable to help track time and control the frame rate of the game
    running = True # Sets the running variable to True, which will be used to control the main game loop

    # Beaker properties
    beaker_width = 75 # Sets the width of the beaker to 75 pixels
    beaker_height = 75 # Sets the height of the beaker to 75 pixels
    beaker_speed = 420 # Sets the speed of the beaker to 420 pixels per second
    beaker_x = 400 - beaker_width/2 # Sets the initial x position of the beaker to the center of the screen
    beaker_y = 550 - beaker_height # Sets the initial y position of the beaker to the bottom of the screen

    # Atom properties
    atoms = []           # each atom is a dict: {"symbol": "H", "x": 300, "y": -20}
    atom_radius = 20
    atom_speed = 120     # pixels per second
    spawn_timer = 1.0    # seconds until the next atom appears
    font = pygame.font.SysFont(None, 28)  # made once here, since making fonts every frame is slow
    
    while running: 
        # Main game Loop. Checks for user input, closes the window if user decides to exit, gives user options for resizing window, and draws the beaker on the screen.
        dt = clock.tick(60)/1000.0 # Limits FPS to 60 and calculates the time since the last frame (Δt) in seconds
        for event in pygame.event.get(): # Gets a list of all events that have occurred since the last frame

            if event.type == pygame.QUIT: # Checks if the user has clicked the close button on the window
                running = False # If so, sets running to False, which will exit the main game loop

            if event.type == pygame.KEYDOWN and event.key == pygame.K_F11: # F11 switches between windowed and full screen
                pygame.display.toggle_fullscreen()

        # Left Key Movement
        keys = pygame.key.get_pressed() # Gets a list of all keys that are currently being pressed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]: # Checks if the left arrow key or the 'A' key is being pressed
            beaker_x -= beaker_speed * dt # Moves the beaker left by the speed multiplied by Δt

        # Right Key Movement
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: # Checks if the right arrow key is being pressed or the 'D' key is being pressed
            beaker_x += beaker_speed * dt # Moves the beaker right by the speed multiplied by Δt

        # Keep the beaker inside the window
        if beaker_x < 0: # Stops the beaker going past the left edge
            beaker_x = 0
        if beaker_x > 800 - beaker_width: # The right side of the beaker is at beaker_x + beaker_width, so beaker_x can't go past 800 - beaker_width
            beaker_x = 800 - beaker_width

        # Spawn a new atom every second
        spawn_timer -= dt
        if spawn_timer <= 0:
            new_atom = {"symbol": random.choice(["H", "O", "C", "N"]),
                        "x": random.randint(atom_radius, 800 - atom_radius),
                        "y": -atom_radius}
            atoms.append(new_atom)
            spawn_timer = 1.0

        # Move every atom down
        for atom in atoms:
            atom["y"] += atom_speed * dt

        # Remove atoms that fell off the bottom
        for atom in list(atoms):    # loop over a copy, since we remove from the real list
            if atom["y"] - atom_radius > 600:
                atoms.remove(atom)

        # Draws the game frame and the beaker
        screen.fill((24,28,38)) # Fills the screen with a dark blue color (RGB: 24, 28, 38)

        for atom in atoms:
            pygame.draw.circle(screen, (120, 120, 130), (int(atom["x"]), int(atom["y"])), atom_radius)
            label = font.render(atom["symbol"], True, (235, 235, 235))
            screen.blit(label, label.get_rect(center=(int(atom["x"]), int(atom["y"]))))

        pygame.draw.rect(screen, (255, 255, 255), (beaker_x, beaker_y, beaker_width, beaker_height)) # Draws a white rectangle representing the beaker at the specified position and size
        pygame.display.flip() # Shows the finished frame on the window. Everything is drawn to a hidden screen first, so the player never sees a half-drawn frame.
        

    pygame.quit()

if __name__ == "__main__":
    main() # Calls the main function to start the game