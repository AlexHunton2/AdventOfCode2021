#Globals
instructions = []

aim = 0
horizontal = 0
depth = 0

#Read File
try:
    with open('input.txt', 'r') as depth_file:
        line = depth_file.readline()
        instructions.append(line)
        while line != '':
            line = depth_file.readline()
            instructions.append(line)
finally:
    depth_file.close()

#Update globals
def move(instruction, num):
    global horizontal, depth, aim
    if (instruction == "forward"):
        horizontal += num
        depth += (aim * num)
    elif (instruction == "down"):
        aim += num
    elif (instruction == "up"):
        aim -= num

#Go through each instruction and update globals
for i in instructions:
    a = i.split()
    if (len(a) > 0):
        move(a[0], int(a[1]))

#Print Results
print("Horizontal: ", horizontal)
print("Depth: ", depth)