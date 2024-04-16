from random import randrange

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

# Visulization

# Input