population = []
MAX_NUMBER = 8

for i in range(0, MAX_NUMBER + 1):
    population.append(0)

#Read File
try:
    with open('input.txt', 'r') as file:
        line = file.readline()
        temp = line.split(",")
        temp = [int(i) for i in temp]

        for i in range(0, len(temp)):
            fish = temp[i]
            population[fish] += 1
finally:
    file.close()

print(population)

result = 0
total_days = 256

for day in range(1, total_days + 1):
    carry = population[0]
    for i in range(1, len(population)):
        population[i - 1] = population[i]
    population[8] = 0
    population[8] += carry
    population[6] += carry

result = sum(population)

print("Result: ", result)