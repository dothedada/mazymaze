from colors import WALLS, BKG, UNDO_PATH, PATH
from graphics import Point, Line


class Cell:
    def __init__(self, window=None):
        self._start = None
        self._end = None
        self.has_top = True
        self.has_right = True
        self.has_bottom = True
        self.has_left = True
        self._window = window
        self.visited = False

    @property
    def _walls(self):
        return {
            "top": (self._start.x, self._start.y, self._end.x, self._start.y),
            "right": (self._end.x, self._start.y, self._end.x, self._end.y),
            "bottom": (self._end.x, self._end.y, self._start.x, self._end.y),
            "left": (self._start.x, self._end.y, self._start.x, self._start.y),
        }

    @property
    def center(self):
        return {
            "x": self._start.x + (self._end.x - self._start.x) / 2,
            "y": self._start.y + (self._end.y - self._start.y) / 2,
        }

    def draw(self, start, end, color=WALLS, width=2):
        if self._window is None:
            return

        if not isinstance(start, Point) or not isinstance(end, Point):
            raise TypeError("Must be a valid Point Class")

        self._start = start
        self._end = end

        for wall, cords in self._walls.items():
            self._window.draw_line(
                Line(Point(*cords[:2]), Point(*cords[2:])),
                fill_color=color if getattr(self, f"has_{wall}") else BKG,
                width=width,
            )

    def draw_move(self, to_cell, undo=False):
        color = PATH if not undo else UNDO_PATH
        self._window.draw_line(
            Line(
                Point(self.center["x"], self.center["y"]),
                Point(to_cell.center["x"], to_cell.center["y"]),
            ),
            fill_color=color,
        )
