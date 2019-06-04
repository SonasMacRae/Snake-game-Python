import random
import os
import math
import time
import board as Board


class Snake:
    body = []
    head = (0,0)

    def __init__(self):
        self.head = (random.randint(0, 9), random.randint(0, 9))
        self.body.append(self.head)

    def Move(self, direction, board):
        head = self.body[0]
        neck = 0

        if len(self.body) > 1:
            neck = self.body[1]

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
            return True
        self.head = head

        if board.board[head[0]][head[1]] == "b" and head != self.body[-1]:
            return False

        if head == board.pickup:
            self.body = self.body[::-1]
            self.body.append(head)
            self.body = self.body[::-1]

            board.SpawnPickup(self.body)
            #global score
            #score = score + 1

        else:
            self.body = self.body[::-1]
            self.body.append(head)
            self.body = self.body[::-1]
            self.body.pop()

        return True
