import random


direction = "w"
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
print(head)


def Render():
    for x in range(10):
        for y in range(10):
            if not board[x][y].isdigit():
                print(board[x][y], end="")
            else:
                print("_", end="")
        print("")


def Move(head):
    if direction == "a":
        head = (head[0], head[1] -1)
        if head[1] < 0:
            head = (head[0], 9)

    if direction == "w":
        head = (head[0] -1, head[1])
        if head[0] < 0:
            head = (9, head[1])

    if direction == "d":
        head = (head[0], head[1] +1)
        if head[1] > 9:
            head = (head[0], 0)

    if direction == "s":
        head = (head[0] +1, head[1])
        if head[0] > 9:
            head = (0, head[1])
    return head


def Update(head):
    board[head[0]][head[1]] = str(head[1])
    head = Move(head)
    board[head[0]][head[1]] = "h"
    Render()
    return head

def SpawnPickup(snake):
    tiles = []
    for x in range(10):
        for y in range(10):
            if board[x][y] != 'h':
                temp = (x + 1, y)
                tiles.append(temp)
    print(tiles)




head = Update(head)
SpawnPickup(snake)
