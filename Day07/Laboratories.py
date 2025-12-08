




file1 = open('Day07/test1.txt', 'r')
Lines = file1.readlines()
file1.close()

startPos = Lines[0].find("S")
beams = set([startPos])
row = 1
totalSplits = 0
print(len(Lines))
while row < len(Lines)-1:
    newBeams = set()
    for beam in beams:
        print(row, beam, Lines[row])
        if Lines[row][beam] == "^":
            newBeams.add(beam -1)
            newBeams.add(beam +1)
            totalSplits += 1
        else:
            newBeams.add(beam)
    beams = newBeams
    row += 1

print(totalSplits)