# Sudoku Capture Solver

> Sudoku Capturing and then Solving it from an Image

The Program uses Opencv to find sudoku puzzle in an image which is then resized and sent to divide among individual cells and passed through a Neural Network for digit recognizing and blank cells are read as "0". The output is passed to sudoku .py which solves sudoku using backtracking its basically a optimized brute-force approach. 

Code in Action on a mobile captured image.

![](http://g.recordit.co/roGLJ1MQa1.gif)

## what's ahead
> Contours are used here to find sudoku puzzle this leads to some cases in which the puzzle is not recgonized and this can be imporved upon.

> The sudoku solving algorithm is brute-force approach this can be imporved upon by using a more efficent solution
