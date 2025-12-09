


file1 = open('Day05/input1.txt', 'r')
Lines = file1.readlines()
file1.close()

ranges = []
available = []
blankLineFound = False
for line in Lines:
    line = line.strip()
    if line == '':
        blankLineFound = True
        continue
    if not blankLineFound:
        parts = line.split('-')
        start = int(parts[0])
        end = int(parts[1])
        ranges.append( (start, end) )
    else:
        available.append( int(line) )

fresh = 0
for ingredient in available:
    for r in ranges:
        if ingredient >= r[0] and ingredient <= r[1]:
            fresh += 1
            break


print(fresh)
