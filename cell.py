from window import Line, Point
class Cell:
    def __init__(self, window):

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None

        self._win = window
    
    def draw(self,x1,y1,x2,y2):

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self.has_left_wall:
            line = Line(Point(x1,y1),Point(x1,y2))
            self._win.draw_line(line)

        if self.has_right_wall:
            line = Line(Point(x2,y1),Point(x2,y2))
            self._win.draw_line(line)

        if self.has_top_wall:
            line = Line(Point(x1,y1),Point(x2,y1))
            self._win.draw_line(line)

        if self.has_bottom_wall:
            line = Line(Point(x1,y2),Point(x2,y2))
            self._win.draw_line(line)

    def draw_move(self,to_cell,undo=False):
        
        # if undo "flag" is not set, draw red, else make it gray
        # use the x/y coordinates of the 2 cells in question to decide how to draw the line connectong two cells
        # need to use the mid-point formula and distance formula
        
        mid_x = (self._x1 + self._x2) // 2
        mid_y = (self._y1 + self._y2) // 2

        to_cell_x = (to_cell._x1 + to_cell._x2) // 2 
        to_cell_y = (to_cell._y1 + to_cell._y2) // 2

        color ="red"
        line = Line(Point(mid_x,mid_y),Point(to_cell_x,to_cell_y))

        if undo:
            color = "gray"
        
        self._win.draw_line(line,color)
            



