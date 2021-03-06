heightmap = []

#Read File
try:
    with open('input.txt', 'r') as file:
        #collect numbers
        line = file.readline()
        while line != '':
            temp = []
            for i in range(0, len(line)):
                if (line[i].strip() != ''):
                    spot = int(line[i].strip())
                    temp.append(spot)
            heightmap.append(temp)
            temp = []
            line = file.readline()          
finally:
    file.close()

MAX_ROW = len(heightmap)
MAX_COL = len(heightmap[0])

lowest_points = []

for row in range(0, MAX_ROW):
    for col in range(0, MAX_COL):
        spot = heightmap[row][col]
        temp = [] # list of valid locations to check
        # if top-left corner
        if (row == 0 and col == 0):
            temp = [heightmap[row+1][col], heightmap[row][col+1]]
        # if top-right corner
        elif (row == 0 and col == (MAX_COL - 1)):
            temp = [heightmap[row+1][col], heightmap[row][col-1]]
        # if bottom-left corner
        elif (row == (MAX_ROW - 1) and col == 0):
            temp = [heightmap[row-1][col], heightmap[row][col+1]]
        # if bottom-right corner
        elif (row == (MAX_ROW - 1) and col == (MAX_COL - 1)):
            temp = [heightmap[row-1][col], heightmap[row][col-1]]
        # if on top row
        elif (row == 0):
            temp = [heightmap[row+1][col], heightmap[row][col-1], heightmap[row][col+1]]
        # if on bottom row
        elif (row == (MAX_ROW - 1)):
            temp = [heightmap[row-1][col], heightmap[row][col-1], heightmap[row][col+1]]
        # if left most col
        elif (col == 0):
            temp = [heightmap[row-1][col], heightmap[row+1][col], heightmap[row][col+1]]
        # if right most col
        elif (col == (MAX_COL - 1)):
            temp = [heightmap[row-1][col], heightmap[row+1][col], heightmap[row][col-1]]
        # if none of above:
        else:
            temp = [heightmap[row-1][col], heightmap[row+1][col], heightmap[row][col-1], heightmap[row][col+1]]

        if (spot not in temp):
            temp.append(spot)
            if min(temp) == spot:
                lowest_points.append(spot)

# calculate risk_level
risk_levels = [i + 1 for i in lowest_points]
print(sum(risk_levels))






