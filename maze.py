from cell import Cell
import time
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []

        self._create_cells()

    def _create_cells(self):

        for i in range(self.num_cols):
            col = []
            for j in range(self.num_rows):
                col.append(Cell(self.win))
            self._cells.append(col)
        
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i , j):

        if self.win is None:
            return

        # calculate the x/y position of the Cell based on i, j, the cell_size and the x/y of the maze itself
        x = self.x1 + i * self.cell_size_x
        y = self.y1 + j * self.cell_size_y

        #draw the cells and call animate
        self._cells.draw(x, y, x1 + self.cell_size_x, y1 +self.cell_size_y)
        self._animate()

    def _animate(self):
        if self._win is None:
            return

        self._win.redraw()
        time.sleep(0.05)