

def addToMergeList(r, mergeList):
    newList = []
    start = r[0]
    end = r[1]
    for interval in mergeList:
        if start <= interval[1] and end >= interval[0]:
            # inside existing interval
            start = min(start, interval[0])
            end = max(end, interval[1])
        else:
            newList.append(interval)
    newList.append( (start, end) )
    return newList



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
        break
    parts = line.split('-')
    start = int(parts[0])
    end = int(parts[1])
    ranges.append( (start, end) )

fresh = 0
mergeList = []
for r in ranges:
    mergeList = addToMergeList(r, mergeList)

ingCount = 0
for interval in mergeList:
    ingCount += (interval[1] - interval[0] + 1)

print(ingCount)