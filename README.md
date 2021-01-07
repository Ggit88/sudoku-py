# sudoku-py
Sudoku resolver, a toy project to learn python fundamentals.

# Core Logic
The logic is in the **core** package, the sudoku module contains a class with resolvign algorithm, the helpers module contains some utility functions.

# Testing
The **test** package contains some unit test for the core logic.
From root folder is possible to execute all test modules:
```console 
nosetests
```
or execute a single test module:
```console 
python -m tests.test_sudoku
```

# Executables
The sudoku resolver is executable in a few ways:
## Command
The command executable reads input matrix from a csv file and writes the resolved matrix to an output csv file, paths of these files are expected as input parameters to the command. File examples are in the **data** folder.
```console
python command.py data/input.csv data/resolved.csv
```
## Prompt
The prompt executable reads from user input commands to add line to the input matrix, print current input matrix, resolve sudoku and exit the prompt. For a detailed list of all available commands use the *man* command.
```console
python prompt.py
```
## GUI
The gui executable renders a 9x9 graphical matrix for user input and a button for start resolving sudoku.
```console
python gui.py
```

# Environment
This project ha been tested up and running with **Python 2.7.18**.

No additional modules are required so no dependency management is provided.

