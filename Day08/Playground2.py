import math

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)


def connectBoxes(distList):
    circuits = [set([i]) for i in range(len(JuBoxes))]

    for dist in distList:
        i, j, d = dist
        added = False
        circuitI = set()
        circuitJ = set()
        for circuit in circuits:
            if i in circuit:
                circuitI = circuit
            if j in circuit:
                circuitJ = circuit
        
        if circuitI == circuitJ:
            continue # already in the same circuit 

        # merge into one circuit
        circuitJ.update(circuitI)
        circuits.remove(circuitI)
        backToOneOneCircuit = len(circuits) == 1

        if backToOneOneCircuit:
            return JuBoxes[i].x * JuBoxes[j].x
    return 0


file1 = open('Day08/input1.txt', 'r')
inputData = file1.readlines()
file1.close()


coordList = [list(int(i) for i in line.split(',')) for line in inputData]

JuBoxes = [Point(coords[0], coords[1], coords[2]) for coords in coordList]

distList = []

for i in range (len(JuBoxes)):
    for j in range(i):
        if i != j:
            distList.append((i, j, JuBoxes[i].distance(JuBoxes[j])))

distList.sort(key=lambda x: x[2])

#print(distList)

coordMult = connectBoxes(distList)


#print(JuBoxes)

#print(circuits)

print(coordMult)