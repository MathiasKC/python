from time import sleep
import os
cols = 20
rows = 20
grid_x = []
time = 0.1
for x in range(cols):
    grid_y = []
    for y in range(rows):
        grid_y.append(0)
    grid_x.append(grid_y)



for x in range(cols):
    print(grid_x[x])



# for x in range(cols):
#     for y in range(rows):
#         if grid_x[x][y] == 1:


while True:
    os.system('cls')
    grid_x[0][5] = 1
    for x in range(cols):
        print(grid_x[x])
    sleep(time)
####DRAW LOOP######

####DRAW LOOP######
    for x in range(cols):
        for y in range(rows):
            if x < cols - 1:
                #CHECK DOWN
                if grid_x[x][y] == 1 and grid_x[x+1][y] == 0:
                    grid_x[x][y] = 0
                    grid_x[x+1][y] = 1
                    os.system('cls')
                    for x in range(cols):
                        print(grid_x[x])
                    sleep(time)
                    #CHECK LEFT
                if x != cols - 1 and y != rows - 1:
                    if grid_x[x][y] == 1 and grid_x[x+1][y] == 1 and grid_x[x + 1][y - 1] == 0:
                        grid_x[x][y] = 0
                        grid_x[x + 1][y - 1] = 1
                        os.system('cls')
                        for x in range(cols):
                            print(grid_x[x])
                        sleep(time)
                if x != cols - 1 and y != rows - 1:
                    #CHECK RIGHT
                    if grid_x[x][y] == 1 and grid_x[x+1][y] == 1 and grid_x[x + 1][y - 1] == 1 and grid_x[x + 1][y + 1] == 0:
                        grid_x[x][y] = 0
                        grid_x[x + 1][y + 1 ] = 1
                        os.system('cls')
                        for x in range(cols):
                            print(grid_x[x])
                        sleep(time)
