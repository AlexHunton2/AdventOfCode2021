#WARNING: BAD CODE
heightmap = []

MAX_HEIGHT = 9

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

lowest_points = {}

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
                lowest_points[(row, col)] = spot

basins = []

def constructBasinPart(i_row = int, i_col = int):
    temp = {}
    temp[(i_row, i_col)] = heightmap[i_row][i_col]

    for i in range(0, 4):
        try:
            if (i == 0):
                if (heightmap[i_row+1][i_col] != MAX_HEIGHT):
                   temp[(i_row+1, i_col)] = heightmap[i_row+1][i_col]
            if (i == 1):
                if (heightmap[i_row-1][i_col] != MAX_HEIGHT):
                    temp[(i_row-1, i_col)] = heightmap[i_row-1][i_col] 
            if (i == 2):
                if (heightmap[i_row][i_col+1] != MAX_HEIGHT):
                    temp[(i_row, i_col+1)] = heightmap[i_row][i_col+1]
            if (i == 3):
                if (heightmap[i_row][i_col-1] != MAX_HEIGHT):
                    temp[(i_row, i_col-1)] = heightmap[i_row][i_col-1]
        except:
            continue
    
    return temp

for key,height in lowest_points.items():
    prev_parts = {(key[0], key[1]) : height}
    parts = constructBasinPart(key[0], key[1])
    
    while True:
        temp = parts
        for key,height in parts.items():
            if (key not in prev_parts):
                parts = parts | constructBasinPart(key[0], key[1])
        prev_parts = temp

        if (len(prev_parts) == len(parts)):
            break
    
    temp = parts.copy()
    for key,height in parts.items():
        if (key[0] < 0 or key[1] < 0):
            temp.pop(key)
    
    basins.append(temp)

result = 1
lengths = []
basin_lengths = [len(j) for j in basins]
copy_basin_lengths = basin_lengths.copy()
for i in range(0, 3):
    result *= max(copy_basin_lengths)
    lengths.append(max(copy_basin_lengths))
    copy_basin_lengths.remove(max(copy_basin_lengths))

print(result)