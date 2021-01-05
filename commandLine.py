from cmd import Cmd

from core import sudoku

class SudokuPrompt(Cmd):

    	def preloop(self):
		self.rowList = []
	
	def do_man(self, inp):
	        print("List of commands:")
	        print("- addLine: Insert the 9 values for the next line seprated by comma, in case of empty value insert zero")
	        print("- printInput: Print the current input matrix")
	        print("- resolve: Resolve and print the output matrix")
	        print("- exit: Exit the current prompt")
	        return False
	
	def do_exit(self, inp):
	        print("Exiting Sudoku Prompt")
	        return True
	        
	def do_printInput(self, inp):
		print("Current input matrix is:")
		print(self.rowList)
	
	def processInputLine(self,inputLine):
		#TODO Add line Validation
		inputArrayString = inputLine.split(",")
		inputArray = map(int, inputArrayString)
		return inputArray
	        
	def do_addLine(self, inp):
		#TODO Add control on input matrix
		nextLineNumber = len(self.rowList)+1
		inputLine = raw_input("Insert the 9 values for the line %s separated by comma, in case of empty value insert zero: " % nextLineNumber)
		inputArray = self.processInputLine(inputLine)
		self.rowList.append(inputArray)
	
	def do_resolve(self, inp):
		if len(self.rowList) != 9:
			print("Input matrix must have 9 line")
			return False
		else:			
			sudokuInstance = sudoku.Sudoku(self.rowList)
			resolvedMatrix = sudokuInstance.resolve()
			print("Resolved matrix")
			print(resolvedMatrix)
			return True

SudokuPrompt().cmdloop()
