
def calcJoltage(batBank :str) -> int:
    maxPos = 0
    maxJoltage = 0
    # nađi najveći
    for i in range(len(batBank)-1):
        if int(batBank[i]) > maxJoltage:
            maxJoltage = int(batBank[i])
            maxPos = i
    
    secondMax = 0
    for i in range(maxPos+1, len(batBank)):
        if int(batBank[i]) > secondMax:
            secondMax = int(batBank[i])

    return maxJoltage*10 + secondMax


file1 = open('Day03/input1.txt', 'r')
Lines = file1.readlines()
file1.close()

totalJoltage = 0 
for line in Lines:
    totalJoltage += calcJoltage(line.strip())

print(totalJoltage)