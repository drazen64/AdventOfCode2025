

file1 = open('Day01/input1.txt', 'r')
Lines = file1.readlines()
file1.close

dial = 50
zeroes = 0

for line in Lines:
    directon = line[0]
    distance = int(line[1:].strip())
    if directon == 'L':
        dial -= distance
        if dial < 0:
            dial = dial % 100         
        if dial == 0:
            zeroes += 1

    elif directon == 'R':
        dial += distance
        if dial >= 100:
            dial = dial % 100            
        if dial == 0:
            zeroes += 1

print(zeroes)
