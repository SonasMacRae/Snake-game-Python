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


def Render():
    for x in range(10):
        for y in range(10):
            if not board[x][y].isdigit():
                print(" "+board[x][y]+" ", end = "")
            else:
                print(" _ ", end = "")
        print("")


def Move(head, direction):
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
    return head


def Update(head):
    board[head[0]][head[1]] = str(head[1])
    head = Move(head)
    board[head[0]][head[1]] = "h"
    Render()
    return head

def UserUpdate(head):
    direction = input("enter: ")
    while direction != "q":
        board[head[0]][head[1]] = str(head[1])
        head = Move(head,direction)
        board[head[0]][head[1]] = "h"
        Render()
        direction = input("enter: ")
    return head


def SpawnPickup(snake):
    tiles = []
    for x in range(10):
        for y in range(10):
            if board[x][y] != 'h' and board[x][y] != 'p':
                temp = (x, y)
                tiles.append(temp)
    pickup = random.randint(0, len(tiles))
    board[tiles[pickup][0]][tiles[pickup][1]] = "p"


SpawnPickup(snake)
SpawnPickup(snake)
Render()
head = UserUpdate(head)

print(head)
