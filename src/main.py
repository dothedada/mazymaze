from graphics import Window, Point
from cell import Cell


def main():
    win = Window(600, 800)

    c = Cell(win)
    c.has_left = False
    c.draw(Point(50, 50), Point(100, 100))

    c = Cell(win)
    c.has_right = False
    c.draw(Point(125, 125), Point(200, 200))

    c = Cell(win)
    c.has_bottom = False
    c.draw(Point(225, 225), Point(250, 250))

    c = Cell(win)
    c.has_top = False
    c.draw(Point(300, 300), Point(500, 500))

    win.wait_for_close()


if __name__ == "__main__":
    main()
