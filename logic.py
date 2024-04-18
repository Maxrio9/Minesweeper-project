from random import randrange
import math
import pygame

'''
TODO LIST
IMPROVEMENTS and EXPANSION

Lose Mechanic
Win Mechanic
Reset Mechanic
Flag Mechanic
Bombs left to Flag Mechanic
Field Click when Flags in proximity Mechanic

Variable Difficultys before Start-Up

Add calculation of risk for each field
Add Hint mechanic
Add AI agent to solve

'''

# Define base variables
bombs = 99;
rows = 16;
columns = 30;

# Display variables
sprite_size = 17;
display_scale = 2;
top_border = 40;

# Create the blank field with (bomb, revealed, neighbours, flag)

field = [];

for column in range(columns):
    current_column = [];
    for cell in range(rows):
        current_column.append([0, 0, 0, 0]);
    field.append(current_column);

# Randomly insert the bombs

counter = 0;

while counter < bombs:
    randRow = randrange(rows);
    randColumn = randrange(columns);
    if field[randColumn][randRow][0] == 1:
        continue;
    else:
        field[randColumn][randRow][0] = 1;
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
for column in range(columns):
    for row in range(rows):
        if field[column][row][0] == 1:
            continue;
        neighbours = 0;
        for i in range(-1,2):
            for j in range(-1,2):
                if i == 0 and j == 0:
                    continue;
                elif i + column < 0 or i + column >= columns or j + row < 0 or j + row >= rows:
                    continue;
                elif field[i + column][j + row][0] == 1:
                    neighbours += 1;
        field[column][row][2] = neighbours;

# Calculate cell in field from mouse position
def pos_field(pixel):
    x = pixel[0]
    y = pixel[1]
    column = math.floor(x / (sprite_size * display_scale))
    row = math.floor((y - top_border) / (sprite_size * display_scale))
    return column, row

# Update the values of the field after click

def update(pixel):
    print(pixel)
    column, row = pos_field(pixel)
    print(column, row)
    field[column][row][1] = 1;
    return (column, row)
# Recursively reveal all the cells around a blank cell and any blank cell in proximity.
# Currently difficult because we can only know the sprite by interaction with the mouse.

def recursive_reveal(column, row):
    for i in range(-1,2):
            for j in range(-1,2):
                if i == 0 and j == 0:
                    continue;
                elif i + column < 0 or i + column >= columns or j + row < 0 or j + row >= rows:
                    continue;
                elif field[i + column][j + row][1] == 1:
                    continue;
                elif field[i + column][j + row][1] == 0 and field[i + column][j + row][2] != 0:
                    field[i + column][j + row][1] = 1
                    update_sprite((column + i, row + j))
                elif field[i + column][j + row][1] == 0 and field[i + column][j + row][2] == 0:
                    field[i + column][j + row][1] = 1
                    update_sprite((column + i, row + j))
                    recursive_reveal(i + column, j + row)
                    
                

# Return type of cell

def return_type(grid):
    if field[grid[0]][grid[1]][0] == 1:
        return "bomb"
    elif field[grid[0]][grid[1]][2] == 0:
        return "rev0"
    elif field[grid[0]][grid[1]][2] == 1:
        return "rev1"
    elif field[grid[0]][grid[1]][2] == 2:
        return "rev2"
    elif field[grid[0]][grid[1]][2] == 3:
        return "rev3"
    elif field[grid[0]][grid[1]][2] == 4:
        return "rev4"
    elif field[grid[0]][grid[1]][2] == 5:
        return "rev5"
    elif field[grid[0]][grid[1]][2] == 6:
        return "rev6"
    elif field[grid[0]][grid[1]][2] == 7:
        return "rev7"
    elif field[grid[0]][grid[1]][2] == 8:
        return "rev8"
    elif field[grid[0]][grid[1]][3] == 1:
        return "flag"
    SystemError("Unexpected Field");

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
    def __init__(self, pixel_x, pixel_y, column, row):
        super().__init__()
        self.image = blank_img
        self.rect = self.image.get_rect()
        self.rect.x = pixel_x
        self.rect.y = pixel_y
        self.grid_x = column
        self.grid_y = row

class Rev0(pygame.sprite.Sprite):
    def __init__(self, pixel_x, pixel_y, column, row):
        super().__init__()
        self.image = rev0_img
        self.rect = self.image.get_rect()
        self.rect.x = pixel_x
        self.rect.y = pixel_y
        self.grid_x = column
        self.grid_y = row

class Rev1(pygame.sprite.Sprite):
    def __init__(self, pixel_x, pixel_y, column, row):
        super().__init__()
        self.image = rev1_img
        self.rect = self.image.get_rect()
        self.rect.x = pixel_x
        self.rect.y = pixel_y
        self.grid_x = column
        self.grid_y = row

class Rev2(pygame.sprite.Sprite):
    def __init__(self, pixel_x, pixel_y, column, row):
        super().__init__()
        self.image = rev2_img
        self.rect = self.image.get_rect()
        self.rect.x = pixel_x
        self.rect.y = pixel_y
        self.grid_x = column
        self.grid_y = row

class Rev3(pygame.sprite.Sprite):
    def __init__(self, pixel_x, pixel_y, column, row):
        super().__init__()
        self.image = rev3_img
        self.rect = self.image.get_rect()
        self.rect.x = pixel_x
        self.rect.y = pixel_y
        self.grid_x = column
        self.grid_y = row

class Rev4(pygame.sprite.Sprite):
    def __init__(self, pixel_x, pixel_y, column, row):
        super().__init__()
        self.image = rev4_img
        self.rect = self.image.get_rect()
        self.rect.x = pixel_x
        self.rect.y = pixel_y
        self.grid_x = column
        self.grid_y = row

class Rev5(pygame.sprite.Sprite):
    def __init__(self, pixel_x, pixel_y, column, row):
        super().__init__()
        self.image = rev5_img
        self.rect = self.image.get_rect()
        self.rect.x = pixel_x
        self.rect.y = pixel_y
        self.grid_x = column
        self.grid_y = row

class Rev6(pygame.sprite.Sprite):
    def __init__(self, pixel_x, pixel_y, column, row):
        super().__init__()
        self.image = rev6_img
        self.rect = self.image.get_rect()
        self.rect.x = pixel_x
        self.rect.y = pixel_y
        self.grid_x = column
        self.grid_y = row

class Rev7(pygame.sprite.Sprite):
    def __init__(self, pixel_x, pixel_y, column, row):
        super().__init__()
        self.image = rev7_img
        self.rect = self.image.get_rect()
        self.rect.x = pixel_x
        self.rect.y = pixel_y
        self.grid_x = column
        self.grid_y = row

class Rev8(pygame.sprite.Sprite):
    def __init__(self, pixel_x, pixel_y, column, row):
        super().__init__()
        self.image = rev8_img
        self.rect = self.image.get_rect()
        self.rect.x = pixel_x
        self.rect.y = pixel_y
        self.grid_x = column
        self.grid_y = row

class Bomb(pygame.sprite.Sprite):
    def __init__(self, pixel_x, pixel_y, column, row):
        super().__init__()
        self.image = bomb_img
        self.rect = self.image.get_rect()
        self.rect.x = pixel_x
        self.rect.y = pixel_y
        self.grid_x = column
        self.grid_y = row

class Bomb_exp(pygame.sprite.Sprite):
    def __init__(self, pixel_x, pixel_y, column, row):
        super().__init__()
        self.image = bomb_exp_img
        self.rect = self.image.get_rect()
        self.rect.x = pixel_x
        self.rect.y = pixel_y
        self.grid_x = column
        self.grid_y = row

sprites_group = pygame.sprite.Group()
for row in range(rows):
    for col in range(columns):
        x = col * sprite_size * display_scale
        y = row * sprite_size * display_scale + top_border
        blank = Blank(x, y, col, row)
        sprites_group.add(blank)

def update_sprite(grid):
    # Delete existing sprite
    for sprite in sprites_group:
        if sprite.grid_x == grid[0] and sprite.grid_y == grid[1]:
            sprites_group.remove(sprite)
    # Create and add new sprite
    type = return_type(grid)
    if type == "bomb":
        new_sprite = Bomb_exp(grid[0] * sprite_size * display_scale, grid[1] * sprite_size * display_scale + top_border, grid[0], grid[1])
        sprites_group.add(new_sprite)
    elif type == "rev0":
        new_sprite = Rev0(grid[0] * sprite_size * display_scale, grid[1] * sprite_size * display_scale + top_border, grid[0], grid[1])
        sprites_group.add(new_sprite)
    elif type == "rev1":
        new_sprite = Rev1(grid[0] * sprite_size * display_scale, grid[1] * sprite_size * display_scale + top_border, grid[0], grid[1])
        sprites_group.add(new_sprite)
    elif type == "rev2":
        new_sprite = Rev2(grid[0] * sprite_size * display_scale, grid[1] * sprite_size * display_scale + top_border, grid[0], grid[1])
        sprites_group.add(new_sprite)
    elif type == "rev3":
        new_sprite = Rev3(grid[0] * sprite_size * display_scale, grid[1] * sprite_size * display_scale + top_border, grid[0], grid[1])
        sprites_group.add(new_sprite)
    elif type == "rev4":
        new_sprite = Rev4(grid[0] * sprite_size * display_scale, grid[1] * sprite_size * display_scale + top_border, grid[0], grid[1])
        sprites_group.add(new_sprite)
    elif type == "rev5":
        new_sprite = Rev5(grid[0] * sprite_size * display_scale, grid[1] * sprite_size * display_scale + top_border, grid[0], grid[1])
        sprites_group.add(new_sprite)
    elif type == "rev6":
        new_sprite = Rev6(grid[0] * sprite_size * display_scale, grid[1] * sprite_size * display_scale + top_border, grid[0], grid[1])
        sprites_group.add(new_sprite)
    elif type == "rev7":
        new_sprite = Rev7(grid[0] * sprite_size * display_scale, grid[1] * sprite_size * display_scale + top_border, grid[0], grid[1])
        sprites_group.add(new_sprite)
    elif type == "rev8":
        new_sprite = Rev8(grid[0] * sprite_size * display_scale, grid[1] * sprite_size * display_scale + top_border, grid[0], grid[1])
        sprites_group.add(new_sprite)
    return type


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;
        elif event.type == pygame.MOUSEBUTTONUP:
            for sprite in sprites_group:
                if sprite.rect.collidepoint(event.pos):
                    (column, row) = update(event.pos)
                    type = update_sprite((column, row))
                    if type == "rev0":
                        recursive_reveal(column, row)
                    print(sprite.grid_x, sprite.grid_y)

                    

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((65, 65, 65));

    # RENDER YOUR GAME HERE
    sprites_group.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60);

pygame.quit()