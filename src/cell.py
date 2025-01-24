from graphics import Point, Line


class Cell:
    def __init__(self, window):
        self._start = None
        self._end = None
        self.has_top = True
        self.has_right = True
        self.has_bottom = True
        self.has_left = True
        self.window = window

    @property
    def walls(self):
        return {
            "top": (self._start.x, self._start.y, self._end.x, self._start.y),
            "right": (self._end.x, self._start.y, self._end.x, self._end.y),
            "bottom": (self._end.x, self._end.y, self._start.x, self._end.y),
            "left": (self._start.x, self._end.y, self._start.x, self._start.y),
        }

    def draw(self, start, end, color="red", width=2):
        if not isinstance(start, Point) or not isinstance(end, Point):
            raise TypeError("Must be a valid Point Class")
        self._start = start
        self._end = end

        for wall, cords in self.walls.items():
            if getattr(self, f"has_{wall}"):
                self.window.draw_line(
                    Line(Point(*cords[:2]), Point(*cords[2:])),
                    fill_color=color,
                    width=width,
                )
