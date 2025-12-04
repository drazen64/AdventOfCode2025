


def accessible(row, col, Lines):
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
    return nCount < 4

def removeRoles(rows, cols, Lines):
    toBeRemoved = []
    for i in range(rows):
        for j in range(cols):
            if accessible(i, j, Lines):
                toBeRemoved.append((i, j))
    if len(toBeRemoved) == 0:
        return 0
    
    for r in toBeRemoved:
        row = r[0]
        col = r[1]
        Lines[row] = Lines[row][:col] + '.' + Lines[row][col+1:]

    return len(toBeRemoved) + removeRoles(rows, cols, Lines)



file1 = open('Day04/input1.txt', 'r')
Lines = file1.readlines()
file1.close()

pdRows = len(Lines)
pdCols = len(Lines[0].strip())
print(removeRoles(pdRows, pdCols, Lines))