# -*- coding: utf-8 -*-
from Tkinter import *
from string import rjust
from string import split

import Board
import Pieces

class app:
    def __init__(self, root):
        a = 60
        b = 80
        l = 50
        self.choose = False
        self.choosed_chess = False
        self.xing_qi = True
        self.hui_he = 0
        self.QIPU = []

        self.root = root
        self.Board = Board.Board(root, a, b, l)
        self.front_display()
        self.Board.canvas.bind('<Button-1>', self.move)

    def front_display(self):
        a = self.Board.width
        b = self.Board.height
        l = self.Board.l
        winTitle = u'\u4E2D\u56FD\u8C61\u68CB'
        self.root.title(winTitle)#中国象棋
        self.root.geometry(str(a*2+l*8+200)+'x'+str(b*2+l*9)+'+500+100')
        self.root.resizable(width=False,height=False)#使界面长宽不可变
        self.MENU()
        sb = Scrollbar(self.root)
        sb.pack(side=RIGHT,fill=Y)
        sb.set(0.8,1)
        self.listbox = Listbox(self.root,width=18,height=29,yscrollcommand=sb.set,font=0)
        self.listbox.place(x=a*2+l*8,y=0)
        self.listbox.insert(END, u'     --\u5F00\u59CB--')
        sb.config(command=self.listbox.yview)

    def MENU(self):
        def daKai():
            top = Toplevel()
            top.geometry('200x50+500+100')
            e_ = StringVar()
            e = Entry(top,textvariable = e_)
            e.pack()
            def daKai_():
                road = e_.get()
                if road[-4:-1]+road[-1] == '.che':
                    f = open(road,'r')
                    f = split(f.read())
                    for i in range(len(f)):
                        f[i] = int(f[i])
                    num = range(f[1])
                    for i in num:
                        num[i] = range(10)
                    for i in range(f[1]):
                        for j in range(10):
                            num[i][j] = f[i*10+j+2]
                    for i in range(f[1]):
                        print num[i]
            b = Button(top,text=u'\u6253\u5F00',command=daKai_)#打开
            b.pack()
        def lingCunWei():
            pass
        def bangZhu():
            pass
        m = Menu(self.root)
        self.root.config(menu=m)
        wen_jian = Menu(m)#文件
        m.add_cascade(label=u'\u6587\u4EF6',menu=wen_jian)
        wen_jian.add_command(label=u'\u6253\u5F00\u2026',command=daKai)#打开…
        wen_jian.add_command(label=u'\u53E6\u5B58\u4E3A\u2026',command=lingCunWei)#另存为…
        bang_zhu = Menu(m)#帮助
        m.add_cascade(label=u'\u5E2E\u52A9',menu=bang_zhu)
        bang_zhu.add_command(label=u'\u5E2E\u52A9',command=bangZhu)#帮助

    def run(self):
        self.root.mainloop()

    def move(self, event):
        a = self.Board.width
        b = self.Board.height
        l = self.Board.l
        x = (event.x - a + l/2) / l#将像素坐标转化为棋盘坐标
        y = (event.y - b + l/2) / l

        #for i in self.Board.chess:
        #    print i.No
        #for i in self.Board.state.state_no:
        #    print i , '\n'

        if x < 0 or y < 0 or x > 8 or y > 9:#点击位置超出棋盘，退出该函数
            return
        if not self.choose and self.Board.state[x, y][0] != -1 and ((self.Board.chess[self.Board.state[x, y][0]].kind>6 and self.xing_qi) or (self.Board.chess[self.Board.state[x, y][0]].kind<7 and not self.xing_qi)):#无选中的棋子时选中点击位置的棋子
            if self.choosed_chess:
                self.choosed_chess.not_choose()
            self.choosed_chess = self.Board.chess[self.Board.state[x, y][0]]#选中棋子
            
            print self.choosed_chess.x
            
            self.choosed_chess.choose()
            self.choose = True
            return
        if self.choose and (self.choosed_chess.No != self.Board.state[x, y][0]):#有选中的棋子,并且再次点击位置与棋子位置不同
            if self.Board.state[x, y][0] != -1:#再次点击的位置有棋子
                another_chess = self.Board.chess[self.Board.state[x, y][0]]
                if (another_chess.kind > 6 and self.choosed_chess.kind > 6) or \
                (another_chess.kind < 7 and self.choosed_chess.kind <7):#棋子属于同一方,选中该棋子
                    self.choosed_chess.not_choose()
                    self.choosed_chess = another_chess
                    self.choosed_chess.choose()
                    return
                else:#棋子不属于同一方
                    if Pieces.right_move(self.Board, self.choosed_chess, x, y):#符合走动规则
                        self.qi_pu(self.choosed_chess,x,y)#棋谱编辑
                        another_chess.canvas.delete(another_chess.oval)#删除该棋子，即吃子
                        another_chess.canvas.delete(another_chess.word)
                        another_chess.x = -1
                        another_chess.y = -1
    
                        self.choosed_chess.canvas.move(self.choosed_chess.oval,(x-self.choosed_chess.x)*self.choosed_chess.l,(y-self.choosed_chess.y)*self.choosed_chess.l)#移动选中的棋子
                        self.choosed_chess.canvas.move(self.choosed_chess.word,(x-self.choosed_chess.x)*self.choosed_chess.l,(y-self.choosed_chess.y)*self.choosed_chess.l)
                        self.Board.state[self.choosed_chess.x, self.choosed_chess.y] = [-1, -1]
                        self.choosed_chess.x = x
                        self.choosed_chess.y = y
                        self.Board.state[x, y] = [self.choosed_chess.No, self.choosed_chess.kind]
                        self.choose = not self.choose#移动后取消对该棋子的选中
                        self.xing_qi = not self.xing_qi
                        return
            if self.Board.state[x, y][1] == -1 and Pieces.right_move(self.Board, self.choosed_chess, x, y):#选中位置无棋子,并且符合走动规则
                self.qi_pu(self.choosed_chess,x,y)#棋谱编辑
    
                self.choosed_chess.canvas.move(self.choosed_chess.oval,(x-self.choosed_chess.x)*self.choosed_chess.l,(y-self.choosed_chess.y)*self.choosed_chess.l)#移动选中的棋子
                self.choosed_chess.canvas.move(self.choosed_chess.word,(x-self.choosed_chess.x)*self.choosed_chess.l,(y-self.choosed_chess.y)*self.choosed_chess.l)
                self.Board.state[self.choosed_chess.x, self.choosed_chess.y] = [-1, -1]
                self.choosed_chess.x = x
                self.choosed_chess.y = y
                self.Board.state[x, y] = [self.choosed_chess.No, self.choosed_chess.kind]
                self.choose = not self.choose#移动后取消对该棋子的选中
                self.choosed_chess.not_choose()
                self.choosed_chess.choose()
                self.xing_qi = not self.xing_qi
                return
        if self.choose and self.choosed_chess.No == self.Board.state[x, y][0]:
            self.choose = not self.choose#再次点击该棋子取消选中
            self.choosed_chess.not_choose()

    def qi_pu(self, chess, x, y):
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
        self.listbox.insert(END, TEXT)
        self.listbox.see(END)
        print self.QIPU[-1][-1]

def display():
    root = Tk()
    ChineseChess = app(root)
    ChineseChess.run()

if __name__ == "__main__":
    display()
