import time
from cell import Cell
from graphics import Point


class Maze:
    def __init__(
        self,
        x1,
        y1,
        rows,
        cols,
        cell_size_x,
        cell_size_y,
        window=None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._rows = rows
        self._cols = cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        self._create_cells()

    def _create_cells(self):
        for i in range(self._cols):
            self._cells.append([])
            for j in range(self._rows):
                self._cells[i].append(Cell(self._window))

        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        cell_x = self._x1 + self._cell_size_x * i
        cell_y = self._y1 + self._cell_size_y * j
        self._cells[i][j].draw(
            Point(cell_x, cell_y),
            Point(cell_x + self._cell_size_x, cell_y + self._cell_size_y),
        )
        self._animate()

    def _animate(self):
        if self._window is None:
            return

        self._window.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top = False
        self._cells[0][0].has_left = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom = False
        self._cells[-1][-1].has_right = False
        self._draw_cell(self._cols - 1, self._rows - 1)
