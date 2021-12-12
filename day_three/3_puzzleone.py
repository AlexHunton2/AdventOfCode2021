blocks = []

BLOCK_WIDTH = 12

#Read File
try:
    with open('input.txt', 'r') as file:
        line = file.readline()
        blocks.append(line)
        while line != '':
            line = file.readline()
            blocks.append(line)
finally:
    file.close()
    
gamma = ""
epsilon = ""

print(blocks)

for i in range(0, BLOCK_WIDTH):
    one = 0
    zero = 0
    for block in blocks:
        block.strip()
        try: 
            if (block[i] == "1"):
                    one += 1
            if (block[i] == "0"):
                    zero += 1
        except:
            print("I: ", i)
            print("Block: ", block)
    if (one > zero):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(gamma)

g = int(gamma, 2)
e = int(epsilon, 2)

print(g * e)
    