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
prev_depth = depths[0]
for i in range(1, len(depths)):
    depth = depths[i]
    if (depth > prev_depth):
        counter = counter + 1    
    prev_depth = depth

print(len(depths))
print(counter)