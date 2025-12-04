
def calcJoltage(batBank :str, bankNo: int) -> int:
    if bankNo > 12:
        return 0
    
    maxPos = 0
    maxJoltage = 0
    # nađi najveći
    for i in range(len(batBank)-(12-bankNo)):
        if int(batBank[i]) > maxJoltage:
            maxJoltage = int(batBank[i])
            maxPos = i
    
    return maxJoltage*10**(12-bankNo) + calcJoltage(batBank[maxPos+1:], bankNo+1)


file1 = open('Day03/input1.txt', 'r')
Lines = file1.readlines()
file1.close()

totalJoltage = 0 
for line in Lines:
    totalJoltage += calcJoltage(line.strip(), 1)

print(totalJoltage)