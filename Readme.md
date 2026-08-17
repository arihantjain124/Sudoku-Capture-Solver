# Sudoku Capture Solver 🔢

Point a camera at a printed Sudoku puzzle and get it solved on screen — a computer-vision pipeline that finds, reads, and solves a Sudoku grid from a live/photographed image.

![Code in action on a mobile-captured image](workingexample.gif)

## How it works

1. **Capture & locate** ([`sudokucapture.py`](sudokucapture.py)) — OpenCV contour detection finds the largest quadrilateral in the frame (the puzzle border) and applies a perspective warp to get a top-down, uniformly-sized view of the grid.
2. **Read digits** ([`sudokuread.py`](sudokuread.py)) — the warped grid is sliced into its 81 cells; each cell is preprocessed (grayscale, histogram-equalised, normalised) and passed through a small CNN (`model.p`, a pickled Keras/TensorFlow model) to classify the digit, with empty cells read as `0`.
3. **Solve** ([`sudoku.py`](sudoku.py)) — the recognized 9×9 grid is solved with a backtracking search (an optimised brute-force constraint solver over each cell's possible values).
4. **Display** ([`sudoku_visual.py`](sudoku_visual.py) / `sudoku_visual_cmd.py`) — the solution is overlaid back onto the original image / printed to the terminal.

## Requirements

- Python 3
- OpenCV (`opencv-python`)
- TensorFlow / Keras
- NumPy

```bash
pip install -r requirements.txt

# Solve from a webcam feed
python sudokucapture.py

# Or solve from one of the sample test images
python sudokuread.py --image Test_Images/1.png
```

> Test images for a quick try are included in [`Test_Images/`](Test_Images).

## What's ahead

> Contours are used to find the sudoku puzzle in the frame — this leads to occasional misses when the puzzle isn't cleanly detected, which could be improved with more robust corner detection.

> The solving algorithm is a brute-force backtracking approach; this could be improved with a more efficient constraint-propagation solver (e.g. dancing links / exact cover).
