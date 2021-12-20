from typing import final


DIGIT_SIGNALS = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
TYPICAL_ORDER = "abcdefg"

MAX_LENGTH_OF_DIGIT = 7

# GENERATE KEY IN ORDER OF DO
# a = whatever letter isn't in 1, but is in 7
# c & d & e 
#   = compare lengths of 6 against 8, get list of 3 digits that could be c d e,
# c = compare candidates with 7, whatever matches is c,
# f = whatever doesn't is f
# d = get candidates for b and d from 4, match d to the 3 candidates
# e = the remaining letter that isn't c or e
# b = use 4, whatever c, f, d isn't
# g = whatever is remaining from 8

class Signal:
    signal_patterns = []
    outputs = []

    def __init__(self, patterns, outputs):
        self.signal_patterns = self.__sortSignalPatterns(patterns)
        self.outputs = outputs

    def __str__(self):
        return "Signal Patterns: {0} \nOutputs: {1}".format(self.signal_patterns, self.outputs)

    # Sorts the signal patterns by their lengths
    def __sortSignalPatterns(self, patterns):
        temp = []
        for i in range(0, MAX_LENGTH_OF_DIGIT + 1): temp.append(list())

        for pattern in patterns:
            temp[len(pattern)].append(pattern)
        return temp

    def getOutputs(self):
        return self.outputs

    def getSignalPatterns(self):
        return self.signal_patterns

    #Returns letters that aren't in seq_one, but are in seq_two
    def __getNotLetters(self, seq_one, seq_two):
        temp = []
        for i in range(0, len(seq_two)):
            l = seq_two[i]
            if (l not in seq_one):
                temp.append(l)
        return temp
        
    def generateKey(self):
        key = []
        for i in range(0, MAX_LENGTH_OF_DIGIT): key.append("")

        # A:
        one = self.signal_patterns[2][0]
        seven = self.signal_patterns[3][0]
        key[0] = self.__getNotLetters(one, seven)[0]

        eight = self.signal_patterns[7][0]

        # C & D & E Candidates:
        cde_candidates = []
        for candi in self.signal_patterns[6]:
            cde_candidates.append(self.__getNotLetters(candi, eight)[0])
        
        # C:
        for candidate in cde_candidates:
            if (candidate in seven):
                key[2] = candidate
        
        # F:
        key[5] = self.__getNotLetters(list(key[2]), one)[0]

        # B & D Candidates:
        not_bd = [key[2], key[5]]
        four = self.signal_patterns[4][0]
        bd_candidates = self.__getNotLetters(not_bd, four)

        # D:
        for cde_candidate in cde_candidates:
            for bd_candidate in bd_candidates:
                if (cde_candidate == bd_candidate):
                    key[3] = cde_candidate

        #B
        for bd_candidate in bd_candidates:
            if (bd_candidate != key[3]):
                key[1] = bd_candidate
        
        #E
        not_e = [key[2], key[3]]
        key[4] = self.__getNotLetters(not_e, cde_candidates)[0]

        #G
        all_but_one = ""
        for i in key:
            all_but_one += str(i)
        key[6] = self.__getNotLetters(all_but_one, eight)[0]
        
        return key

#unscrambles the digit into typical_order
def unscramble(key=list, digit=str):
    temp = ""
    for i in range(0, len(digit)):
        l = digit[i]
        index_ = key.index(l)
        temp += TYPICAL_ORDER[index_]
    return temp

#takes typical order digit and finds it string decimal digit
def convertToDigit(string=str):
    temp = sorted(string)
    final = ""
    for i in temp:
        final += i
    return DIGIT_SIGNALS.index(final)

    
signals = [] # Array of Signals

#Read File
try:
    with open('input.txt', 'r') as file:
        line = file.readline()
        temp = []
        while line != '':
            temp = line.split(" | ")
            outputs = temp[1].split(" ")
            outputs = [i.strip() for i in outputs]
            signal = Signal(temp[0].split(" "), outputs)
            signals.append(signal)
            line = file.readline()
            continue
finally:
    file.close()

counter = 0

for signal in signals:
    key = signal.generateKey()
    outputs = signal.getOutputs()
    final_digit = ""
    for output in outputs:
        digit = str(convertToDigit(unscramble(key, output)))
        final_digit += digit
    counter += int(final_digit)


print("Result: ", counter)