from cell import Cell

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows =num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        _create_cells()

    def _create_cells():

        self._cells = []
        for i in range(self.num_rows):
            self._rows = []
            for j in range(self.num_cols):
                self._rows.append(Cell(self._win))
            self._cells.append(self._rows)
        
        for i in range(self.num_rows):
            for j in range(self.num_cols)
                self._draw_cell(i,j)
    
    def _draw_cell(self, i , j):

        if self._win is None:
            return 
        
        




    def _animate(self):
        pass