from graphics import Window, Point, Line


def main():
    win = Window(600, 800)

    win.draw_line(Line(Point(10, 10), Point(100, 10)))
    win.draw_line(Line(Point(100, 10), Point(100, 100)))
    win.draw_line(Line(Point(100, 100), Point(10, 100)))
    win.draw_line(Line(Point(10, 100), Point(10, 10)), "black")

    win.wait_for_close()


if __name__ == "__main__":
    main()
