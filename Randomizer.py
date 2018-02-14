#Custom made algorithm for picking a subscribed winner

import random

#creates a list of 3 semifinalists
def randomizer(subList):
	semiFinalList = []
	finalistcounter = 0

	while finalistcounter<3:
		
		randomIndex = random.randint(0,len(subList)-1)

		if subList[randomIndex] not in semiFinalList:
			semiFinalList.append(subList[randomIndex])
			finalistcounter = finalistcounter + 1

	return semiFinalList

#populates a list of unique values from the list passed in
def uniqueList(numberList):
	uniqueValuesList = []

	for i in numberList:

		if i not in uniqueValuesList:
			uniqueValuesList.append(i)
		

	return uniqueValuesList

#picks the winner from the semifinalist list based on the highest frequency of random numbers in the semiFinalList
def selectWinner(one,two,three, semiFinalList):
	semiList = [one,two,three]
	maxValue = max(semiList)
	print(maxValue)
	winnerIndex = semiList.index(maxValue)

	print("Winner: "+ semiFinalList[winnerIndex])

#creates a list of 100 values mapping to 3 semifinalists.
#This is creating a list of number variances.
def semiFinalRandomizer(semiFinalList):
	pickCounter = 0
	pickList = []

	while pickCounter < 100:
		numberIndexer = random.randint(0,len(semiFinalList)-1)
		pickList.append(numberIndexer)
		pickCounter = pickCounter + 1


	distinctValues = uniqueList(pickList)


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
		
		


#Test data
b = ["Jeff","Jim","Kyle","John","Rich","Brandon","Karam"]

semiFinalList = randomizer(b)

semiFinalRandomizer(semiFinalList)

