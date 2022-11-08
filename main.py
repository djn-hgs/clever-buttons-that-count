import tkinter as tk
import functools as ft


class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x300')
        self.my_gui = ButtonFrame(self, 'green')

        self.my_gui.grid(row=1, column=0, sticky='news')
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)


class CleverButton(tk.Button):
    def __init__(self, parent, i, j):
        super().__init__(parent)
        self.i = i
        self.j = j
        self.pressed = 0
        self.configure(text=f'Button {i}, {j}', command=self.do_thing)

    def do_thing(self):
        self.pressed += 1
        self.configure(text=f'Pressed {self.pressed} times')

class ButtonFrame(tk.Frame):
    def __init__(self, parent, color):
        super().__init__(parent)
        self.parent = parent
        self.configure(bg=color)

        self.buttons = [[0,0,0], [0,0,0], [0,0,0]]

        for i in range(3):
            for j in range(3):
                new_button = CleverButton(self, i, j)
                new_button.grid(row=i, column=j, sticky='news')

                self.buttons[i][j] = new_button

        for i in range(3):
            self.rowconfigure(i, weight=1)

        for j in range(3):
            self.columnconfigure(j, weight=1)




one = MyApp()

tk.mainloop()
