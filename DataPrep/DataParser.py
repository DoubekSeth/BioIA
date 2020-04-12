import random
#in
def readIn(fileName):
    file = open(fileName, "r")
    contents = file.read()
    file.close()
    return contents

raw = readIn("Data/Data.csv")

#Get'em Arrayed
countryArr = str(raw).split("\n")
countryArr = countryArr[1:]
dataArr = []
for country in countryArr:
    info = str(country).split(",")
    isLong = False
    if(info[0].startswith('"')):
       countryName = info[0] + info[1]
       isLong = True
    else:
       countryName = info[0]
    category = info[2]
    if(isLong):
        category = info[3]
    dataArr.append([countryName, category, info[len(info)-1]])
    
counter = 1
countryData = []
miniCountryArr = []
for country in dataArr:
    miniCountryArr.append([country[1], country[2]])
    counter += 1
    if(counter == 6):
        miniCountryArr.insert(0, country[0])
        countryData.append(miniCountryArr)
        miniCountryArr = []
        counter = 1


goodCountry = []
for country in countryData:
    isGood = True
    for i in range(1, 6):
        if(country[i][1] == ".."):
            isGood = False
    if(isGood):
        goodCountry.append(country)

print(len(goodCountry))
for country in goodCountry:
    print(country[0])

trainOut = "Diabetes,GDP,Internet,UrbanPop,Income\n"
testOut = "Diabetes,GDP,Internet,UrbanPop,Income\n"
output = ""
for country in goodCountry:
    output += country[2][1] + "," + country[1][1] + "," + country[3][1] + "," + country[4][1] + "," + country[5][1] + "\n"


outArr = output.split("\n")
print(len(outArr))
for i in range(0, 20):
    randomSpot = random.randint(0, len(outArr) - 1)
    testOut += outArr[randomSpot] + "\n"
    del outArr[randomSpot]

for remaining in outArr:
    trainOut += remaining + "\n"
    

def writeOut(fileName, perim):
    file = open(fileName, "w")
    file.write(perim)
    file.close()
    
writeOut("trainData.csv", trainOut)
writeOut("testData.csv", testOut)




