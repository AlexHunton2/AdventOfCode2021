from numpy import median
positions = []

#Read File
try:
    with open('input.txt', 'r') as file:
        line = file.readline()
        positions = line.split(",")
        positions = [int(i) for i in positions]
finally:
    file.close()

media_n = int(median(positions))
result = 0

for position in positions:
    fuel = abs(position - media_n)
    result += fuel

print(result)
