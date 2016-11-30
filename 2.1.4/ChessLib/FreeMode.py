# -*- coding: cp936 -*- 
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
        for i in range(11):
            for j in range(10):
                print [self.state_no[i][j], self.state_kind[i][j]],
            print
        print


class appArb:
    def __init__(self, root):
        a = 60
        b = 80
        l = 50
        self.choose = False
        self.choosed_chess = False
        self.xing_qi = True
        self.root = root
        self.Board = Board(root, a, b, l)
        self.front_display()
        self.Board.canvas.bind('<Button-1>', self.move)

    def front_display(self):
        a = self.Board.width
        b = self.Board.height
        l = self.Board.l
        winTitle = u'\u4E2D\u56FD\u8C61\u68CB'
        self.root.title(winTitle)  # 中国象棋
        self.root.geometry(str(a * 2 + l * 8 + 200) + 'x' + str(b * 2 + l * 9) + '+500+100')
        self.root.resizable(width=False, height=False)  # 使界面长宽不可变

    def run(self):
        self.root.mainloop()

    def move(self, event):
        a = self.Board.width
        b = self.Board.height
        l = self.Board.l
        x = (event.x - a + l / 2) / l  # 将点击处的像素坐标转化为棋盘坐标
        if x <= 8:
            y = (event.y - b + l / 2) / l
        else:
            y = (event.y - b + l) / l

        if x < 0 or y < 0 or x > 10 or y > 9:  # 点击位置超出棋盘，退出该函数
            return
        if x > 8 and (y < 2 or y > 8):
            return
        if not self.choose:
            if x > 8:
                self.choosed_chess = self.Board.chess[7 * (x - 9) + (y - 2)]  # 选中棋子
                self.choosed_chess.choose()
                self.choose = True
        if self.choose and x > 8 and (self.choosed_chess.No != 7 * (x - 9) + (y - 2)):  # 有选中的棋子,并且再次点击位置与棋子位置不同
            another_chess = self.Board.chess[7 * (x - 9) + (y - 2)]
            self.choosed_chess.not_choose()
            self.choosed_chess = another_chess
            self.choosed_chess.choose()
        if self.choose and x < 9:  # 选中棋子，并且移到棋盘内
            self.choosed_chess.canvas.move(self.choosed_chess.oval, (x - self.choosed_chess.x) * self.choosed_chess.l,
                                           (y - self.choosed_chess.y - 0.5) * self.choosed_chess.l)  # 移动选中的棋子
            self.choosed_chess.canvas.move(self.choosed_chess.word, (x - self.choosed_chess.x) * self.choosed_chess.l,
                                           (y - self.choosed_chess.y - 0.5) * self.choosed_chess.l)
            self.choosed_chess.not_choose()
            self.choose = False  # 移动后取消对该棋子的选中
            self.choosed_chess.pack(self.choosed_chess.y, self.choosed_chess.No)
            return


class Board:
    def __init__(self, master, width, height, l):
        self.width = width
        self.height = height
        self.l = l
        self.master = master
        self.canvas = Canvas(self.master, width=self.width * 2 + self.l * 8 + 200, height=self.height * 2 + self.l * 9,
                             bg='white')
        self.canvas.place(x=0, y=0)
        self.state = BoardState()
        self.chess = []
        self.location = [
            1,  # 将
            2,  # 仕
            3,  # 象
            4,  # 马
            5,  # 车
            6,  # 炮
            7,  # 卒
            1,  # 帅
            2,  # 士
            3,  # 相
            4,  # 马
            5,  # 车
            6,  # 炮
            7,  # 兵
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
            self.chess += [CHESS(self.canvas, kind, self)]
            self.chess[kind].pack(self.location[kind], kind)


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

    def pack(self, y, No):
        if self.kind < 7:
            self.oval = self.canvas.create_oval( \
                self.a + 9 * self.l - self.r, self.b + y * self.l - self.r + 0.5 * self.l, \
                self.a + 9 * self.l + self.r, self.b + y * self.l + self.r + 0.5 * self.l, \
                fill='white', width=4)
            self.word = self.canvas.create_text( \
                self.a + 9 * self.l, self.b + y * self.l + 0.5 * self.l, \
                text=self.name, \
                font=0)
            self.x = 9
        else:
            self.oval = self.canvas.create_oval( \
                self.a + 10 * self.l - self.r, self.b + y * self.l - self.r + 0.5 * self.l, \
                self.a + 10 * self.l + self.r, self.b + y * self.l + self.r + 0.5 * self.l, \
                fill='white', outline='red', width=4)
            self.word = self.canvas.create_text( \
                self.a + 10 * self.l, self.b + y * self.l + 0.5 * self.l, \
                text=self.name, \
                fill='red', font=0)
            self.x = 10
        self.y = y
        self.No = No

    def choose(self):
        if self.x <= 8:
            self.mark1 = self.canvas.create_line( \
                self.a + self.x * self.l - self.l * 3 / 8, self.b + self.y * self.l - self.l / 2, \
                self.a + self.x * self.l - self.l / 2, self.b + self.y * self.l - self.l / 2, \
                self.a + self.x * self.l - self.l / 2, self.b + self.y * self.l - self.l * 3 / 8)
            self.mark2 = self.canvas.create_line( \
                self.a + self.x * self.l + self.l * 3 / 8, self.b + self.y * self.l - self.l / 2, \
                self.a + self.x * self.l + self.l / 2, self.b + self.y * self.l - self.l / 2, \
                self.a + self.x * self.l + self.l / 2, self.b + self.y * self.l - self.l * 3 / 8)
            self.mark3 = self.canvas.create_line( \
                self.a + self.x * self.l + self.l * 3 / 8, self.b + self.y * self.l + self.l / 2, \
                self.a + self.x * self.l + self.l / 2, self.b + self.y * self.l + self.l / 2, \
                self.a + self.x * self.l + self.l / 2, self.b + self.y * self.l + self.l * 3 / 8)
            self.mark4 = self.canvas.create_line( \
                self.a + self.x * self.l - self.l * 3 / 8, self.b + self.y * self.l + self.l / 2, \
                self.a + self.x * self.l - self.l / 2, self.b + self.y * self.l + self.l / 2, \
                self.a + self.x * self.l - self.l / 2, self.b + self.y * self.l + self.l * 3 / 8)
        else:
            self.mark1 = self.canvas.create_line( \
                self.a + self.x * self.l - self.l * 3 / 8, self.b + self.y * self.l - self.l / 2 + 0.5 * self.l, \
                self.a + self.x * self.l - self.l / 2, self.b + self.y * self.l - self.l / 2 + 0.5 * self.l, \
                self.a + self.x * self.l - self.l / 2, self.b + self.y * self.l - self.l * 3 / 8 + 0.5 * self.l)
            self.mark2 = self.canvas.create_line( \
                self.a + self.x * self.l + self.l * 3 / 8, self.b + self.y * self.l - self.l / 2 + 0.5 * self.l, \
                self.a + self.x * self.l + self.l / 2, self.b + self.y * self.l - self.l / 2 + 0.5 * self.l, \
                self.a + self.x * self.l + self.l / 2, self.b + self.y * self.l - self.l * 3 / 8 + 0.5 * self.l)
            self.mark3 = self.canvas.create_line( \
                self.a + self.x * self.l + self.l * 3 / 8, self.b + self.y * self.l + self.l / 2 + 0.5 * self.l, \
                self.a + self.x * self.l + self.l / 2, self.b + self.y * self.l + self.l / 2 + 0.5 * self.l, \
                self.a + self.x * self.l + self.l / 2, self.b + self.y * self.l + self.l * 3 / 8 + 0.5 * self.l)
            self.mark4 = self.canvas.create_line( \
                self.a + self.x * self.l - self.l * 3 / 8, self.b + self.y * self.l + self.l / 2 + 0.5 * self.l, \
                self.a + self.x * self.l - self.l / 2, self.b + self.y * self.l + self.l / 2 + 0.5 * self.l, \
                self.a + self.x * self.l - self.l / 2, self.b + self.y * self.l + self.l * 3 / 8 + 0.5 * self.l)

    def not_choose(self):
        self.canvas.delete(self.mark1)
        self.canvas.delete(self.mark2)
        self.canvas.delete(self.mark3)
        self.canvas.delete(self.mark4)


def main():
    root = Tk()
    ChineseChess = appArb(root)
    ChineseChess.run()
