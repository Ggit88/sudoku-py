import Tkinter as tk

from core import helpers
from core import sudoku

class Application(tk.Frame):

	def initGrid(self):
		self.topFrame = tk.Frame(root, bg = 'lavender', width = 200, height=10, relief = 'raised').grid(row = 0, column = 0, columnspan = 9,  sticky="w")
		for i in range(1,10):
	    		for j in range(0,9):
				text_var = tk.StringVar()				  
				tk.Entry(textvariable=text_var, width = 2).grid(row=i, column=j)
				self.entryMatrix[i-1].append(text_var)   
		self.button = tk.Button(text='Confirm', command=self.confirm).grid(row=11, column=0, columnspan = 9)

	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.entryMatrix = helpers.createArrayOfEmptyArrays()
		self.initGrid()
	
	def updateGrid(self,inputMatrix):
		for i in range(0,9):
	    		for j in range(0,9):
				self.entryMatrix[i][j].set('%s' % inputMatrix[i][j])
	
	def createIntMatrixFromStringVar(self,stringMatrix):
		intMatrix = helpers.createArrayOfZerosArrays()
		for i in range(0,9):
			for j in range(0,9):
				variable = stringMatrix[i][j].get()
				if variable:
					intMatrix[i][j] = int(stringMatrix[i][j].get())
		return intMatrix
	
	def confirm(self):
		intMatrix = self.createIntMatrixFromStringVar(self.entryMatrix)
		sudokuInstance = sudoku.Sudoku(intMatrix)
		resolvedMatrix = sudokuInstance.resolve()
		self.updateGrid(resolvedMatrix)	

root = tk.Tk()
root.title("Sudoku")
app = Application(master=root)
app.mainloop()

