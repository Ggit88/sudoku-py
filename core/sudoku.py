import helpers

class Sudoku:

	def __init__(self, inputMatrix=[]):
	        self.__rowList = inputMatrix
	        self.__colList = helpers.createColumnsArray(inputMatrix)
	        self.__matList = helpers.createMatricesArray(inputMatrix)
	        self.__initialZeroCount = helpers.countZeroInMatrix(inputMatrix)
	        self.iterationsCount = 0

	def __processSingleValue(self,singleValue,r,c):
		self.__rowList[r][c] = singleValue
		self.__colList[c][r] = singleValue
		self.__matList[helpers.createMatricesRowIndexes()[r][c]][helpers.createMatricesColumnIndexes()[r][c]] = singleValue
		self.__initialZeroCount -= 1
	
	def __processCellZero(self,r,c):
		singleValue = helpers.findSingleValue(self.__rowList[r],self.__colList[c],self.__matList[helpers.createMatricesRowIndexes()[r][c]])
		if(singleValue!=0):
			self.__processSingleValue(singleValue,r,c)
			
	def __processCell(self,r,c):
		if self.__rowList[r][c] == 0:
			self.__processCellZero(r,c)		
	
	def __processRowWithZeros(self,r):
		for c in range(0,9):
			self.__processCell(r,c)
	
	def __processRow(self,r):
		if self.__rowList[r].count(0) > 0:
			self.__processRowWithZeros(r)
	
	def __processIteration(self):
		self.iterationsCount += 1
		for r in range(0,9):
			self.__processRow(r)			

	def resolve(self):
		while(self.__initialZeroCount>0):
			self.__processIteration()
		return self.__rowList
