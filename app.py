import random
import os
import math
import time
import board
import snake



snake = snake.Snake()
board = board.Board()
board.SpawnPickup(snake.body)

def Distance(x, y):
    tempX = abs(x[0] - y[0])
    tempY = abs(x[1] - y[1])
    return (tempX + tempY)

def PathScores(board, snake, destination):
    tiles = []
    for x in range(10):
        tiles.append([])
        for y in range(10):
            tiles[x].append(Distance(destination,(x,y)))
            if(board[x][y] == "b"):
                tiles[x][y] = 999

    controls = ['w','s','a','d']
    scores = []

    head = snake[0]

    if len(snake) > 1:
        tiles[snake[1][0]][snake[1][1]] = 1100

    # up
    upCoord = (head[0] -1, head[1])
    if upCoord[0] < 0:
        scores.append(1000)
    else:
        scores.append(tiles[upCoord[0]][upCoord[1]])

    # down
    downCoord = (head[0] + 1, head[1])
    if downCoord[0] > 9:
        scores.append(1000)
    else:
        scores.append(tiles[downCoord[0]][downCoord[1]])

    # left
    leftCoord = (head[0], head[1] - 1)
    if leftCoord[1] < 0:
        scores.append(1000)
    else:
        scores.append(tiles[leftCoord[0]][leftCoord[1]])

    # right
    rightCoord = (head[0], head[1] + 1)
    if rightCoord[1] > 9:
        scores.append(1000)
    else:
        scores.append(tiles[rightCoord[0]][rightCoord[1]])

    minScore = min(scores)
    index = scores.index(minScore)
    print(scores)
    return controls[index]

def Bot(board, snake):
    direction = "w"

    head = snake.head
    destination = (0,0)
    destination = board.pickup
    flag = True
    while flag:

        destination = board.pickup
        flag = snake.Move(PathScores(board.board, snake.body, destination), board)
        head = snake.head

        os.system('cls||clear')
        board.Render(snake)

        time.sleep(0.5)

def UserUpdate(board, snake):
    flag = True
    direction = "w"
    board.Render(snake)
    controls = ['w','a','s','d','q']
    while direction != "q" and flag:
        direction = input("move: ")
        if direction not in controls:
            continue
        flag = snake.Move(direction, board)

        os.system('cls||clear')
        board.Render(snake)


Bot(board,snake)
print("Game Over!")
