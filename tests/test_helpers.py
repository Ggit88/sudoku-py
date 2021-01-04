import unittest

from .context import helpers

class TestHelpers(unittest.TestCase):
       
	def test_createArrayOfEmptyArrays(self):
	        """
	        Test createArrayOfEmptyArrays
	        """
		data = [[],[],[],[],[],[],[],[],[]]
	        result = helpers.createArrayOfEmptyArrays()
	        self.assertEqual(result, data)
        
	def test_createArrayOfZerosArrays(self):
	        """
	        Test createArrayOfZerosArrays
	        """
		data = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
	        result = helpers.createArrayOfZerosArrays()
	        self.assertEqual(result, data)
        
	def test_countZeroInMatrix(self):
	        """
	        Test countZeroInMatrix
	        """
	        dataInput = [[6,7,9,0,5,0,1,0,4],[0,0,0,1,0,7,2,0,0],[8,0,0,6,9,0,0,5,7],[7,0,0,0,3,0,8,0,0],[2,0,0,8,0,0,6,0,3],[3,0,6,0,2,1,9,0,5],[5,6,0,0,1,3,0,0,0],[0,0,0,5,0,0,4,6,1],[1,4,0,2,6,0,5,0,0]]
		dataOutput = 41
		result = helpers.countZeroInMatrix(dataInput)
		self.assertEqual(result, dataOutput)
	
	def test_createMatricesRowIndexes(self):
	        """
	        Test createMatricesRowIndexes
	        """
	        dataOutput = [[0,0,0,1,1,1,2,2,2],
	        [0,0,0,1,1,1,2,2,2],
	        [0,0,0,1,1,1,2,2,2],
	        [3,3,3,4,4,4,5,5,5],
	        [3,3,3,4,4,4,5,5,5],
	        [3,3,3,4,4,4,5,5,5],
	        [6,6,6,7,7,7,8,8,8],
	        [6,6,6,7,7,7,8,8,8],
	        [6,6,6,7,7,7,8,8,8]]
	        result = helpers.createMatricesRowIndexes()
	        self.assertEqual(result, dataOutput)
        
	def test_createMatricesColumnIndexes(self):
	        """
	        Test createMatricesColumnIndexes
	        """
		dataOutput = [[0,1,2,0,1,2,0,1,2],
		[3,4,5,3,4,5,3,4,5],
		[6,7,8,6,7,8,6,7,8],
		[0,1,2,0,1,2,0,1,2],
		[3,4,5,3,4,5,3,4,5],
		[6,7,8,6,7,8,6,7,8],
		[0,1,2,0,1,2,0,1,2],
		[3,4,5,3,4,5,3,4,5],
		[6,7,8,6,7,8,6,7,8]] 
	        result = helpers.createMatricesColumnIndexes()
	        self.assertEqual(result, dataOutput)
	
	def test_createColumnsArray(self):
	        """
	        Test createColumnsArray
	        """
	        dataInput = [[6,7,9,0,5,0,1,0,4],[0,0,0,1,0,7,2,0,0],[8,0,0,6,9,0,0,5,7],[7,0,0,0,3,0,8,0,0],[2,0,0,8,0,0,6,0,3],[3,0,6,0,2,1,9,0,5],[5,6,0,0,1,3,0,0,0],[0,0,0,5,0,0,4,6,1],[1,4,0,2,6,0,5,0,0]]
		dataOutput = [[6,0,8,7,2,3,5,0,1],[7,0,0,0,0,0,6,0,4],[9,0,0,0,0,6,0,0,0],[0,1,6,0,8,0,0,5,2],[5,0,9,3,0,2,1,0,6],[0,7,0,0,0,1,3,0,0],[1,2,0,8,6,9,0,4,5],[0,0,5,0,0,0,0,6,0],[4,0,7,0,3,5,0,1,0]]
		result = helpers.createColumnsArray(dataInput)
		self.assertEqual(result, dataOutput)

	def test_createMatricesArray(self):
	        """
	        Test createMatricesArray
	        """
	        dataInput = [[6,7,9,0,5,0,1,0,4],[0,0,0,1,0,7,2,0,0],[8,0,0,6,9,0,0,5,7],[7,0,0,0,3,0,8,0,0],[2,0,0,8,0,0,6,0,3],[3,0,6,0,2,1,9,0,5],[5,6,0,0,1,3,0,0,0],[0,0,0,5,0,0,4,6,1],[1,4,0,2,6,0,5,0,0]]
		dataOutput = [[6,7,9,0,0,0,8,0,0],[0,5,0,1,0,7,6,9,0],[1,0,4,2,0,0,0,5,7],
		[7,0,0,2,0,0,3,0,6],[0,3,0,8,0,0,0,2,1],[8,0,0,6,0,3,9,0,5],[5,6,0,0,0,0,1,4,0],[0,1,3,5,0,0,2,6,0],[0,0,0,4,6,1,5,0,0]]
		result = helpers.createMatricesArray(dataInput)
		self.assertEqual(result, dataOutput)    	            	

	def test_findSingleValue_ko(self):
	        """
	        Test findSingleValue_ko
	        """
	        row = [7,0,0,0,3,0,8,0,0]
	        col = [9,0,0,0,0,6,0,0,0]
	        mat = [7,0,0,2,0,0,3,0,6]
		dataOutput = 0
		result = helpers.findSingleValue(row,col,mat)
		self.assertEqual(result, dataOutput)
	
	def test_findSingleValue_ok(self):
	        """
	        Test findSingleValue_ok
	        """
	        row = [6,7,9,0,5,0,1,0,4]
	        col = [0,1,6,0,8,0,0,5,2]
	        mat = [0,5,0,1,0,7,6,9,0]
		dataOutput = 3
		result = helpers.findSingleValue(row,col,mat)
		self.assertEqual(result, dataOutput)

if __name__ == '__main__':
    unittest.main()

