import random
import os
import math
import time

board = []
snake = []
head = (0,0)


def Init():
    for x in range(10):
        board.append([])
        for y in range(10):
            board[x].append(str(y))
    head = (random.randint(0, 9), random.randint(0, 9))
    board[head[0]][head[1]] = "h"
    snake.append(head)
    return head


head = Init()


def Render(board):
    for x in range(10):
        for y in range(10):
            if not board[x][y].isdigit():
                print(" "+board[x][y]+" ", end = "")
            else:
                print(" _ ", end = "")
        print("")
    print("Score: ", score)


def Move(snake, direction, board):
    head = snake[0]
    neck = 0

    if len(snake) > 1:
        neck = snake[1]

    if direction == "a":
        head = (head[0], head[1] - 1)
        if head[1] < 0:
            head = (head[0], 9)

    if direction == "w":
        head = (head[0] -1, head[1])
        if head[0] < 0:
            head = (9, head[1])

    if direction == "d":
        head = (head[0], head[1] + 1)
        if head[1] > 9:
            head = (head[0], 0)

    if direction == "s":
        head = (head[0] + 1, head[1])
        if head[0] > 9:
            head = (0, head[1])

    if head == neck:
        return snake

    if board[head[0]][head[1]] == "b" and head != snake[-1]:
        snake = "Q"
        return snake

    if board[head[0]][head[1]] == "p":
        snake = snake[::-1]
        snake.append(head)
        snake = snake[::-1]
        SpawnPickup(snake)
        global score
        score = score + 1

    else:
        snake = snake[::-1]
        snake.append(head)
        snake = snake[::-1]
        snake.pop()

    return snake


def Update(head):
    board[head[0]][head[1]] = str(head[1])
    head = Move(head)
    board[head[0]][head[1]] = "h"
    Render(board)
    return head


def UserUpdate(board, snake):
    direction = "w"
    controls = ['w','a','s','d','q']
    head = snake[0]
    while direction != "q":
        direction = input("enter: ")
        if direction not in controls:
            continue
        snake = Move(snake, direction, board)
        head = snake[0]

        if snake == "Q":
            print("game over")
            return

        for x in range(10):
            for y in range(10):
                if(board[x][y] != "p"):
                    board[x][y] = str(y)

        for b in snake:
            board[b[0]][b[1]] = "b"

        board[head[0]][head[1]] = "h"

        os.system('cls||clear')
        Render(board)


    print("Thank you for playing, goodbye!")


def FindPickup(board):
    for x in range(10):
        for y in range(10):
            if(board[x][y] == "p"):
                return (x,y)


def Bot(board, snake):
    direction = "w"

    head = snake[0]
    destination = (0,0)
    destination = FindPickup(board)

    while direction != "q":

        destination = FindPickup(board)
        snake = Move(snake, PathScores(board, snake, destination), board)
        head = snake[0]

        if snake == "Q":
            print("game over")
            return

        for x in range(10):
            for y in range(10):
                if(board[x][y] != "p"):
                    board[x][y] = str(y)

        for b in snake:
            board[b[0]][b[1]] = "b"

        board[head[0]][head[1]] = "h"

        os.system('cls||clear')
        Render(board)

        time.sleep(0.25)

    print("Thank you for playing, goodbye!")


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


def SpawnPickup(snake):
    tiles = []
    for x in range(10):
        for y in range(10):
            if board[x][y] != 'h' and board[x][y] != 'b':
                temp = (x, y)
                tiles.append(temp)
    pickup = random.randint(0, len(tiles) - 1)
    board[tiles[pickup][0]][tiles[pickup][1]] = "p"


score = 0
SpawnPickup(snake)
Render(board)
Bot(board, snake)
# UserUpdate(board,snake)
print(head)
