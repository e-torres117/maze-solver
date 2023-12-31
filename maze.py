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

        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self.seed = seed
        self._cells = []
        
        if self.seed:
            random.seed(random)  

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
      

    def _create_cells(self):

        for i in range(self._num_rows):
            cols = []
            for j in range(self._num_cols):
                cols.append(Cell(self._win))
            self._cells.append(cols)
        
        for i in range(self._num_rows):
            for j in range(self._num_cols):
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

    def _break_entrance_and_exit(self):
        if self._win is None:
            return

        # Entrance 
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)

        # Exit 
        self._cells[self._num_rows - 1][self._num_cols - 1].has_bottom_wall = False
        self._draw_cell(self._num_rows - 1, self._num_cols - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True

        while True:
            to_visit = []

            # bounds checks for possible directions
            # up
            if j < self._num_cols - 1 and not self._cells[i][j + 1]._visited:
                to_visit.append((i, j + 1))

            # right
            if  i < self._num_rows - 1 and not self._cells[i + 1][j]._visited:
                to_visit.append((i + 1, j))
            
            # down
            if j > 0 and not self._cells[i][j - 1]._visited:
                to_visit.append((i, j - 1))

            # left
            if i > 0 and not self._cells[i - 1][j]._visited:
                to_visit.append((i - 1, j))

            if not to_visit:
                self._draw_cell(i, j)
                return
            
            rand_index = random.randint(0, len(to_visit) - 1)
            next_i, next_j = to_visit[rand_index]
       
            # Knock down the walls between the current cell and the chosen cell.
            # right
            if next_i == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][j].has_left_wall = False
                
            # down(y- is counter-intuitive)   
            if next_j == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][next_j].has_bottom_wall = False

            # left
            if next_i == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][j].has_right_wall = False
                
            # up(y- is counter-intuitive)   
            if next_j == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][next_j].has_top_wall = False
                     
            self._break_walls_r(next_i, next_j)

    def _reset_cells_visited(self):
         for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._cells[i][j]._visited = False 

    def solve(self):
        if self._solve_r(0,0):
            return True
        
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j]._visited = True

        if i == self._num_rows - 1 and j == self._num_cols - 1:
            return True

        # for each direction 
        move_index = []

        # left
        if i > 0 and not self._cells[i][j].has_left_wall and not self._cells[i - 1][j]._visited:
            move_index.append((i - 1, j))

        #down
        if j < self._num_cols - 1 and not self._cells[i][j].has_bottom_wall and not self._cells[i][j + 1]._visited:
            move_index.append((i, j + 1))

        #up
        if j > 0 and not self._cells[i][j].has_top_wall and not self._cells[i][j - 1]._visited:
            move_index.append((i, j - 1))

        #right
        if i < self._num_rows - 1 and not self._cells[i][j].has_right_wall and not self._cells[i + 1][j]._visited:
            move_index.append((i + 1, j))
            
        for move in move_index:
            move_i, move_j = move

            self._cells[i][j].draw_move(self._cells[move_i][move_j])

            if self._solve_r(move_i, move_j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[move_i][move_j], True)


        return False