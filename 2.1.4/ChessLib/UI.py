# -*- coding: utf-8 -*-
from Tkinter import *
import FreeMode
import Board
import Pieces
import Record
from InitChoice import InitChoice


class app:
    def __init__(self, root):
        a = 60
        b = 80
        l = 50
        self.choose = False
        self.choosed_chess = False
        self.xing_qi = True

        self.root = root
        self.Board = Board.Board(root, a, b, l)
        self.front_display()
        self.Board.canvas.bind('<Button-1>', self.move)
        self.che_record = Record.CHE_Record(self.Board)

        #test
        #self.f = open("mousePos.txt", 'w')

    def front_display(self):
        a = self.Board._offset_x
        b = self.Board._offset_y
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
                    #f = split(f.read())
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
        self.root.quit()
# RickFreeman week11-Tuesday:
#   I want to break down the move function so that it can be easily modified to receive FEN strings and behave just like
#   after clicked, and the program internally pass a FEN string to it.
#   This is for the convinence of testing

    def windows_coord_to_board_coord(self, x, y):
        a = self.Board._offset_x
        b = self.Board._offset_y
        l = self.Board.l
        board_x = (x - a + l / 2) / l  # 将像素坐标转化为棋盘坐标
        board_y = (y - b + l / 2) / l
        return board_x, board_y

    def mouse_click_callback(self, event):
        board_coord = self.windows_coord_to_board_coord(event.x, event.y)
        if not self.legal_move(board_coord, self.Board):
            return
        self.change_state(board_coord)
        self.draw_canvas()

    def legal_move(self, _board_coord, _board):
        pass

    def draw_canvas(self):  # 2016/11/23 RickFreeman: the canvas won't clean up itself. Gotta solve it.
        _board = self.Board

        for i in range(32):
            if (_board.chess[i].x, _board.chess[i].y) != (-1, -1):
                _board.chess[i].pack((_board.chess[i].x, _board.chess[i].y), i)

    def change_state(self, _board_coord):
        pass

    def move(self, event):
        a = self.Board._offset_x
        b = self.Board._offset_y
        l = self.Board.l
        x = (event.x - a + l/2) / l#将像素坐标转化为棋盘坐标
        y = (event.y - b + l/2) / l

        #.write("windows coord: (%d, %d); screen coord: (%d, %d)\n" %(event.x, event.y, event.x_root, event.y_root))

        if x < 0 or y < 0 or x > 8 or y > 9:#点击位置超出棋盘，退出该函数
            return
        if not self.choose and self.Board.state[x, y][0] != -1 and ((self.Board.chess[self.Board.state[x, y][0]].kind>6 and self.xing_qi) or (self.Board.chess[self.Board.state[x, y][0]].kind<7 and not self.xing_qi)):#无选中的棋子时选中点击位置的棋子
            if self.choosed_chess:
                self.choosed_chess.not_choose()
            self.choosed_chess = self.Board.chess[self.Board.state[x, y][0]]#选中棋子
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
                        self.che_record.qi_pu(self.listbox, self.Board, self.choosed_chess,x,y)#棋谱编辑
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
                self.che_record.qi_pu(self.listbox, self.Board, self.choosed_chess,x,y)#棋谱编辑
    
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


def display():
    _win = Tk()
    initChoice = InitChoice(_win)
    gameMode = initChoice.get_mode()

    root = Tk()
    if gameMode == 1:
        ChineseChess = app(root)
        ChineseChess.run()
    elif gameMode == 2:
        arbitaryChess = FreeMode.appArb(root)
        arbitaryChess.run()

if __name__ == "__main__":
    display()
