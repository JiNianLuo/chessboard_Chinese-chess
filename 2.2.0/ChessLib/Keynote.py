# -*- coding: utf-8 -*-
from Tkinter import *
from tkFileDialog import askopenfilename
from tkMessageBox import askokcancel

import Record

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


class Keynote:
    def __init__(self, root):
        self.width = 60
        self.height = 80
        self.length = 50
        self.radium = 7 * self.length / 16
        self.counter = -1

        self.file = None
        self.fen = None

        self.canvas_width = self.width * 2 + self.length * 8
        self.canvas_height = self.height * 2 + self.length * 9
        # self.button_size = (0.5*self.canvas_width-5, self.canvas_height-10, \
        # 0.5*self.canvas_width+5, self.canvas_height-15)

        self.root = root
        self.canvas = Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.place(x=0, y=0)
        # self.canvas.create_rectangle(self.button_size)
        # self.canvas.create_text(0.5*self.canvas_width, self.canvas_height-10, text='Next Move', font=0, tag='button')
        Button(self.root, text='Next Move', command=self.play).pack()
        # Button(self.root, text='Start From Here', command=self.getFen).pack()

        self.root.geometry('520x610')
        self.initRun()
        self.root.mainloop()

    def __getitem__(self):
        return self.fen

    # 返回FEN记录
    def getFen(self):
        return self.fen

    # 绘制当前棋局画面
    def put_chess(self):
        self.fen = Record.FEN_Record(self.read())
        state = self.fen._import()[1]
        for col in range(10):
            for row in range(9):
                chess_kind = state[row][col]
                if chess_kind != -1:
                    # print chess_kind, row, col
                    self.pack((row, col), chess_kind)
                    # print 'Chess put.'

    # 清空当前画面中的棋子
    def erase(self):
        self.canvas.delete("all")

    # print 'Canvas erased.'

    # 绘制棋子
    def pack(self, (x, y), kind):
        if kind < 7:
            self.oval = self.canvas.create_oval( \
                self.width + x * self.length - self.radium, self.height + y * self.length - self.radium, \
                self.width + x * self.length + self.radium, self.height + y * self.length + self.radium, \
                fill='white', width=4)
            self.word = self.canvas.create_text( \
                self.width + x * self.length, self.height + y * self.length, \
                text=name[kind], font=0)
        else:
            self.oval = self.canvas.create_oval( \
                self.width + x * self.length - self.radium, self.height + y * self.length - self.radium, \
                self.width + x * self.length + self.radium, self.height + y * self.length + self.radium, \
                fill='white', outline='red', width=4)
            self.word = self.canvas.create_text( \
                self.width + x * self.length, self.height + y * self.length, \
                text=name[kind], fill='red', font=0)
            # print name[kind], 'packed.'

    # 绘制棋盘
    def paint_board(self):
        for i in range(1, 9):  # 横线
            self.canvas.create_line(self.width, self.height + i * self.length, self.width + 8 * self.length,
                                    self.height + i * self.length)
        for i in range(1, 8):  # 竖线
            self.canvas.create_line(self.width + i * self.length, self.height, self.width + i * self.length,
                                    self.height + 4 * self.length)
            self.canvas.create_line(self.width + i * self.length, self.height + 5 * self.length,
                                    self.width + i * self.length, self.height + 9 * self.length)

        self.canvas.create_line(self.width, self.height + 0 * self.length, self.width + 8 * self.length,
                                self.height + 0 * self.length, width=3)  # 边界线加粗
        self.canvas.create_line(self.width, self.height + 9 * self.length, self.width + 8 * self.length,
                                self.height + 9 * self.length, width=3)
        self.canvas.create_line(self.width + 0 * self.length, self.height, self.width + 0 * self.length,
                                self.height + 9 * self.length, width=3)
        self.canvas.create_line(self.width + 8 * self.length, self.height, self.width + 8 * self.length,
                                self.height + 9 * self.length, width=3)

        self.canvas.create_line(self.width + 3 * self.length, self.height, self.width + 5 * self.length,
                                self.height + 2 * self.length)  # 九宫格内交叉线
        self.canvas.create_line(self.width + 5 * self.length, self.height, self.width + 3 * self.length,
                                self.height + 2 * self.length)
        self.canvas.create_line(self.width + 3 * self.length, self.height + 7 * self.length,
                                self.width + 5 * self.length, self.height + 9 * self.length)
        self.canvas.create_line(self.width + 5 * self.length, self.height + 7 * self.length,
                                self.width + 3 * self.length, self.height + 9 * self.length)

        for i in [1, 7]:  # 炮台与兵卒位
            for j in [2, 7]:
                self.canvas.create_line(self.width + i * self.length - 4,
                                        self.height + j * self.length - self.length / 3,
                                        self.width + i * self.length - 4, self.height + j * self.length - 4,
                                        self.width + i * self.length - self.length / 3,
                                        self.height + j * self.length - 4)
                self.canvas.create_line(self.width + i * self.length - 4,
                                        self.height + j * self.length + self.length / 3,
                                        self.width + i * self.length - 4, self.height + j * self.length + 4,
                                        self.width + i * self.length - self.length / 3,
                                        self.height + j * self.length + 4)
                self.canvas.create_line(self.width + i * self.length + 4,
                                        self.height + j * self.length - self.length / 3,
                                        self.width + i * self.length + 4, self.height + j * self.length - 4,
                                        self.width + i * self.length + self.length / 3,
                                        self.height + j * self.length - 4)
                self.canvas.create_line(self.width + i * self.length + 4,
                                        self.height + j * self.length + self.length / 3,
                                        self.width + i * self.length + 4, self.height + j * self.length + 4,
                                        self.width + i * self.length + self.length / 3,
                                        self.height + j * self.length + 4)

        for i in [0, 2, 4, 6, 8]:  # 兵卒位
            for j in [3, 6]:
                if i != 0:
                    self.canvas.create_line(self.width + i * self.length - 4,
                                            self.height + j * self.length - self.length / 3,
                                            self.width + i * self.length - 4, self.height + j * self.length - 4,
                                            self.width + i * self.length - self.length / 3,
                                            self.height + j * self.length - 4)
                    self.canvas.create_line(self.width + i * self.length - 4,
                                            self.height + j * self.length + self.length / 3,
                                            self.width + i * self.length - 4, self.height + j * self.length + 4,
                                            self.width + i * self.length - self.length / 3,
                                            self.height + j * self.length + 4)
                if i != 8:
                    self.canvas.create_line(self.width + i * self.length + 4,
                                            self.height + j * self.length - self.length / 3,
                                            self.width + i * self.length + 4, self.height + j * self.length - 4,
                                            self.width + i * self.length + self.length / 3,
                                            self.height + j * self.length - 4)
                    self.canvas.create_line(self.width + i * self.length + 4,
                                            self.height + j * self.length + self.length / 3,
                                            self.width + i * self.length + 4, self.height + j * self.length + 4,
                                            self.width + i * self.length + self.length / 3,
                                            self.height + j * self.length + 4)
                    # print 'Borad painted.'

    # 切换棋局画面
    def play(self):
        self.erase()
        self.paint_board()
        try:
            self.put_chess()
        except IndexError:
            if askokcancel('演示完成', '是否继续演示？'):
                self.file_window()
            else:
                self.root.destroy()

    # 逐行读取FEN记录文件
    def read(self):
        if not self.file.closed:
            fen = self.file.readline()
        # self.counter += 1
        else:
            raise IOError
        return fen

    # 初始显示界面
    def initRun(self):
        self.paint_board()
        self.file_window()

    # 文件选择窗口
    def file_window(self):
        file_name = askopenfilename(parent=self.root, title='选择文件', \
                                    filetypes=[('FEN Records', '*.fen'), ('Text Files', '*.txt'), ('All Files', '*.*')],
                                    initialdir='Resourses/', \
                                    initialfile='example.fen')
        # self.file = open(file_name, 'r')
        # self.play()
        # '''
        try:
            self.file = open(file_name, 'r')
            self.play()
        except IOError:
            if askokcancel('错误的路径', '是否重新选择？'):
                self.file_window()
            else:
                self.root.destroy()
                # '''


def main():
    root = Tk()
    keynote = Keynote(root)


# keynote.initRun()

if __name__ == '__main__':
    main()
