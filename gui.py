import tkinter as tk
from function import *

width = 600
height = 600
x_edge = 10
y_edge = 10
size = 20
start = 50
no_of_bombs = 1
rect_block = [[None for _ in range(x_edge)] for _ in range(y_edge)]
bomb_block = [[None for _ in range(x_edge)] for _ in range(y_edge)]

root = tk.Tk()
canvas = tk.Canvas(root, width = width, height = height)

def add_bomb(event):
    X = (event.x - start)//size
    Y = (event.y - start)//size
    if X<=19 and X>=0 and Y>=0 and Y<=19:
            canvas.create_oval(start + X*size, start + Y*size, start + (X+1)*size, start + (Y+1)*size, fill = "red")
            bomb_block[Y][X] = True
    print ("clicked at", X, Y)

def click_block(event):
    X = (event.x - start)//size
    Y = (event.y - start)//size
    if X<=19 and X>=0 and Y>=0 and Y<=19:
        check(canvas, rect_block, bomb_block, x_edge, y_edge, X, Y)
    print ("clicked at", X, Y)

add_bomb_list(bomb_block, x_edge, y_edge, no_of_bombs)
# print(bomb_block)
create_rect(rect_block, canvas, x_edge, y_edge, size)
# canvas.create_text(start + size/2, start + size/2, text = "H")
for i in range(y_edge):
    for j in range(x_edge):
        canvas.tag_bind(rect_block[j][i], "<Button-1>", click_block)
# canvas.bind("<Button-1>", click_block)
canvas.pack()
tk.mainloop()
