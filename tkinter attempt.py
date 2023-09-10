# GAME ENVIRONMENT
from tkinter import *
from PIL import Image, ImageTk
root = Tk()

root.title("PACMAN")
root.iconbitmap('C:/Users/munee/Desktop/FINAL PROJECT/Pacman.ico')
root.geometry('750x700+400+50')
root.resizable(False, False)
# MAIN MENU FILE
MYMAP = [
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', 'x', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', ' ', 'x'],
    ['x', ' ', 'x', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', 'x', ' ', 'x'],
    ['x', ' ', 'x', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', 'x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', 'x', 'x', 'x', 'x'],
    [' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' '],
    [' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', 'x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' '],
    ['x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 'x', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', 'x', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', ' ', 'x'],
    ['x', ' ', 'x', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', 'x', ' ', 'x'],
    ['x', ' ', 'x', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

]

MAP = Canvas(root, height=800, width=800, relief=SUNKEN, borderwidth=3)
MAP.pack()

# Loads and create image (put the image in the folder)
img = Image.open('PACMAN.png')
rimg = img.resize((50,50))
nimg = ImageTk.PhotoImage(rimg)
Pacman = MAP.create_image(10, 10, anchor = NW, image=nimg)


def move(event):
    print('key pressed was: ', event.char)
    """Move the sprite image with a d w and s when click them"""
    if event.char == 'a' or event.char == 'A':
        MAP.configure(image = nimg)
        MAP.move(Pacman, -10, 0)
    elif event.char == "d" or event.char == 'D':
        MAP.move(Pacman, 10, 0)
    elif event.char == "w" or event.char == 'W':
        MAP.move(Pacman, 0, -10)
    elif event.char == "s" or event.char == 'S':
        MAP.move(Pacman, 0, 10)


# This bind window to keys so that move is called when you press a key
root.bind("<Key>", move)

root.mainloop()
