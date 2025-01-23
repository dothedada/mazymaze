from graphics import Window, Point, Line, Cell


def main():
    win = Window(600, 800)

    win.draw_line(Line(Point(10, 10), Point(100, 10)))
    win.draw_line(Line(Point(100, 10), Point(100, 100)))
    win.draw_line(Line(Point(100, 100), Point(10, 100)))
    win.draw_line(Line(Point(10, 100), Point(10, 10)), "black")

    win.draw_cell(Cell(Point(100, 100), Point(200, 200)))
    win.draw_cell(Cell(Point(150, 150), Point(300, 300)))
    win.draw_cell(Cell(Point(10, 100), Point(250, 250)))

    win.wait_for_close()


if __name__ == "__main__":
    main()
