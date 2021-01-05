from sys import argv

import csv
import os.path

from core import helpers
from core import sudoku

print(len(argv))

if len(argv) != 3:
	print("Two args are mandatory for sudoku command:")
	print("1) csv file path for reading input matrix")
	print("2) csv file path for writing resolved matrix")
	exit()

sourcePath = argv[1]
destPath = argv[2]

if not os.path.isfile(sourcePath):
    print ("Source file path not exist")
    exit()
    
initialMatrix = helpers.createArrayOfEmptyArrays()

with open(sourcePath) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		for i in range(0,9):
			initialMatrix[line_count].append(int(row[i]))
	        line_count += 1

sudokuInstance = sudoku.Sudoku(initialMatrix)
resolvedMatrix = sudokuInstance.resolve()

with open(destPath, mode='w') as resolved:
	resolved = csv.writer(resolved, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	for i in range(0,9):
		resolved.writerow(resolvedMatrix[i])
