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
    
oxygen = "0"
carbon = "0"

#print(blocks)

valids = blocks.copy()

for pos in range(0, BLOCK_WIDTH):
    one = 0
    zero = 0
    for valid in valids:
        try: 
            if (valid[pos] == "1"):
                    one += 1
            if (valid[pos] == "0"):
                    zero += 1
        except:
            continue
    j = -1
    for valid in valids:
        j += 1
        if (len(valid) > 0):
            if (one > zero):
                if (valid[pos] == "0"):
                    valids[j] = ""
            elif (zero > one):
                if (valid[pos] == "1"):
                    valids[j] = ""
            elif (zero == one):
                if (valid[pos] == "0"):
                    valids[j] = ""
        else:
            valids[j] = ""

oxygen = list(filter(("").__ne__, valids))[0]

valids = blocks.copy()

for pos in range(0, BLOCK_WIDTH):
    valids = list(filter(("").__ne__, valids))
    one = 0
    zero = 0
    for valid in valids:
        try: 
            if (valid[pos] == "1"):
                    one += 1
            if (valid[pos] == "0"):
                    zero += 1
        except:
            continue
    j = -1
    for valid in valids:
        if (len(valids) > 1):
            j += 1
            if (len(valid) > 0):
                if (zero < one):
                    if (valid[pos] == "1"):
                        valids[j] = ""
                elif (one < zero):
                    if (valid[pos] == "0"):
                        valids[j] = ""
                elif (zero == one):
                    if (valid[pos] == "1"):
                        valids[j] = ""
            else:
                valids[j] = ""
    print(pos, valids)


carbon = list(filter(("").__ne__, valids))[0]


o = int(oxygen, 2)
c = int(carbon, 2)

print(o * c)
    