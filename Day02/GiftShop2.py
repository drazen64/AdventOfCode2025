def PrebrojiDuplikatePoBrojuZnamenki(id: int, brojZnamenki: int, rangeStart: int, rangeEnd: int, listaDuplikata):
    idStr = str(id)
       
    if len(idStr) % brojZnamenki > 0:
        return 0
    
    length = len(idStr) // brojZnamenki

    prvi = idStr[0:brojZnamenki]
    zadnji = (brojZnamenki) * "9"
    sumaDuplikata = 0
    for i in range(int(prvi), int(zadnji)+1):
        # napravi duplikat
        noviID = str(i) * length
        noviIDInt = int(noviID)
        # provjeri je li duplikat u rasponu
        if noviIDInt < rangeStart:
            continue
        if noviIDInt > rangeEnd:
            break
        # provjeri je li već pronađen: ovo sprečava da se isti duplikat broji više puta
        # Npr za id=1111 i brojZnamenki=1 i 2 dobijemo isti duplikat 1111
        if noviIDInt in listaDuplikata:
            continue
        print("  Duplicat found: ", noviIDInt)
        listaDuplikata.append(noviIDInt)
        sumaDuplikata += noviIDInt
    return sumaDuplikata




def PrebrojiDuplikate(id: int, rangeStart: int, rangeEnd: int):
    idStr = str(id)
    polovicaDuljine = len(idStr) // 2
    sumaDuplikata = 0
    # tražimo brojeve s ponavljajućim sekvencama od 1 do polovice ukupnog broja znamenki
    listaDuplikata = []
    for brojZnamenki in range(1, polovicaDuljine+1):
        sumaDuplikata += PrebrojiDuplikatePoBrojuZnamenki(id, brojZnamenki, rangeStart, rangeEnd, listaDuplikata)

    return sumaDuplikata

def sumInvalidIDs(rangeStart: int, rangeEnd: int):
    invalidIdSum = 0
    id = rangeStart
    while id <= rangeEnd:    
        strID = str(id)
        invalidIdSum += PrebrojiDuplikate(id, rangeStart, rangeEnd)
        # sad smo pokrili sve duplikate za trenutni broj znamenki
        # generiraj prvi Id s jednom znamenkom više
        id = 10**(len(strID)) 
        print('Prvi veći: ' , id)
        if id > rangeEnd:
            break
    return invalidIdSum



file1 = open('Day02/input1.txt', 'r')
Lines = file1.readlines()
file1.close()

#Lines = ['11-22']
for line in Lines:
    ranges = line.strip().split(',')
    totalInvalidIDs = 0
    for idRange in ranges:    
        print( idRange)
        first, second = idRange.strip().split('-')
        totalInvalidIDs += sumInvalidIDs(int(first), int(second))

print(totalInvalidIDs)