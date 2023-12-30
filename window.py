from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self,width,height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self._canvas = Canvas(self.__root, bg ="black",width = width, height = height)
        self._canvas.pack(fill=BOTH,expand=1)
        self.WINDOW_RUN = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.WINDOW_RUN = True
        while self.WINDOW_RUN == True:
            self.redraw()

    def draw_line(self,line,fill_color="white"):
        line.draw(self._canvas,fill_color)   

    def close(self):
        self.WINDOW_RUN = False
            

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Line:
    def __init__(self,p1,p2):
        self.point1 = p1
        self.point2 = p2

    def draw(self,canvas,fill_color="black"):
        canvas.create_line(
            self.point1.x,
            self.point1.y,
            self.point2.x,
            self.point2.y, 
            fill=fill_color,width=2
        )
        canvas.pack(fill=BOTH,expand = 1)