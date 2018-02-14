import random


def randomizer(subList):
	semiFinalList = []
	finalistcounter = 0

	while finalistcounter<3:
		
		randomIndex = random.randint(0,len(subList)-1)

		if subList[randomIndex] not in semiFinalList:
			semiFinalList.append(subList[randomIndex])
			finalistcounter = finalistcounter + 1

	return semiFinalList


def uniqueList(numberList):
	uniqueValuesList = []

	for i in numberList:

		if i not in uniqueValuesList:
			uniqueValuesList.append(i)
		

	return uniqueValuesList

def selectWinner(one,two,three, semiFinalList):
	semiList = [one,two,three]
	maxValue = max(semiList)
	print(maxValue)
	winnerIndex = semiList.index(maxValue)

	print("Winner: "+ semiFinalList[winnerIndex])

def semiFinalRandomizer(semiFinalList):
	pickCounter = 0
	pickList = []

	while pickCounter < 100:
		numberIndexer = random.randint(0,len(semiFinalList)-1)
		pickList.append(numberIndexer)
		pickCounter = pickCounter + 1

	#print(pickList)

	distinctValues = uniqueList(pickList)

	#print(distinctValues)

	count1 = 0
	count2 = 0
	count3 = 0

	for i in pickList:
		if pickList[i]== distinctValues[0]:
			count1 = count1 + 1
		elif pickList[i] == distinctValues[1]:
			count2 = count2 + 1
		elif pickList[i] == distinctValues[2]:
			count3 = count3 + 1
	
	print(count1, count2, count3)
	


	selectWinner(count1,count2,count3, semiFinalList)
		
		



b = ["Jim","Kyle","John","Rich","Brandon","Karam"]

semiFinalList = randomizer(b)

semiFinalRandomizer(semiFinalList)

