import random
from constants import *
def create_grid(canvas, width, height, size):
    start = 50
    for i in range(height+1):
        canvas.create_line(start, start + i*size, start + width*size, start + i*size)
    for i in range(width+1):
        canvas.create_line(start + i*size, start, start + i*size, start + height*size)

def create_rect(array, canvas, width, height, size):
    start = 50
    for j in range(height):
        for i in range(width):
            array[j][i] = canvas.create_rectangle(start + i*size, start + j*size, start + (i+1)*size, start + (j+1)*size, fill = "grey")

def add_bomb_list(array, width, height, no_of_bombs):
    for _ in range(no_of_bombs):
        x = random.randint(0, width-1)
        y = random.randint(0, height-1)
        while array[y][x] == True:
            x = random.randint(0, width-1)
            y = random.randint(0, height-1)
        array[y][x] = True

def check(canvas, rect_block, bomb_block, width, height, X, Y):
    start = 50
    if bomb_block[Y][X] == True:
        quit()
    else:
        just_miss_rect(canvas, rect_block, bomb_block, width, height, X, Y)

def just_miss_rect(canvas, rect_block, bomb_block, width, height, X, Y):
    # canvas.create_rectangle(start + X*size, start + Y*size, start + (X+1)*size, start + (Y+1)*size, fill = "pink")
    # canvas.create_text(start + size/2, start + size/2, text = "H")
    temp_list = []
    temp_list.append([X,Y, calculate_bomb(bomb_block, width, height, X, Y)])
    while len(temp_list)!=0:
        tmp = temp_list.pop()
        if tmp[2] == 0:
            canvas.create_rectangle(start + tmp[0]*size, start + tmp[1]*size, start + (tmp[0]+1)*size, start + (tmp[1]+1)*size, fill = "pink")
            canvas.create_text(start + tmp[0]*size + size/2, start + tmp[1]*size + size/2, text = str(tmp[2]))
            add_adjacent(temp_list, bomb_block, width, height, tmp[0], tmp[1])
        else:
            canvas.create_rectangle(start + tmp[0]*size, start + tmp[1]*size, start + (tmp[0]+1)*size, start + (tmp[1]+1)*size, fill = "pink")
            canvas.create_text(start + tmp[0]*size + size/2, start + tmp[1]*size + size/2, text = str(tmp[2]))

def calculate_bomb(bomb_block, width, height, X, Y):
    count = 0
    if X+1<=width-1 and Y+1<=height-1 and bomb_block[X+1][Y+1] == True:
        count += 1
    if X+1<=width-1 and Y<=height-1 and bomb_block[X+1][Y] == True:
        count += 1
    if X<=width-1 and Y+1<=height-1 and bomb_block[X][Y+1] == True:
        count += 1
    if X-1>=0 and Y<=height-1 and bomb_block[X-1][Y] == True:
        count += 1
    if X<=width-1 and Y-1>=0 and bomb_block[X][Y-1] == True:
        count += 1
    if X-1>=0 and Y-1>=0 and bomb_block[X-1][Y-1] == True:
        count += 1
    if X-1>=0 and Y+1<=height-1 and bomb_block[X-1][Y+1] == True:
        count += 1
    if X+1<=width-1 and Y-1>=0 and bomb_block[X+1][Y-1] == True:
        count += 1
    return count

def add_adjacent(temp_list, bomb_block, width, height, X, Y):
    if X+1<=width-1 and Y+1<=height-1:
        temp_list.append([X+1,Y+1, calculate_bomb(bomb_block, width, height, X+1, Y+1)])
    if X+1<=width-1 and Y<=height-1 :
        temp_list.append([X+1,Y, calculate_bomb(bomb_block, width, height, X+1, Y)])
    if X<=width-1 and Y+1<=height-1 :
        temp_list.append([X,Y+1, calculate_bomb(bomb_block, width, height, X, Y+1)])
    if X-1>=0 and Y<=height-1 :
        temp_list.append([X-1,Y, calculate_bomb(bomb_block, width, height, X-1, Y)])
    if X<=width-1 and Y-1>=0 :
        temp_list.append([X,Y-1, calculate_bomb(bomb_block, width, height, X, Y-1)])
    if X-1>=0 and Y-1>=0 :
        temp_list.append([X-1,Y-1, calculate_bomb(bomb_block, width, height, X-1, Y-1)])
    if X-1>=0 and Y+1<=height-1 :
        temp_list.append([X-1,Y+1, calculate_bomb(bomb_block, width, height, X-1, Y+1)])
    if X+1<=width-1 and Y-1>=0 :
        temp_list.append([X+1,Y-1, calculate_bomb(bomb_block, width, height, X+1, Y-1)])
