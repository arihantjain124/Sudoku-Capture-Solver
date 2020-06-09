# Sudoku Capture Solver

> Sudoku Capturing and then Solving it from an Image

The Program uses Opencv to find sudoku puzzle in an image which is then resized and sent to divide among individual cells and passed through a Neural Network for digit recognizing and blank cells are read as "0". The output is passed to sudoku .py which solves sudoku using backtracking its basically an optimized brute-force approach.

Code in Action on a mobile captured image.

![](workingexample.gif)

## what's ahead

> Contours are used here to find the sudoku puzzle this leads to some cases in which the puzzle is not recognized and this can be improved upon.

> The sudoku solving algorithm is a brute-force approach this can be improved upon by using a more efficient solution
