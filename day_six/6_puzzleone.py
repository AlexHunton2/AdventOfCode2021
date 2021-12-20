population = []

#Read File
try:
    with open('testcase.txt', 'r') as file:
        line = file.readline()
        population = line.split(",")
        population = [int(i) for i in population]
finally:
    file.close()


def getFishTotalAtDay(end_day):
    global population

    temp = population.copy()
    for day in range(1, end_day + 1):
        for i in range(0, len(temp)):
            fish = temp[i]
            if (fish == 0):
                temp[i] = 6
                temp.append(8)
            else:
                temp[i] = fish - 1
    return len(temp)

print("Result: ", getFishTotalAtDay(80))




