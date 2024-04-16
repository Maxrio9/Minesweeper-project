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
screen = pygame.display.set_mode((1080, 720));
clock = pygame.time.Clock();
running = True;
dt = 0;
screen_width = screen.get_width();
screen_height = screen.get_height();

grid_rows = rows;
grid_columns = columns;
sprite_size = 17;
display_scale = 2;

# sprites
blank_img = pygame.image.load("sprites/blank.png")
blank_img = pygame.transform.scale(blank_img, (sprite_size * display_scale, sprite_size * display_scale))
rev0_img = pygame.image.load("sprites/rev0.png")
rev0_img = pygame.transform.scale(rev0_img, (sprite_size * display_scale, sprite_size * display_scale))

class Blank(pygame.sprite.Sprite):
    def __init__(self, column, row):
        super().__init__()
        self.image = blank_img
        self.rect = self.image.get_rect()
        self.rect.y = row
        self.rect.x = column

sprites_group = pygame.sprite.Group()
for row in range(rows):
    for col in range(columns):
        x = col * sprite_size * display_scale
        y = row * sprite_size * display_scale
        blank = Blank(x, y)
        sprites_group.add(blank)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((65, 65, 65));

    # RENDER YOUR GAME HERE
    sprites_group.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60);

pygame.quit()