from tkinter import Tk, Canvas  # add => BOTH later


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Mazy MAAAZEEEEE!!!")
        self.__canvas = Canvas(
            master=self.__root,
            bg="white",
            width=width,
            height=height,
        )
        self.__canvas.pack()
        self.__is_active = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_active = True
        self.__root.mainloop()
        # while self.__is_active:
        #     self.redraw()
        print("window is closed...")

    def close(self):
        self.__is_active = False
        self.__root.destroy()

    def draw_line(self, line, fill_color="red", width=2):
        if not isinstance(line, Line):
            raise TypeError("Line param must be a valid Line class instance")

        line.draw(self.__canvas, fill_color, width)


class Point:
    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both params must be a real number")

        self.x = x
        self.y = y


class Line:
    def __init__(self, point_a, point_b):
        if not isinstance(point_a, Point) or not isinstance(point_b, Point):
            raise TypeError("Both params must be valid Point instances")

        self.point_a = point_a
        self.point_b = point_b

    def draw(self, canvas, fill_color, width):
        canvas.create_line(
            self.point_a.x,
            self.point_a.y,
            self.point_b.x,
            self.point_b.y,
            fill=fill_color,
            width=width,
        )
