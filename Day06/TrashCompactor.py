

file1 = open('Day06/input1.txt', 'r')
Lines = file1.readlines()
file1.close()

arguments = [line.split() for line in Lines[:-1]]
mathOps = Lines[-1].strip().split()


total = 0
for col in range(len(mathOps)):
    multTotal = 1
    sumTotal = 0
    for row in range(len(arguments)):
        if mathOps[col] == "+":
            sumTotal += int(arguments[row][col])
        elif mathOps[col] == "*":
            multTotal *= int(arguments[row][col])    
    print(mathOps[col], multTotal, sumTotal)
    if mathOps[col] == "*":
        total += multTotal
    elif mathOps[col] == "+":
        total += sumTotal


print("Final Total:", total)


