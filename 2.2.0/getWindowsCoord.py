# -*- coding: utf-8 -*-
import ChessLib.UI
from Tkinter import Tk
import os

# 说明
# author:崔泓睿
# date:2016/11/30
# 这个模块是配合TestExample模块使用的，主要是为了获得最终矩阵的状态和鼠标点击坐标序列
# 运行后点击的窗口坐标会记录在coord.txt文件里，每一次点击后的矩阵状态会记录在matrix.txt
# 文件中，matrix.txt的最后一个矩阵就是我们需要的最终状态。
# 特别注意，为了保证测试的正确性，文件打开模式为w，因此每次运行模块都会清空相应的文件
# 如果需要保存的话请先做好备份。

root = Tk()
game = ChessLib.UI.app(root)
game.root.geometry('%dx%d+%d+%d' % (600, 600, 0, 0))
f_coord = open("coord.txt", 'w')
f_matrix = open("matrix.txt", 'w')
try:
    os.chdir("TestSample")
except WindowsError:
    os.mkdir("TestSample")
    os.chdir("TestSample")


def mouse_click_callback(event):
    f_coord.write("%d %d\n" % (event.x_root, event.y_root))
    for row in game.Board.state.state_no:
        for element in row:
            f_matrix.write("%d " % element)
        f_matrix.write('\n')
    f_matrix.write('\n')


def print_coord(event):
    print event.x, event.y, ";", event.x_root, event.y_root

game.root.bind("<Button-1>", mouse_click_callback)
game.run()
f_coord.close()
f_matrix.close()
os.chdir("..")

