from graphics import Window
from maze import Maze


def main():
    rows = 5
    cols = 5
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = 20
    cell_size_y = 20
    # cell_size_x = (screen_x - 2 * margin) / cols
    # cell_size_y = (screen_y - 2 * margin) / rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, rows, cols, cell_size_x, cell_size_y, win)
    maze.solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()
