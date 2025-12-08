import math

MaxConnectedPairs = 1000

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def distance(self, other):
        #return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)


def connectBoxes(distList):
    circuits = []
    connected = set()
    numConnectedPairs = 0
    for dist in distList:
        i, j, d = dist
        if numConnectedPairs == MaxConnectedPairs:
            break
        #if i in connected and j in connected:
        #    continue
        added = False
        circuitI = set()
        circuitJ = set()
        for circuit in circuits:
            if i in circuit:
                circuitI = circuit
            elif j in circuit:
                circuitJ = circuit
        
        if circuitI == circuitJ and len(circuitI) > 0 and len(circuitJ) > 0:
            continue # already in the same circuit 

        if len(circuitI) > 0 and len(circuitJ) > 0:
            # merge into one circuit
            circuitI.update(circuitJ)
            circuits.remove(circuitJ)
            added = True
        elif len(circuitI) > 0 and len(circuitJ) == 0:
            # add to circuit I
            circuitI.add(j)
            added = True
        elif len(circuitJ) > 0 and len(circuitI) == 0:
            # add to circuit J
            circuitJ.add(i)
            added = True
        else:
            newCircuit = set()
            #if i not in connected:
            newCircuit.add(i)
            #if j not in connected:
            newCircuit.add(j)
            circuits.append(newCircuit)
        connected.add(i)
        connected.add(j)
        numConnectedPairs += 1
    return circuits


file1 = open('Day08/input1.txt', 'r')
inputData = file1.readlines()
file1.close()


coordList = [list(int(i) for i in line.split(',')) for line in inputData]

JuBoxes = [Point(coords[0], coords[1], coords[2]) for coords in coordList]

boxesCount = len(JuBoxes)
distCount = boxesCount * (boxesCount-1)//2 

distList = []

for i in range (len(JuBoxes)):
    for j in range(i):
        if i != j:
            distList.append((i, j, JuBoxes[i].distance(JuBoxes[j])))

distList.sort(key=lambda x: x[2])

circuits = connectBoxes(distList)

circuitLengths = [len(circuit) for circuit in circuits]
circuitLengths.sort(reverse=True)



#print(JuBoxes)
#print(distList)
#print(circuits)

print(circuitLengths, circuitLengths[0]*circuitLengths[1]*circuitLengths[2])