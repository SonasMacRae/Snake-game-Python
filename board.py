import random
import os
import math
import time
import snake as Snake


class Board:

    board = []
    pickup = (0,0)

    def __init__(self):
        self.CleanBoard()
        self.pickup = (0,0)

    def CleanBoard(self):
        self.board = []
        for x in range(10):
            self.board.append([])
            for y in range(10):
                self.board[x].append(str(y))

    def Render(self, snake):
        self.CleanBoard()

        for x in snake.body:
            self.board[x[0]][x[1]] = "b"

        self.board[snake.head[0]][snake.head[1]] = "h"
        self.board[self.pickup[0]][self.pickup[1]] = "p"

        for x in range(10):
            for y in range(10):
                if not self.board[x][y].isdigit():
                    print(" " + self.board[x][y] + " ", end = "")
                else:
                    print(" _ ", end = "")
            print("")

    def SpawnPickup(self, snake):
        tiles = []
        for x in range(10):
            for y in range(10):
                if self.board[x][y] != 'h' and self.board[x][y] != 'b':
                    temp = (x, y)
                    tiles.append(temp)
        temp = random.randint(0, len(tiles) - 1)
        self.pickup = tiles[temp]
