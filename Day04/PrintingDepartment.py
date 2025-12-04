

def checkAccess(row, col, Lines):
    if Lines[row][col] != '@':
        return 0
    neighbours = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1),          (0, 1),
                 (1, -1),  (1, 0), (1, 1)]    
    nCount = 0
    for n in neighbours:
        nRow = row + n[0]
        nCol = col + n[1]
        if nRow < 0 or nRow >= len(Lines):
            continue
        if nCol < 0 or nCol >= len(Lines[0].strip()):
            continue
        if Lines[nRow][nCol] == '@':
            nCount += 1
    return 1 if nCount < 4 else 0




file1 = open('Day04/input1.txt', 'r')
Lines = file1.readlines()
file1.close()

pdRows = len(Lines)
pdCols = len(Lines[0].strip())


accCounter = 0
for i in range(pdRows):
    for j in range(pdCols):
        accCounter += checkAccess(i, j, Lines)
        
print(accCounter)