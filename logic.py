from random import randrange
import pygame

# Define base variables
bombs = 99;
rows = 16;
columns = 30;

# Create the blank field with (bomb, revealed, neighbours)

field = [];

for row in range(rows):
    current_row = [];
    for cell in range(columns):
        current_row.append([0, 0, 0]);
    field.append(current_row);

# Randomly insert the bombs

counter = 0;

while counter < bombs:
    randRow = randrange(rows);
    randColumn = randrange(columns);
    if field[randRow][randColumn][0] == 1:
        continue;
    else:
        field[randRow][randColumn][0] = 1;
        counter += 1;


''' Check the amount of bombs matches the set parameter
counter = 0;

for row in range(rows):
    for column in range(columns):
        if field[row][column][0] == 1:
            counter += 1;

print("There are {0} bombs in the field.".format(counter))
'''

# Calculate the amount of neighbouring bombs except if it's a bomb
for row in range(rows):
    for column in range(columns):
        if field[row][column][0] == 1:
            continue;
        neighbours = 0;
        for i in range(-1,2):
            for j in range(-1,2):
                if i == 0 and j == 0:
                    continue;
                elif i + row < 0 or i + row >= rows or j + column < 0 or j + column >= columns:
                    continue;
                elif field[i + row][j + column][0] == 1:
                    neighbours += 1;
        field[row][column][2] = neighbours;

# Visulization and Input

# pygame setup
pygame.init();
screen = pygame.display.set_mode((720, 480));
clock = pygame.time.Clock();
running = True;
dt = 0;

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2);

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray");

    # RENDER YOUR GAME HERE
    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt;
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt;
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt;
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt;

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000;

pygame.quit()