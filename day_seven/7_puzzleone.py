from numpy import std
from numpy.lib.function_base import average
positions = []

#Read File
try:
    with open('input.txt', 'r') as file:
        line = file.readline()
        positions = line.split(",")
        positions = [int(i) for i in positions]
finally:
    file.close()

best_pos = int(average(positions))
result = 0

print(best_pos)


for position in positions:
    dist = abs(position - best_pos)
    fuel = 0
    for i in range(1, dist + 1):
        fuel += i
    result += fuel

print(result)
