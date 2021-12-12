MAX_WIDTH = 1000

lines = []

#Read File - Populate with lists of [[x1, y1], [x2, y2]]
try:
    with open('input.txt', 'r') as file:
        line = " "
        temp = []
        while line != '':
            line = file.readline()
            a = line.split(" -> ")
            if (len(a) > 1):
                for i in range(0, len(a)):
                    b = a[i].split(',')
                    b = [int(i) for i in b]
                    temp.append(b)
                lines.append(temp)
                temp = []
finally:
    file.close()

model = []

#build empty graph of all points
for x in range(0, MAX_WIDTH):
    temp = []
    for y in range(0, MAX_WIDTH):
        temp.append(0)
    model.append(temp)

for line in lines:
    #if vertical
    if (line[0][0] == line[1][0]):
        mi = min(line[0][1], line[1][1])
        ma = max(line[0][1], line[1][1])
        for y in range(mi, (ma + 1)):
            model[line[0][0]][y] += 1
    #if horizontal
    elif (line[0][1] == line[1][1]):
        mi = min(line[0][0], line[1][0])
        ma = max(line[0][0], line[1][0])
        for x in range(mi, (ma + 1)):
            model[x][line[0][1]] += 1


counter = 0
for x in range(0, MAX_WIDTH):
    for y in range(0, MAX_WIDTH):
        if (model[x][y] > 1):
                counter += 1

print("Result: ", counter)
