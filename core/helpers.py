def createArrayOfEmptyArrays():
	return [[] for i in range(0,9)] 
	
def createArrayOfZerosArrays():
	return [[0 for j in range (0,9)] for i in range (0,9)]

def createSameValueRepeatedArray(startingIndex):
	array = []
	for n in range (0,3):
		array = array + [startingIndex + n for i in range (0,3)]
	return array

def createMatricesRowIndexes():
	array = []
	for n in [0, 0, 0, 3, 3, 3, 6, 6, 6]:
		array.append(createSameValueRepeatedArray(n))
	return array
	
def createIncrementValueRepeatedArray(startingIndex):
	array = []
	for n in range (0,3):
		array = array + range(startingIndex,startingIndex+3)
	return array

def createMatricesColumnIndexes():
	array = []
	for n in [0,3,6,0,3,6,0,3,6]:
		array.append(createIncrementValueRepeatedArray(n))
	return array

def createColumnsArray(inputMatrix):
	colList = createArrayOfEmptyArrays()
	for r in range(0,9):
		for c in range(0,9):
	    		colList[c].append(inputMatrix[r][c])
	return colList
	
def createMatricesArray(inputMatrix):
	matList = createArrayOfEmptyArrays()
	matRowIndexes = createMatricesRowIndexes();
	for r in range(0,9):
	     	for c in range(0,9):
			matList[createMatricesRowIndexes()[r][c]].append(inputMatrix[r][c])
	return matList

def countZeroInMatrix(inputMatrix):
	countZero = 0;
	for i in range(len(inputMatrix)):
		countZero += inputMatrix[i].count(0)
	return countZero

def diffArray(array1,array2):
	diff = [item for item in array1 if item not in array2]
	return diff

def findSingleValue(row,col,mat):
	commonValues = diffArray(range(1,10),row)
	if(len(commonValues)==1):
		return commonValues[0]
	commonValues = diffArray(commonValues,col)
	if(len(commonValues)==1):
		return commonValues[0]
	commonValues = diffArray(commonValues,mat)
	if(len(commonValues)==1):
		return commonValues[0]
	return 0
