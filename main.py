from window import Window
from cell import Cell

def main():
    win = Window(1000,800)

    c1 = Cell(win)
    c1.draw(300, 300, 450 ,450)    

    c2 = Cell(win)
    c2.draw(300,450, 450 ,600)

    c3 = Cell(win)
    c3.draw(450, 300, 600, 450)

    c4 = Cell(win)
    c4.draw(450, 450, 600, 600)

    c1.draw_move(c2)
    c2.draw_move(c3)
    c3.draw_move(c4)
    c4.draw_move(c1)
    

    win.wait_for_close()

if __name__ == "__main__":
    main()