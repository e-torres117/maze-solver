from window import Window
from maze import Maze

def main():
   
    num_cols = 10
    num_rows = 12
    cell = 100
    window_x = 1200
    window_y = 800
    size_x = (window_x - 2 * cell) // num_cols
    size_y = (window_y - 2 * cell) // num_rows
    win = Window(window_x,window_y)

    m1 = Maze(cell, cell, num_rows, num_cols, size_x, size_y, win)
    win.wait_for_close()

if __name__ == "__main__":
    main()