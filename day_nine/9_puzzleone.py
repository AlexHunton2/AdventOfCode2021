heightmap = []

#Read File
try:
    with open('testinput.txt', 'r') as file:
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
        temp = []
        # if top-left corner
        if (row == 0 and col == 0):
            continue
        # if top-right corner
        elif (row == 0 and col == (MAX_COL - 1)):
            continue
        # if bottom-left corner
        elif (row == (MAX_ROW - 1) and col == 0):
            continue
        # if bottom-right corner
        elif (row == (MAX_ROW - 1) and col == (MAX_COL - 1)):
            continue
        # if on top row
        elif (row == 0):
            continue
        # if on bottom row
        elif (row == (MAX_ROW - 1)):
            continue
        # if none of above:
        else:
            temp = [heightmap[row-1][col], heightmap[row+1][col], heightmap[row][col-1], heightmap[row][col+1]]
        temp.append(spot)

        if min(temp) == spot:
            lowest_points.append(spot)





