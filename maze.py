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
        seed = None
    ):
        if seed not None:
            random.seed(random)

        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        self._create_cells()
        self._break_entrance_break_exit()

    def _create_cells(self):

        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)
        
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i , j):

        if self._win is None:
            return

        # calculate the x/y position of the Cell based on i, j, the cell_size and the x/y of the maze itself
        x = self._x1 + i * self._cell_size_x
        y = self._y1 + j * self._cell_size_y

        x2 = x + self._cell_size_x
        y2 = y + self._cell_size_y
        
        #draw the cells and call animate
        self._cells[i][j].draw(x, y, x2 , y2)
        self._animate()

    def _animate(self):

        if self._win is None:
            return

        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_break_exit(self):
        if self._win is None:
            return

        # Entrance 
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)

        # Exit 
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols -1,self._num_rows - 1)

    def _break_walls_r(self, i, j):
        pass