## Source: https://stackoverflow.com/questions/22925599/mouse-position-python-tkinter
import tkinter as tk
root = tk.Tk()

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

root.bind('<Motion>', motion)
root.mainloop()
