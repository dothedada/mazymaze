from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Mazy MAAAZEEEEE!!!")
        self.__canvas = Canvas(master=self.__root, bg="white" width=width, height=height)
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
