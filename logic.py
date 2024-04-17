from random import randrange
import math
import pygame

# Define base variables
bombs = 99;
rows = 16;
columns = 30;

# Display variables
sprite_size = 17;
display_scale = 2;
top_border = 40;

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

# Calculate cell in field from mouse position
def pos_field(pos):
    x = pos[0]
    y = pos[1]
    column = math.floor(x / (sprite_size * display_scale))
    row = math.floor((y - top_border) / (sprite_size * display_scale))
    return column, row

# Update the values of the field after click

def update(pos):
    print(pos)
    column, row = pos_field(pos)
    print(column, row)
    field[row][column][1] = 1;
    

# Visulization and Input


# pygame setup
pygame.init();

screen_width = sprite_size * display_scale * columns;
screen_height = sprite_size * display_scale * rows + top_border;

screen = pygame.display.set_mode((screen_width, screen_height));
clock = pygame.time.Clock();
running = True;

# sprites
blank_img = pygame.image.load("sprites/blank.png")
blank_img = pygame.transform.scale(blank_img, (sprite_size * display_scale, sprite_size * display_scale))
rev0_img = pygame.image.load("sprites/rev0.png")
rev0_img = pygame.transform.scale(rev0_img, (sprite_size * display_scale, sprite_size * display_scale))
rev1_img = pygame.image.load("sprites/rev1.png")
rev1_img = pygame.transform.scale(rev1_img, (sprite_size * display_scale, sprite_size * display_scale))
rev2_img = pygame.image.load("sprites/rev2.png")
rev2_img = pygame.transform.scale(rev2_img, (sprite_size * display_scale, sprite_size * display_scale))
rev3_img = pygame.image.load("sprites/rev3.png")
rev3_img = pygame.transform.scale(rev3_img, (sprite_size * display_scale, sprite_size * display_scale))
rev4_img = pygame.image.load("sprites/rev4.png")
rev4_img = pygame.transform.scale(rev4_img, (sprite_size * display_scale, sprite_size * display_scale))
rev5_img = pygame.image.load("sprites/rev5.png")
rev5_img = pygame.transform.scale(rev5_img, (sprite_size * display_scale, sprite_size * display_scale))
rev6_img = pygame.image.load("sprites/rev6.png")
rev6_img = pygame.transform.scale(rev6_img, (sprite_size * display_scale, sprite_size * display_scale))
rev7_img = pygame.image.load("sprites/rev7.png")
rev7_img = pygame.transform.scale(rev7_img, (sprite_size * display_scale, sprite_size * display_scale))
rev8_img = pygame.image.load("sprites/rev8.png")
rev8_img = pygame.transform.scale(rev8_img, (sprite_size * display_scale, sprite_size * display_scale))
bomb_img = pygame.image.load("sprites/bomb.png")
bomb_img = pygame.transform.scale(bomb_img, (sprite_size * display_scale, sprite_size * display_scale))
bomb_exp_img = pygame.image.load("sprites/bomb_exp.png")
bomb_exp_img = pygame.transform.scale(bomb_exp_img, (sprite_size * display_scale, sprite_size * display_scale))


class Blank(pygame.sprite.Sprite):
    def __init__(self, column, row):
        super().__init__()
        self.image = blank_img
        self.rect = self.image.get_rect()
        self.rect.y = row
        self.rect.x = column

class Rev0(pygame.sprite.Sprite):
    def __init__(self, column, row):
        super().__init__()
        self.image = rev0_img
        self.rect = self.image.get_rect()
        self.rect.y = row
        self.rect.x = column

class Rev1(pygame.sprite.Sprite):
    def __init__(self, column, row):
        super().__init__()
        self.image = rev1_img
        self.rect = self.image.get_rect()
        self.rect.y = row
        self.rect.x = column

class Rev2(pygame.sprite.Sprite):
    def __init__(self, column, row):
        super().__init__()
        self.image = rev2_img
        self.rect = self.image.get_rect()
        self.rect.y = row
        self.rect.x = column

class Rev3(pygame.sprite.Sprite):
    def __init__(self, column, row):
        super().__init__()
        self.image = rev3_img
        self.rect = self.image.get_rect()
        self.rect.y = row
        self.rect.x = column

class Rev4(pygame.sprite.Sprite):
    def __init__(self, column, row):
        super().__init__()
        self.image = rev4_img
        self.rect = self.image.get_rect()
        self.rect.y = row
        self.rect.x = column

class Rev5(pygame.sprite.Sprite):
    def __init__(self, column, row):
        super().__init__()
        self.image = rev5_img
        self.rect = self.image.get_rect()
        self.rect.y = row
        self.rect.x = column

class Rev6(pygame.sprite.Sprite):
    def __init__(self, column, row):
        super().__init__()
        self.image = rev6_img
        self.rect = self.image.get_rect()
        self.rect.y = row
        self.rect.x = column

class Rev7(pygame.sprite.Sprite):
    def __init__(self, column, row):
        super().__init__()
        self.image = rev7_img
        self.rect = self.image.get_rect()
        self.rect.y = row
        self.rect.x = column

class Rev8(pygame.sprite.Sprite):
    def __init__(self, column, row):
        super().__init__()
        self.image = rev8_img
        self.rect = self.image.get_rect()
        self.rect.y = row
        self.rect.x = column

class Bomb(pygame.sprite.Sprite):
    def __init__(self, column, row):
        super().__init__()
        self.image = bomb_img
        self.rect = self.image.get_rect()
        self.rect.y = row
        self.rect.x = column

class Bomb_exp(pygame.sprite.Sprite):
    def __init__(self, column, row):
        super().__init__()
        self.image = bomb_exp_img
        self.rect = self.image.get_rect()
        self.rect.y = row
        self.rect.x = column

sprites_group = pygame.sprite.Group()
for row in range(rows):
    for col in range(columns):
        x = col * sprite_size * display_scale
        y = row * sprite_size * display_scale + top_border
        blank = Blank(x, y)
        sprites_group.add(blank)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;
        elif event.type == pygame.MOUSEBUTTONUP:
            for sprite in sprites_group:
                if sprite.rect.collidepoint(event.pos):
                    update(event.pos)
                    

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((65, 65, 65));

    # RENDER YOUR GAME HERE
    sprites_group.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60);

pygame.quit()