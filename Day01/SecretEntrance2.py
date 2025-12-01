

file1 = open('Day01/input1.txt', 'r')
Lines = file1.readlines()
file1.close

dial = 50
zeroes = 0



for line in Lines:
    directon = line[0]
    distance = int(line[1:].strip())
    if directon == 'L':
        if dial > 0 and dial <= distance % 100:
            zeroes += 1
        zeroes += distance // 100
        #print(dial, -distance, dial-distance, ((dial-distance) // 100) + 1, zeroes, (dial-distance)%100)
        dial -= distance
        dial = dial % 100        


    elif directon == 'R':
        if dial > 0 and dial + distance % 100 >= 100:
            zeroes += 1
        zeroes += distance // 100

        #print(dial, distance, dial+distance, zeroes, (dial+distance)%100)        
        dial += distance
        dial = dial % 100            

print(zeroes)
