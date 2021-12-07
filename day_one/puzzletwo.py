depths = []

try:
    with open('depthmeasures.txt', 'r') as depth_file:
        line = depth_file.readline()
        depths.append(int(line))
        while line != '':
            line = depth_file.readline()
            try:
                depths.append(int(line))
            except:
                continue
finally:
    depth_file.close()

counter = 0
blocks = []
j = 0
while (j < len(depths) - 2):
    sum = depths[j] + depths[j+1] + depths[j+2]
    blocks.append(sum)
    j = j + 1

prev_block = blocks[0]
for i in range(1, len(blocks)):
    block = blocks[i]
    if (block > prev_block):
        counter = counter + 1    
    prev_block = block

print(counter)