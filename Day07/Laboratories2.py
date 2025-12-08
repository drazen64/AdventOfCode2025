Lines = []

def printLines():
    l1 = ''.join( [''.join(line) for line in Lines])
    print(l1, sep='\n')

def drawTimelines():
    # draw all timelines
    for row in range(2,len(Lines[0])):        
        for i in range(len(Lines[0])):
            if Lines[row-1][i] == "|":           
                if Lines[row][i] == "^":
                    #split:
                    Lines[row][i+1] = "|"
                    Lines[row][i-1] = "|" 
                else:
                    Lines[row][i] = "|"




def countTimeLines():
    results = len(Lines[0]) * [0]
    rows = len(Lines)-1
    for col in range(len(Lines[0])-1):
        if Lines[rows][col] == "|":
            results[col] = 1  
    
    # go backwards from the last row and count timelines
    for row in range(rows-1,0,-1):
        newResults = len(Lines[0]) * [0]
        for col in range(len(Lines[0])-1):
            if Lines[row][col] == "^":
                #sum timelines from left and right
                newResults[col] += results[col-1] + results[col+1]
            elif Lines[row][col] == "|":
                #continue timeline
                newResults[col] += results[col]
        results = newResults
        #print(results)
    return results



file1 = open('Day07/input1.txt', 'r')
inputData = file1.readlines()
file1.close()

Lines = [list(line) for line in inputData]

startPos = inputData[0].find("S")
row = 1
Lines[1][startPos] = "|"
drawTimelines()
printLines()
result = countTimeLines()

print(result[startPos])




# .......S.......
# ...............
# .......^.......2
# ...............
# ......^.^......2 2
# ...............
# .....^.^.^.....2 2 2
# ...............
# ....^.^...^....2
# ...............
# ...^.^...^.^...2
# ...............
# ..^...^.....^..2
# ...............
# .^.^.^.^.^...^.2
# ...............

#.......S.......
#.......|.......1
#......|^|......2
#......|.|......
#.....|^|^|.....2 2
#.....|.|.|.....
#....|^|^|^|....2 2 2
#....|.|.|.|....
#...|^|^|||^|...2 2 2
#...|.|.|||.|...
#..|^|^|||^|^|..2 2 2 2
#..|.|.|||.|.|..
#.|^|||^||.||^|.2 2 2
#.|.|||.||.||.|.
#|^|^|^|^|^|||^|2 2 2 2 2
#|.|.|.|.|.|||.|