# -*- coding: utf-8 -*-
from Tkinter import *

name = [
    u'\u5C06',  # 将
    u'\u4ED5',  # 仕
    u'\u8C61',  # 象
    u'\u9A6C',  # 马
    u'\u8F66',  # 车
    u'\u70AE',  # 炮
    u'\u5352',  # 卒
    u'\u5E05',  # 帅
    u'\u58EB',  # 士
    u'\u76F8',  # 相
    u'\u9A6C',  # 马
    u'\u8F66',  # 车
    u'\u70AE',  # 炮
    u'\u5175',  # 兵
]


class BoardState:
    def __init__(self):
        self.state_no = [
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        ]
        self.state_kind = [
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        ]

    def __getitem__(self, (x, y)):
        return [self.state_no[x][y], self.state_kind[x][y]]

    def __setitem__(self, (x, y), (no, kind)):
        self.state_no[x][y] = no
        self.state_kind[x][y] = kind

    def print_state(self):
        for i in range(9):
            for j in range(10):
                print [self.state_no[i][j], self.state_kind[i][j]],
            print
        print


class Board:
    def __init__(self, master, width, height, l):
        self.width = width
        self.height = height
        self.l = l
        self.master = master
        self.canvas = Canvas(self.master, width=self.width * 2 + self.l * 8, height=self.height * 2 + self.l * 9,
                             bg='white')
        self.canvas.place(x=0, y=0)
        self.state = BoardState()
        self.chess = []
        self.location = [
            (4, 0),  # 将
            (5, 0), (3, 0),  # 仕
            (6, 0), (2, 0),  # 象
            (7, 0), (1, 0),  # 马
            (8, 0), (0, 0),  # 车
            (7, 2), (1, 2),  # 炮
            (8, 3), (6, 3), (4, 3), (2, 3), (0, 3),  # 卒
            (4, 9),  # 帅
            (5, 9), (3, 9),  # 士
            (6, 9), (2, 9),  # 相
            (7, 9), (1, 9),  # 马
            (8, 9), (0, 9),  # 车
            (7, 7), (1, 7),  # 炮
            (8, 6), (6, 6), (4, 6), (2, 6), (0, 6)  # 兵
        ]
        self.numbers = [1, 2, 2, 2, 2, 2, 5, 1, 2, 2, 2, 2, 2, 5]
        self.display()

    def display(self):
        self.paint_board()
        self.put_chess()

    def paint_board(self):
        a = self.width
        b = self.height
        l = self.l
        c = self.canvas

        for i in range(1, 9):  # 横线
            c.create_line(a, b + i * l, a + 8 * l, b + i * l)
        for i in range(1, 8):  # 竖线
            c.create_line(a + i * l, b, a + i * l, b + 4 * l)
            c.create_line(a + i * l, b + 5 * l, a + i * l, b + 9 * l)

        c.create_line(a, b + 0 * l, a + 8 * l, b + 0 * l, width=3)  # 边界线加粗
        c.create_line(a, b + 9 * l, a + 8 * l, b + 9 * l, width=3)
        c.create_line(a + 0 * l, b, a + 0 * l, b + 9 * l, width=3)
        c.create_line(a + 8 * l, b, a + 8 * l, b + 9 * l, width=3)

        c.create_line(a + 3 * l, b, a + 5 * l, b + 2 * l)  # 九宫格内交叉线
        c.create_line(a + 5 * l, b, a + 3 * l, b + 2 * l)
        c.create_line(a + 3 * l, b + 7 * l, a + 5 * l, b + 9 * l)
        c.create_line(a + 5 * l, b + 7 * l, a + 3 * l, b + 9 * l)

        for i in [1, 7]:  # 炮台与兵卒位
            for j in [2, 7]:
                c.create_line(a + i * l - 4, b + j * l - l / 3, a + i * l - 4, b + j * l - 4, a + i * l - l / 3,
                              b + j * l - 4)
                c.create_line(a + i * l - 4, b + j * l + l / 3, a + i * l - 4, b + j * l + 4, a + i * l - l / 3,
                              b + j * l + 4)
                c.create_line(a + i * l + 4, b + j * l - l / 3, a + i * l + 4, b + j * l - 4, a + i * l + l / 3,
                              b + j * l - 4)
                c.create_line(a + i * l + 4, b + j * l + l / 3, a + i * l + 4, b + j * l + 4, a + i * l + l / 3,
                              b + j * l + 4)

        for i in [0, 2, 4, 6, 8]:  # 兵卒位
            for j in [3, 6]:
                if i != 0:
                    c.create_line(a + i * l - 4, b + j * l - l / 3, a + i * l - 4, b + j * l - 4, a + i * l - l / 3,
                                  b + j * l - 4)
                    c.create_line(a + i * l - 4, b + j * l + l / 3, a + i * l - 4, b + j * l + 4, a + i * l - l / 3,
                                  b + j * l + 4)
                if i != 8:
                    c.create_line(a + i * l + 4, b + j * l - l / 3, a + i * l + 4, b + j * l - 4, a + i * l + l / 3,
                                  b + j * l - 4)
                    c.create_line(a + i * l + 4, b + j * l + l / 3, a + i * l + 4, b + j * l + 4, a + i * l + l / 3,
                                  b + j * l + 4)

    def put_chess(self):
        for kind in range(14):
            for j in range(self.numbers[kind]):
                self.chess += [CHESS(self.canvas, kind, self)]

        for i in range(32):
            self.chess[i].pack(self.location[i], i)
            self.state.state_no[self.location[i][0]][self.location[i][1]] = self.chess[i].No
            self.state.state_kind[self.location[i][0]][self.location[i][1]] = self.chess[i].kind


class CHESS:  # 棋子属性
    def __init__(self, canvas, kind, master):
        self.canvas = canvas
        self.kind = kind
        self.name = name[kind]
        self.a = master.width
        self.b = master.height
        self.l = master.l
        self.r = 7 * self.l / 16
        self.x = self.y = -1
        self.No = -1

    def pack(self, (x, y), No):
        if self.kind < 7:
            self.oval = self.canvas.create_oval(
                self.a + x * self.l - self.r, self.b + y * self.l - self.r,
                self.a + x * self.l + self.r, self.b + y * self.l + self.r,
                fill='white', width=4)
            self.word = self.canvas.create_text(
                self.a + x * self.l, self.b + y * self.l,
                text=self.name,
                font=0)
        else:
            self.oval = self.canvas.create_oval(
                self.a + x * self.l - self.r, self.b + y * self.l - self.r,
                self.a + x * self.l + self.r, self.b + y * self.l + self.r,
                fill='white', outline='red', width=4)
            self.word = self.canvas.create_text(
                self.a + x * self.l, self.b + y * self.l,
                text=self.name,
                fill='red', font=0)
        self.x = x
        self.y = y
        self.No = No

    def choose(self):
        self.mark1 = self.canvas.create_line(
            self.a + self.x * self.l - self.l * 3 / 8, self.b + self.y * self.l - self.l / 2,
            self.a + self.x * self.l - self.l / 2, self.b + self.y * self.l - self.l / 2,
            self.a + self.x * self.l - self.l / 2, self.b + self.y * self.l - self.l * 3 / 8)
        self.mark2 = self.canvas.create_line(
            self.a + self.x * self.l + self.l * 3 / 8, self.b + self.y * self.l - self.l / 2,
            self.a + self.x * self.l + self.l / 2, self.b + self.y * self.l - self.l / 2,
            self.a + self.x * self.l + self.l / 2, self.b + self.y * self.l - self.l * 3 / 8)
        self.mark3 = self.canvas.create_line(
            self.a + self.x * self.l + self.l * 3 / 8, self.b + self.y * self.l + self.l / 2,
            self.a + self.x * self.l + self.l / 2, self.b + self.y * self.l + self.l / 2,
            self.a + self.x * self.l + self.l / 2, self.b + self.y * self.l + self.l * 3 / 8)
        self.mark4 = self.canvas.create_line(
            self.a + self.x * self.l - self.l * 3 / 8, self.b + self.y * self.l + self.l / 2,
            self.a + self.x * self.l - self.l / 2, self.b + self.y * self.l + self.l / 2,
            self.a + self.x * self.l - self.l / 2, self.b + self.y * self.l + self.l * 3 / 8)

    def not_choose(self):
        self.canvas.delete(self.mark1)
        self.canvas.delete(self.mark2)
        self.canvas.delete(self.mark3)
        self.canvas.delete(self.mark4)
