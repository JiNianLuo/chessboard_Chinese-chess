# -*- coding: utf-8 -*-
from Tkinter import *
from string import rjust
from string import split

class CHE_RECORD:
    def __init__(self, Board):
        self.Board = Board

        self.hui_he = 0
        self.QIPU = []

    def record(self, chess, x, y):
        zhong_guo_shu_zi = [
            u'\u4E00',#一
            u'\u4E8C',#二
            u'\u4E09',#三
            u'\u56DB',#四
            u'\u4E94',#五
            u'\u516D',#六
            u'\u4E03',#七
            u'\u516B',#八
            u'\u4E5D',#九
            ]
        Arabic_num = [
            u'\uFF11',#１
            u'\uFF12',#２
            u'\uFF13',#３
            u'\uFF14',#４
            u'\uFF15',#５
            u'\uFF16',#６
            u'\uFF17',#７
            u'\uFF18',#８
            u'\uFF19',#９
            ]
    
        TEXT = chess.name
        if chess.kind in [0,4,5,6]:#黑方车、炮、将、卒
            if chess.y == y:
                TEXT += Arabic_num[chess.x] + u'\u5E73' + Arabic_num[x]#平
            elif chess.y > y:
                TEXT += Arabic_num[chess.x] + u'\u9000' + Arabic_num[chess.y-y-1]#退
            else:
                TEXT += Arabic_num[chess.x] + u'\u8FDB' + Arabic_num[y-chess.y-1]#进
        elif chess.kind in [7,11,12,13]:#红方车、炮、帅、兵
            if chess.y == y:
                TEXT += zhong_guo_shu_zi[8-chess.x] + u'\u5E73' + zhong_guo_shu_zi[8-x]#平
            elif chess.y < y:
                TEXT += zhong_guo_shu_zi[8-chess.x] + u'\u9000' + zhong_guo_shu_zi[y-chess.y-1]#退
            else:
                TEXT += zhong_guo_shu_zi[8-chess.x] + u'\u8FDB' + zhong_guo_shu_zi[chess.y-y-1]#进
        elif chess.kind in [8,9,10]:#红方马、相、士
            if chess.y < y:
                TEXT += zhong_guo_shu_zi[8-chess.x] + u'\u9000' + zhong_guo_shu_zi[8-x]#退
            else:
                TEXT += zhong_guo_shu_zi[8-chess.x] + u'\u8FDB' + zhong_guo_shu_zi[8-x]#进
        else:#黑方马、象、仕
            if chess.y > y:
                TEXT += Arabic_num[chess.x] + u'\u9000' + Arabic_num[x]#退
            else:
                TEXT += Arabic_num[chess.x] + u'\u8FDB' + Arabic_num[x]#进
        if chess.kind < 7:
            self.QIPU += [[self.Board.state.state_no, [chess.No, 32, 0, 9-chess.y, 8-chess.x, 9-y, 8-x, 0, self.hui_he*2, 0]]]#真实记谱.che格式
            for i in range(10):
                if self.Board.state[chess.x, i][1] == chess.kind and i != chess.y:
                    if i < chess.y:
                        TEXT = u'   \u524D' + TEXT
                        break
                    else:
                        TEXT = u'   \u540E' + TEXT
                        break
            else:
                TEXT = '     ' + TEXT
        else:
            self.hui_he += 1
            self.QIPU += [[self.Board.state.state_no, [chess.No, 32, 1, 9-chess.y, 8-chess.x, 9-y, 8-x, 0, self.hui_he*2-1, 0]]]#真实记谱.che格式
            for i in range(10):
                if self.Board.state[chess.x, i][1] == chess.kind and i != chess.y:
                    if i > chess.y:
                        TEXT = rjust(str(self.hui_he),3) + u'. \u524D' + TEXT
                        break
                    else:
                        TEXT = rjust(str(self.hui_he),3) + u'. \u540E' + TEXT
                        break
            else:
                TEXT = rjust(str(self.hui_he),3) + '. ' + TEXT
        return TEXT, self.QIPU

def qi_pu(listbox, Board, chess, x, y):
    RECORD = CHE_RECORD(Board)
    (TEXT, QIPU) = RECORD.record(chess, x, y)
    listbox.insert(END, TEXT)
    listbox.see(END)
    print QIPU[-1][-1]
