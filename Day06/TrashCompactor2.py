
def calcList(argList, operation):
    total = 0
    if operation == "+":
        for num in argList:
            total += int(num)
    elif operation == "*":
        total = 1
        for num in argList:
            total *= int(num)
    #print (operation, total, argList)
    return total

def getArguments(argumentList):
    transposedList = []
    for col in range(len(argumentList[0])):
        num = ""
        for row in range(len(argumentList)):
            num += argumentList[row][col].strip()
            #print (num, argumentList[row][col])
        if len(num.strip()) > 0:
            transposedList.append(num.strip())
        #print(transposedList)
    return transposedList


file1 = open('Day06/input1.txt', 'r')
Lines = file1.readlines()
file1.close()

arguments = [line for line in Lines[:-1]]
mathOps = Lines[-1]


total = 0

mathOp = mathOps[0]
startIndex = 0
endIndex = 1
while endIndex < len(mathOps):
    if mathOps[endIndex] == " ":
        endIndex += 1
        continue
    
    argumentList = [line[startIndex:endIndex] for line in arguments]
    transposedArgs = getArguments(argumentList)
    total += calcList(transposedArgs, mathOp.strip())
    #print(total)
    startIndex = endIndex
    mathOp = mathOps[startIndex]
    endIndex += 1    

print("-->", startIndex, endIndex, len(mathOps))
argumentList = [line[startIndex:endIndex] for line in arguments]
transposedArgs = getArguments(argumentList)
total += calcList(transposedArgs, mathOp.strip())


print("Final Total:", total)


