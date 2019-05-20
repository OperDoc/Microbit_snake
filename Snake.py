import microbit
import time
import random
def arrPrint(arrForPrint):
    for i in range(5):
        for j in range(5):
            microbit.display.set_pixel(j, i, arrForPrint[i][j])

def makeDir(word):
    if word == 'a':
        return 1
    if word == 'd':
        return -1
    return 0

def snakePrint(arrForPrint, snake, head, mark):
    for i in range(len(arrForPrint)):
        arrForPrint[i] = [0] * 5
    for i in snake:
        arrForPrint[i[0]][i[1]] = 7
    arrForPrint[mark[0]][mark[1]] = 5
    arrForPrint[head[0]][head[1]] = 9


def go(segm, dir):
    if dir == 0:
        segm[0] = (segm[0] - 1) % 5
    if dir == 1:
        segm[1] = (segm[1] - 1) % 5
    if dir == 2:
        segm[0] = (segm[0] + 1) % 5
    if dir == 3:
        segm[1] = (segm[1] + 1) % 5
    oldDir = segm[2]
    segm[2] = dir
    return oldDir

def collision(snake):
    fild = [[0] * 5 for i in range(5)]
    for i in snake:
        if fild[i[0]][i[1]] == 1:
            return False
        fild[i[0]][i[1]] = 1
    return True

def went(sanke, dir):
    for i in range(len(snake)):
        dir = go(snake[i], dir)

def nextTar(tar, arr):
    while arr[tar[0]][tar[1]] != 0:
        tar[0] = random.randint(0, 4)
        tar[1] = random.randint(0, 4)

arr = [[0] * 5 for i in range(5)]
snake = [[0, 2, 0], [1, 2, 0], [2, 2, 0]]
head = [0, 2, 0]
mark = [0, 0]
dir = 0
run = True

while True:
    while run:
        snakePrint(arr, snake, head, mark)
        arrPrint(arr)
        cnt = 0
        for i in range(10):
            if microbit.button_b.is_pressed():
                cnt = -1
            if microbit.button_a.is_pressed():
                cnt = 1
            time.sleep(.1)
        dir =  (dir + cnt) % 4
        x = snake[len(snake) - 1][0]
        y = snake[len(snake) - 1][1]
        z = snake[len(snake) - 1][2]
        tale = [x, y, z]
        went(snake, dir)
        go(head, dir)
        if head[0] == mark[0] and head[1] == mark[1]:
            snake.append(tale)
            nextTar(mark, arr)
        run = collision(snake)
    microbit.display.show(microbit.Image.SAD)
    while not run:
        A = microbit.button_a.is_pressed()
        B = microbit.button_b.is_pressed()
        run = run or A or B
    arr = [[0] * 5 for i in range(5)]
    snake = [[0, 2, 0], [1, 2, 0], [2, 2, 0]]
    head = [0, 2, 0]
    mark = [0, 0]
    dir = 0