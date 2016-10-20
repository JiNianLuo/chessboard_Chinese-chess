# -*- coding: cp936 -*- 
from Tkinter import *
from string import rjust
from string import split
name = [
    u'\u5C06',#将
    u'\u4ED5',#仕
    u'\u8C61',#象
    u'\u9A6C',#马
    u'\u8F66',#车
    u'\u70AE',#炮
    u'\u5352',#卒
    u'\u5E05',#帅
    u'\u58EB',#士
    u'\u76F8',#相
    u'\u9A6C',#马
    u'\u8F66',#车
    u'\u70AE',#炮
    u'\u5175',#兵
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
        self.canvas = Canvas(self.master, width=self.width*2+self.l*8, height=self.height*2+self.l*9, bg='white')
        self.canvas.place(x=0, y=0)
        self.state = BoardState()
        self.chess = []
        self.location = [
              (4,0),#将
              (5,0),(3,0),#仕
              (6,0),(2,0),#象
              (7,0),(1,0),#马
              (8,0),(0,0),#车
              (7,2),(1,2),#炮
              (8,3),(6,3),(4,3),(2,3),(0,3),#卒
              (4,9),#帅
              (5,9),(3,9),#士
              (6,9),(2,9),#相
              (7,9),(1,9),#马
              (8,9),(0,9),#车
              (7,7),(1,7),#炮
              (8,6),(6,6),(4,6),(2,6),(0,6)#兵
              ]
        self.numbers = [1,2,2,2,2,2,5,1,2,2,2,2,2,5]
        self.display()


    def display(self):
        self.paint_board()
        self.put_chess()

    def paint_board(self):
        a = self.width
        b = self.height
        l = self.l
        c = self.canvas

        for i in range(1,9):#横线
            c.create_line(a,b+i*l,a+8*l,b+i*l)
        for i in range(1,8):#竖线
            c.create_line(a+i*l,b,a+i*l,b+4*l)
            c.create_line(a+i*l,b+5*l,a+i*l,b+9*l)
    
        c.create_line(a,b+0*l,a+8*l,b+0*l, width = 3)#边界线加粗
        c.create_line(a,b+9*l,a+8*l,b+9*l, width = 3)
        c.create_line(a+0*l,b,a+0*l,b+9*l, width = 3)
        c.create_line(a+8*l,b,a+8*l,b+9*l, width = 3)
    
        c.create_line(a+3*l,b,a+5*l,b+2*l)#九宫格内交叉线
        c.create_line(a+5*l,b,a+3*l,b+2*l)
        c.create_line(a+3*l,b+7*l,a+5*l,b+9*l)
        c.create_line(a+5*l,b+7*l,a+3*l,b+9*l)
    
        for i in [1,7]:#炮台与兵卒位
            for j in [2,7]:
                c.create_line(a+i*l-4,b+j*l-l/3,a+i*l-4,b+j*l-4,a+i*l-l/3,b+j*l-4)
                c.create_line(a+i*l-4,b+j*l+l/3,a+i*l-4,b+j*l+4,a+i*l-l/3,b+j*l+4)
                c.create_line(a+i*l+4,b+j*l-l/3,a+i*l+4,b+j*l-4,a+i*l+l/3,b+j*l-4)
                c.create_line(a+i*l+4,b+j*l+l/3,a+i*l+4,b+j*l+4,a+i*l+l/3,b+j*l+4)
    
        for i in [0,2,4,6,8]:#兵卒位
            for j in [3,6]:
                if i != 0:
                    c.create_line(a+i*l-4,b+j*l-l/3,a+i*l-4,b+j*l-4,a+i*l-l/3,b+j*l-4)
                    c.create_line(a+i*l-4,b+j*l+l/3,a+i*l-4,b+j*l+4,a+i*l-l/3,b+j*l+4)
                if i != 8:
                    c.create_line(a+i*l+4,b+j*l-l/3,a+i*l+4,b+j*l-4,a+i*l+l/3,b+j*l-4)
                    c.create_line(a+i*l+4,b+j*l+l/3,a+i*l+4,b+j*l+4,a+i*l+l/3,b+j*l+4)
    
    def put_chess(self):
        for kind in range(14):
            for j in range(self.numbers[kind]):
                self.chess += [CHESS(self.canvas,kind,self)]
        
        
        for i in range(32):
            self.chess[i].pack(self.location[i], i)
            self.state.state_no  [self.location[i][0]][self.location[i][1]] = self.chess[i].No
            self.state.state_kind[self.location[i][0]][self.location[i][1]] = self.chess[i].kind
            
class CHESS:#棋子属性
    def __init__(self, canvas, kind, master):
        self.canvas = canvas
        self.kind = kind
        self.name = name[kind]
        self.a = master.width
        self.b = master.height
        self.l = master.l
        self.r = 7*self.l/16
        self.x = self.y = -1
        self.No = -1
    def pack(self, (x, y), No):
        if self.kind < 7:
            self.oval = self.canvas.create_oval(\
            self.a+x*self.l-self.r,self.b+y*self.l-self.r,\
            self.a+x*self.l+self.r,self.b+y*self.l+self.r,\
            fill='white',width=4)
            self.word = self.canvas.create_text(\
            self.a+x*self.l,self.b+y*self.l,\
            text = self.name,\
            font=0)
        else:
            self.oval = self.canvas.create_oval(\
            self.a+x*self.l-self.r,self.b+y*self.l-self.r,\
            self.a+x*self.l+self.r,self.b+y*self.l+self.r,\
            fill='white',outline='red',width=4)
            self.word = self.canvas.create_text(\
            self.a+x*self.l,self.b+y*self.l,\
            text = self.name,\
            fill='red',font=0)
        self.x = x
        self.y = y
        self.No = No
    def choose(self):
        self.mark1 = self.canvas.create_line(\
            self.a+self.x*self.l-self.l*3/8,self.b+self.y*self.l-self.l/2,\
            self.a+self.x*self.l-self.l/2,self.b+self.y*self.l-self.l/2,\
            self.a+self.x*self.l-self.l/2,self.b+self.y*self.l-self.l*3/8)
        self.mark2 = self.canvas.create_line(\
            self.a+self.x*self.l+self.l*3/8,self.b+self.y*self.l-self.l/2,\
            self.a+self.x*self.l+self.l/2,self.b+self.y*self.l-self.l/2,\
            self.a+self.x*self.l+self.l/2,self.b+self.y*self.l-self.l*3/8)
        self.mark3 = self.canvas.create_line(\
            self.a+self.x*self.l+self.l*3/8,self.b+self.y*self.l+self.l/2,\
            self.a+self.x*self.l+self.l/2,self.b+self.y*self.l+self.l/2,\
            self.a+self.x*self.l+self.l/2,self.b+self.y*self.l+self.l*3/8)
        self.mark4 = self.canvas.create_line(\
            self.a+self.x*self.l-self.l*3/8,self.b+self.y*self.l+self.l/2,\
            self.a+self.x*self.l-self.l/2,self.b+self.y*self.l+self.l/2,\
            self.a+self.x*self.l-self.l/2,self.b+self.y*self.l+self.l*3/8)
    def not_choose(self):
        self.canvas.delete(self.mark1)
        self.canvas.delete(self.mark2)
        self.canvas.delete(self.mark3)
        self.canvas.delete(self.mark4)

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
        self.Board = Board(root, a, b, l)
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
                    if self.right_move(self.choosed_chess, x, y):#符合走动规则
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
            if self.Board.state[x, y][1] == -1 and self.right_move(self.choosed_chess, x, y):#选中位置无棋子,并且符合走动规则
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

    def right_move(self, chess, x, y):
        a = self.Board.width
        b = self.Board.height
        l = self.Board.l
        if chess.kind % 7 == 4:#车
            if chess.x == x:#车在直线上走动
                if y > chess.y:
                    for i in range(chess.y+1, y):
                        if self.Board.state[x, i][0] != -1:
                            return False
                else:
                    for i in range(y+1, chess.y):
                        if self.Board.state[x, i][0] != -1:
                            return False
                return True
            elif chess.y == y:#车在直线上走动
                if x > chess.x:
                    for i in range(chess.x+1, x):
                        if self.Board.state[i, y][0] != -1:
                            return False
                else:
                    for i in range(x+1, chess.x):
                        if self.Board.state[i, y][0] != -1:
                            return False
                return True
            return False
        elif chess.kind % 7 == 3:#马
            if (abs(chess.x-x) == 2 and abs(chess.y-y) == 1) or\
            (abs(chess.x-x) == 1 and abs(chess.y-y) == 2):#马走日
                if abs(chess.x - x) == 2:
                    if self.Board.state[chess.x+(x-chess.x)/abs(chess.x-x), chess.y][0] != -1:
                        return False
                else:
                    if self.Board.state[chess.x, chess.y+(y-chess.y)/abs(chess.y-y)][0] != -1:
                        return False
                return True
            return False
        elif chess.kind % 7 == 5:#炮
            if chess.x == x:#炮在直线上走动
                if y > chess.y:
                    if self.Board.state[x, y][0] == -1:
                        for i in range(chess.y+1, y):
                            if self.Board.state[x, i][0] != -1:
                                return False
                    else:
                        a = 0
                        for i in range(chess.y+1, y):
                            if self.Board.state[x, i][0] != -1:
                                a += 1
                        if a != 1:
                            return False
                else:
                    if self.Board.state[x, y][0] == -1:
                        for i in range(y+1, chess.y):
                            if self.Board.state[x, i][0] != -1:
                                return False
                    else:
                        a = 0
                        for i in range(y+1, chess.y):
                            if self.Board.state[x,i][0] != -1:
                                a += 1
                        if a != 1:
                            return False
                return True
            elif chess.y == y:#炮在直线上走动
                if x > chess.x:
                    if self.Board.state[x, y][0] == -1:
                        for i in range(chess.x+1, x):
                            if self.Board.state[i, y][0] != -1:
                                return False
                    else:
                        a = 0
                        for i in range(chess.x+1, x):
                            if self.Board.state[i,y][0] != -1:
                                a += 1
                        if a != 1:
                            return False
                else:
                    if self.Board.state[x, y][0] == -1:
                        for i in range(x+1, chess.x):
                            if self.Board.state[i, y][0] != -1:
                                return False
                    else:
                        a = 0
                        for i in range(x+1, chess.x):
                            if self.Board.state[i, y][0] != -1:
                                a += 1
                        if a != 1:
                            return False
                return True
            return False
        elif chess.kind % 7 == 2:#相 or 象
            if abs(chess.x-x) == 2 and abs(chess.y-y) == 2 and self.Board.state[(chess.x+x)/2, (chess.y+y)/2][0] == -1:#象走田，不塞象心
                if (chess.kind < 7 and y < 5) or (chess.kind > 6 and y > 4):#红方（黑方）相（象）不过河
                    return True
            return False
        elif chess.kind % 7 == 1:#士 or 仕
            if abs(chess.x-x) == 1 and abs(chess.y-y) == 1:#士斜走
                if 3<=x<=5 and ((chess.kind < 7 and 0<=y<=2) or (chess.kind > 6 and 7<=y<=9)):#不出九宫
                    return True
            return False
        elif chess.kind % 7 == 0:#帅 or 将
            if (abs(chess.x-x) == 1 and chess.y == y) or (abs(chess.y-y) == 1 and chess.x == x):#帅(将)直走一格
                if 3<=x<=5 and ((chess.kind < 7 and 0<=y<=2) or (chess.kind > 6 and 7<=y<=9)):#不出九宫
                    return True
            return False
        elif chess.kind % 7 == 6:#兵 or 卒
            if chess.kind < 7:
                if (chess.y<5 and chess.x==x and y-chess.y==1) or (chess.y>4 and ((chess.x==x and y-chess.y==1) or (chess.y==y and abs(chess.x-x)==1))):
                    return True
            if chess.kind > 6:
                if (chess.y>4 and chess.x==x and chess.y-y==1) or (chess.y<5 and ((chess.x==x and chess.y-y==1) or (chess.y==y and abs(chess.x-x)==1))):
                    return True
            return False
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

def main():
    root = Tk()
    ChineseChess = app(root)
    ChineseChess.run()

if __name__ == "__main__":
    main()
