
def PrebrojiDuplikate(id: int, rangeStart: int, rangeEnd: int):
    idStr = str(id)
    length = len(idStr) // 2
    prvi = idStr[0:length]
    zadnji = length * "9"
    sumaDuplikata = 0
    for i in range(int(prvi), int(zadnji)+1):
        # napravi duplikat
        noviID = str(i) + str(i)
        noviIDInt = int(noviID)
        # provjeri je li duplikat u rasponu
        if noviIDInt < rangeStart:
            continue
        if noviIDInt > rangeEnd:
            break
        print("  Duplicat found: ", noviIDInt)
        sumaDuplikata += noviIDInt
    return sumaDuplikata

def sumInvalidIDs(rangeStart: int, rangeEnd: int):
    invalidIdSum = 0
    id = rangeStart
    while id <= rangeEnd:    
        strID = str(id)
        if len(strID) % 2 != 0:
            # preskoci sve brojeve s neparnim brojem znamenki
            # prvi sljedeći broj s jednom znamenkom više
            id = 10**(len(strID))
            print('Prvi veći: ' , id)
            continue
        invalidIdSum += PrebrojiDuplikate(id, rangeStart, rangeEnd)
        # sad smo pokrili sve duplikate za trenutni broj znamenki
        # generiraj prvi Id s jednom znamenkom više
        id = 10**(len(strID)+1) 
        print('Prvi veći: ' , id)
        if id > rangeEnd:
            break
    return invalidIdSum



file1 = open('Day02/input1.txt', 'r')
Lines = file1.readlines()
file1.close()

#Lines = ['1188511880-1188511890']
for line in Lines:
    ranges = line.strip().split(',')
    totalInvalidIDs = 0
    for idRange in ranges:    
        print( idRange)
        first, second = idRange.strip().split('-')
        totalInvalidIDs += sumInvalidIDs(int(first), int(second))

print(totalInvalidIDs)