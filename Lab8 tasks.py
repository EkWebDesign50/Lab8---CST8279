import gfxhat

def ConvertToCsv(fileName):
    f = open(fileName, "r")
    lines = f.readlines()
    f.close()
    f = open(fileName[0:len(fileName)-4]+".csv", "w")
    f.write("\"First Name\",\"Count\"\n")
    for lino in lines:
        spaceIndex = lino.find(" ")
        newline = "\"" + lino[0:spaceIndex] + "\","+lino[spaceIndex+1:len(lino)]
        f.write(newline)
    f.close()

ConvertToCsv("2000_GirlsNames.txt")
ConvertToCsv("2000_BoysNames.txt")

def displayLines():
    fileName = input("Enter the name of a csv file: ")
    f = open(fileName, "r")
    lineList = f.readlines()
    print(lineList)

displayLines()


def loadDict(fileName):
    f = open(fileName, "r")
    lines = f.readlines()
    f.close()
    d = {}
    for lin in lines:
        a,b = lin.split(",")
        d[b.rstrip()] = a
    return d

d=loadDict("font3.txt")
print(d['a'])
