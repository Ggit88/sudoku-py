import unittest

from .context import sudoku as sd

class TestSudoku(unittest.TestCase):

    def test_resolve(self):
        """
        Test resolve
        """
        dataInput = [[6,7,9,0,5,0,1,0,4],
[0,0,0,1,0,7,2,0,0],
[8,0,0,6,9,0,0,5,7],
[7,0,0,0,3,0,8,0,0],
[2,0,0,8,0,0,6,0,3],
[3,0,6,0,2,1,9,0,5],
[5,6,0,0,1,3,0,0,0],
[0,0,0,5,0,0,4,6,1],
[1,4,0,2,6,0,5,0,0]]
        dataOutput = [[6,7,9,3,5,2,1,8,4],
[4,3,5,1,8,7,2,9,6],
[8,1,2,6,9,4,3,5,7],
[7,5,4,9,3,6,8,1,2],
[2,9,1,8,4,5,6,7,3],
[3,8,6,7,2,1,9,4,5],
[5,6,8,4,1,3,7,2,9],
[9,2,3,5,7,8,4,6,1],
[1,4,7,2,6,9,5,3,8]]
	sudoku = sd.Sudoku(dataInput)
	result = sudoku.resolve()
	self.assertEqual(result, dataOutput)
	
    def test_iterationsCount(self):
        """
        Test iterationsCount
        """
        dataInput = [[6,7,9,0,5,0,1,0,4],
[0,0,0,1,0,7,2,0,0],
[8,0,0,6,9,0,0,5,7],
[7,0,0,0,3,0,8,0,0],
[2,0,0,8,0,0,6,0,3],
[3,0,6,0,2,1,9,0,5],
[5,6,0,0,1,3,0,0,0],
[0,0,0,5,0,0,4,6,1],
[1,4,0,2,6,0,5,0,0]]
        dataOutput = 5
	sudoku = sd.Sudoku(dataInput)
	sudoku.resolve()
	result = sudoku.iterationsCount
	self.assertEqual(result, dataOutput)

if __name__ == '__main__':
    unittest.main()
