import time
from cell import Cell
from graphics import Point
import random


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
        seed=None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._rows = rows
        self._cols = cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom = False
        self._draw_cell(self._cols - 1, self._rows - 1)

    def __neighbors(self, i, j):
        return [
            ("top", i, j + -1, "bottom"),
            ("right", i + 1, j, "left"),
            ("bottom", i, j + 1, "top"),
            ("left", i + -1, j, "right"),
        ]

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            directions = []
            for neighbor in self.__neighbors(i, j):
                if (
                    0 <= neighbor[1] < self._cols
                    and 0 <= neighbor[2] < self._rows
                    and not self._cells[neighbor[1]][neighbor[2]].visited
                ):
                    directions.append(neighbor)
            if len(directions) == 0:
                return
            next = directions[random.randrange(0, len(directions))]

            setattr(self._cells[i][j], f"has_{next[0]}", False)
            setattr(self._cells[next[1]][next[2]], f"has_{next[3]}", False)
            self._draw_cell(i, j)
            self._break_walls_r(next[1], next[2])

    def _reset_cells_visited(self):
        for i in range(self._cols):
            for j in range(self._rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        current = self._cells[i][j]
        current.visited = True
        if i == self._cols - 1 and j == self._rows - 1:
            return True
        neighbors = self.__neighbors(i, j)
        for neighbor in neighbors:
            if (
                0 <= neighbor[1] < self._cols
                and 0 <= neighbor[2] < self._rows
                and not getattr(current, f"has_{neighbor[0]}")
                and not self._cells[neighbor[1]][neighbor[2]].visited
            ):
                current.draw_move(self._cells[neighbor[1]][neighbor[2]])
                if self._solve_r(neighbor[1], neighbor[2]):
                    return True
                else:
                    current.draw_move(self._cells[neighbor[1]][neighbor[2]], undo=True)
        return False
