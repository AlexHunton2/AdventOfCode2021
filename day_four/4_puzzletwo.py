numbers = []
boards = []

BOARD_WIDTH = 5

def getCorrectNumbers(nums: list, current_number):
    global numbers

    correct = 0
    for num in nums:
        for i in range(0, current_number + 1):
            if (num == numbers[i]):
                correct += 1
                break
    #if (correct == 5):
        #print("Winning Row: ", nums)
    return correct

def isMark(v, current_number):
    for i in range(0, current_number + 1):
        x = numbers[i]
        if (v == x):
            return True
    return False

def getResult(board: list, current_number):
    global numbers
    non_marked = []
    correct_numbers = []
    for row in range(0, BOARD_WIDTH):
        for col in range(0, BOARD_WIDTH):
            v = board[row][col]
            if not isMark(v, current_number):
                non_marked.append(v)
            else:
                correct_numbers.append(v)
    
    print("Current: ", current_number)
    print("Last Number: ", numbers[current_number])
    print("Non_marked: ", non_marked)
    print("Correct Numbers: ", correct_numbers)

    return sum(non_marked) * numbers[current_number]

#Read File
try:
    with open('input.txt', 'r') as file:
        #collect numbers
        line = file.readline()
        numbers = line.split(',')
        numbers = [int(i) for i in numbers]
        file.readline()

        #collect boards
        i = -1
        line = " "
        temp = []
        while line != '':
            i += 1
            line = file.readline()
            if (i == 5):
                boards.append(temp)
                temp = []
                i = -1
                continue
            row = line.split()
            row = [int(j) for j in row]
            temp.append(row)
finally:
    file.close()

current_number = 0

#Look for winner
while True:
    #Check indidivual board for winner
    for board in boards:

        #row check
        for row in board:
            correct_count = getCorrectNumbers(row, current_number)
            if correct_count == BOARD_WIDTH:
                try:
                    boards.remove(board)
                except:
                    continue
                
        #column check
        temp = []
        for col in range(0, BOARD_WIDTH):
            for row in range(0, BOARD_WIDTH):
                temp.append(board[row][col])
            correct_count = getCorrectNumbers(temp, current_number)
            if correct_count == BOARD_WIDTH:
                try:
                    boards.remove(board)
                except:
                    continue
            else:
                temp = []
        
    #no winner yet? expand possible numbers
    if (current_number > len(numbers)):
        print("Failure :(")
        break

    if (len(boards) < 2):
        print(boards[0])
        print("Result: ", getResult(boards[0], current_number))
        raise Exception

    current_number += 1


        
