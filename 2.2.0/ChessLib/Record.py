# -*- coding: utf-8 -*-
from Tkinter import *
from string import rjust
from string import split

FEN_STARTING = 'rnbakabnr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RNBAKABNR w - - 0 1'


class FEN_Record:
    def __init__(self, FEN=None):
        if FEN is None:
            self.fen = FEN_STARTING
        else:
            self.fen = FEN

    def _export(self, Board, chess):  # Board to FEN
        self.fen = ''
        for col in range(10):
            tmp = 0
            for row in range(9):
                no = Board.state.state_kind[row][col]
                if no != -1:
                    tmp = 0
                else:
                    tmp += 1
                if row == 8 and tmp != 0:   self.fen += str(tmp); continue
                if row != 8 and tmp != 0 and Board.state.state_kind[row + 1][col] != -1:
                    self.fen += str(tmp);
                    continue
                if no == 0: self.fen += 'k'; continue
                if no == 1: self.fen += 'a'; continue
                if no == 2: self.fen += 'b'; continue
                if no == 3: self.fen += 'n'; continue
                if no == 4: self.fen += 'r'; continue
                if no == 5: self.fen += 'c'; continue
                if no == 6: self.fen += 'p'; continue
                if no == 7: self.fen += 'K'; continue
                if no == 8: self.fen += 'A'; continue
                if no == 9: self.fen += 'B'; continue
                if no == 10: self.fen += 'N'; continue
                if no == 11: self.fen += 'R'; continue
                if no == 12: self.fen += 'C'; continue
                if no == 13: self.fen += 'P'; continue
            # 以上if语句组可用dict实现
            self.fen += '/'
        self.fen = self.fen[:-1]
        if chess.kind > 7:
            self.fen += ' b - - '
        else:
            self.fen += ' r - - '
        self.fen += str(Board.half_counter) + ' ' + str(Board.counter)
        return self.fen

    def _import(self):  # FEN to Board
        new_fen = ''

        pointer = -1
        for item in self.fen:
            if not item.isspace():
                pointer += 1
                if item.isdigit():
                    tmp = int(item)
                    while tmp > 0:
                        new_fen += '0'  # 将FEN记录中的数字缩进展开，便于之后的读取操作
                        tmp -= 1
                    continue
                if item.isalpha():
                    new_fen += item
            else:
                break

        # print pointer

        # 导出执棋方的颜色
        if self.fen[pointer + 2] == 'r':
            chess_colour = True
        else:
            chess_colour = False
        # print self.fen[pointer+2]

        # 导出半回合数
        pointer += 8
        half_counter = ''
        while self.fen[pointer].isdigit():
            half_counter += self.fen[pointer]
            pointer += 1
        half_counter = int(half_counter)
        # print half_counter

        # 导出回合数
        pointer += 1
        counter = ''
        while True:
            try:
                if self.fen[pointer].isdigit():
                    counter += self.fen[pointer]
                    pointer += 1
                else:
                    break
            except IndexError:
                break
        counter = int(counter)
        # print counter

        state_no = [
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
        state_kind = [
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

        ptr = -1
        a = b = n = r = c = p = A = B = N = R = C = P = 0
        for col in range(10):
            for row in range(9):
                ptr += 1
                char = new_fen[ptr]
                # print ptr, char, a, b, n, r, c, p
                if char == '0': state_no[row][col] = -1; state_kind[row][col] = -1; continue
                if char == 'k': state_no[row][col] = 0; state_kind[row][col] = 0; continue
                if char == 'a': state_no[row][col] = 1 + a; state_kind[row][col] = 1; a += 1; continue
                if char == 'b': state_no[row][col] = 3 + b; state_kind[row][col] = 2; b += 1; continue
                if char == 'n': state_no[row][col] = 5 + n; state_kind[row][col] = 3; n += 1; continue
                if char == 'r': state_no[row][col] = 7 + r; state_kind[row][col] = 4; r += 1; continue
                if char == 'c': state_no[row][col] = 9 + c; state_kind[row][col] = 5; c += 1; continue
                if char == 'p': state_no[row][col] = 11 + p; state_kind[row][col] = 6; p += 1; continue
                if char == 'K': state_no[row][col] = 16; state_kind[row][col] = 7; continue
                if char == 'A': state_no[row][col] = 17 + A; state_kind[row][col] = 8; A += 1; continue
                if char == 'B': state_no[row][col] = 19 + B; state_kind[row][col] = 9; B += 1; continue
                if char == 'N': state_no[row][col] = 21 + N; state_kind[row][col] = 10; N += 1; continue
                if char == 'R': state_no[row][col] = 23 + R; state_kind[row][col] = 11; R += 1; continue
                if char == 'C': state_no[row][col] = 25 + C; state_kind[row][col] = 12; C += 1; continue
                if char == 'P': state_no[row][col] = 27 + P; state_kind[row][col] = 13; P += 1; continue
            # 以上if语句组可用dict实现

        # print state_kind
        return state_no, state_kind, chess_colour, half_counter, counter


class CHE_Record:
    def __init__(self, Board):
        self.Board = Board
        self.hui_he = 0
        self.QIPU = []

    def record(self, chess, x, y):
        zhong_guo_shu_zi = [
            u'\u4E00',  # 一
            u'\u4E8C',  # 二
            u'\u4E09',  # 三
            u'\u56DB',  # 四
            u'\u4E94',  # 五
            u'\u516D',  # 六
            u'\u4E03',  # 七
            u'\u516B',  # 八
            u'\u4E5D',  # 九
        ]
        Arabic_num = [
            u'\uFF11',  # １
            u'\uFF12',  # ２
            u'\uFF13',  # ３
            u'\uFF14',  # ４
            u'\uFF15',  # ５
            u'\uFF16',  # ６
            u'\uFF17',  # ７
            u'\uFF18',  # ８
            u'\uFF19',  # ９
        ]

        TEXT = chess.name
        if chess.kind in [0, 4, 5, 6]:  # 黑方车、炮、将、卒
            if chess.y == y:
                TEXT += Arabic_num[chess.x] + u'\u5E73' + Arabic_num[x]  # 平
            elif chess.y > y:
                TEXT += Arabic_num[chess.x] + u'\u9000' + Arabic_num[chess.y - y - 1]  # 退
            else:
                TEXT += Arabic_num[chess.x] + u'\u8FDB' + Arabic_num[y - chess.y - 1]  # 进
        elif chess.kind in [7, 11, 12, 13]:  # 红方车、炮、帅、兵
            if chess.y == y:
                TEXT += zhong_guo_shu_zi[8 - chess.x] + u'\u5E73' + zhong_guo_shu_zi[8 - x]  # 平
            elif chess.y < y:
                TEXT += zhong_guo_shu_zi[8 - chess.x] + u'\u9000' + zhong_guo_shu_zi[y - chess.y - 1]  # 退
            else:
                TEXT += zhong_guo_shu_zi[8 - chess.x] + u'\u8FDB' + zhong_guo_shu_zi[chess.y - y - 1]  # 进
        elif chess.kind in [8, 9, 10]:  # 红方马、相、士
            if chess.y < y:
                TEXT += zhong_guo_shu_zi[8 - chess.x] + u'\u9000' + zhong_guo_shu_zi[8 - x]  # 退
            else:
                TEXT += zhong_guo_shu_zi[8 - chess.x] + u'\u8FDB' + zhong_guo_shu_zi[8 - x]  # 进
        else:  # 黑方马、象、仕
            if chess.y > y:
                TEXT += Arabic_num[chess.x] + u'\u9000' + Arabic_num[x]  # 退
            else:
                TEXT += Arabic_num[chess.x] + u'\u8FDB' + Arabic_num[x]  # 进
        if chess.kind < 7:
            self.QIPU += [[self.Board.state.state_no,
                           [chess.No, 32, 0, 9 - chess.y, 8 - chess.x, 9 - y, 8 - x, 0, self.hui_he * 2,
                            0]]]  # 真实记谱.che格式
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
            self.QIPU += [[self.Board.state.state_no,
                           [chess.No, 32, 1, 9 - chess.y, 8 - chess.x, 9 - y, 8 - x, 0, self.hui_he * 2 - 1,
                            0]]]  # 真实记谱.che格式
            for i in range(10):
                if self.Board.state[chess.x, i][1] == chess.kind and i != chess.y:
                    if i > chess.y:
                        TEXT = rjust(str(self.hui_he), 3) + u'. \u524D' + TEXT
                        break
                    else:
                        TEXT = rjust(str(self.hui_he), 3) + u'. \u540E' + TEXT
                        break
            else:
                TEXT = rjust(str(self.hui_he), 3) + '. ' + TEXT

        # fen = FEN_RECORD()
        # print fen._export(self.Board)

        return TEXT

    def qi_pu(self, listbox, Board, chess, x, y):
        TEXT = self.record(chess, x, y)
        listbox.insert(END, TEXT)
        listbox.see(END)
