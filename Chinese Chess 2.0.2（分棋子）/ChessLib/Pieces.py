# -*- coding: utf-8 -*-
class Piece:
    def __init__(self, Board, chess):
        self.Board = Board
        self.chess = chess

class Rook(Piece):#车
    def legal_move(self, x, y):
        if self.chess.x == x:#车在直线上走动
            if y > self.chess.y:
                for i in range(self.chess.y+1, y):
                    if self.Board.state[x, i][0] != -1:
                        return False
            else:
                for i in range(y+1, self.chess.y):
                    if self.Board.state[x, i][0] != -1:
                        return False
            return True
        elif self.chess.y == y:#车在直线上走动
            if x > self.chess.x:
                for i in range(self.chess.x+1, x):
                    if self.Board.state[i, y][0] != -1:
                        return False
            else:
                for i in range(x+1, self.chess.x):
                    if self.Board.state[i, y][0] != -1:
                        return False
            return True
        return False

class Knight(Piece):
    def legal_move(self, x, y):
        if (abs(self.chess.x-x) == 2 and abs(self.chess.y-y) == 1) or\
            (abs(self.chess.x-x) == 1 and abs(self.chess.y-y) == 2):#马走日
            if abs(self.chess.x - x) == 2:
                if self.Board.state[self.chess.x+(x-self.chess.x)/abs(self.chess.x-x), self.chess.y][0] != -1:
                    return False
            else:
                if self.Board.state[self.chess.x, self.chess.y+(y-self.chess.y)/abs(self.chess.y-y)][0] != -1:
                    return False
            return True
        return False

class Cannon(Piece):
    def legal_move(self, x, y):
        if self.chess.x == x:#炮在直线上走动
            if y > self.chess.y:
                if self.Board.state[x, y][0] == -1:
                    for i in range(self.chess.y+1, y):
                        if self.Board.state[x, i][0] != -1:
                            return False
                else:
                    a = 0
                    for i in range(self.chess.y+1, y):
                        if self.Board.state[x, i][0] != -1:
                            a += 1
                    if a != 1:
                        return False
            else:
                if self.Board.state[x, y][0] == -1:
                    for i in range(y+1, self.chess.y):
                        if self.Board.state[x, i][0] != -1:
                            return False
                else:
                    a = 0
                    for i in range(y+1, self.chess.y):
                        if self.Board.state[x,i][0] != -1:
                            a += 1
                    if a != 1:
                        return False
            return True
        elif self.chess.y == y:#炮在直线上走动
            if x > self.chess.x:
                if self.Board.state[x, y][0] == -1:
                    for i in range(self.chess.x+1, x):
                        if self.Board.state[i, y][0] != -1:
                            return False
                else:
                    a = 0
                    for i in range(self.chess.x+1, x):
                        if self.Board.state[i,y][0] != -1:
                            a += 1
                    if a != 1:
                        return False
            else:
                if self.Board.state[x, y][0] == -1:
                    for i in range(x+1, self.chess.x):
                        if self.Board.state[i, y][0] != -1:
                            return False
                else:
                    a = 0
                    for i in range(x+1, self.chess.x):
                        if self.Board.state[i, y][0] != -1:
                            a += 1
                    if a != 1:
                        return False
            return True
        return False

class Bishop(Piece):
    def legal_move(self, x, y):
        if abs(self.chess.x-x) == 2 and abs(self.chess.y-y) == 2 and self.Board.state[(self.chess.x+x)/2, (self.chess.y+y)/2][0] == -1:#象走田，不塞象心
            if (self.chess.kind < 7 and y < 5) or (self.chess.kind > 6 and y > 4):#红方（黑方）相（象）不过河
                return True
        return False

class Ambassador(Piece):
    def legal_move(self, x, y):
        if abs(self.chess.x-x) == 1 and abs(self.chess.y-y) == 1:#士斜走
            if 3<=x<=5 and ((self.chess.kind < 7 and 0<=y<=2) or (self.chess.kind > 6 and 7<=y<=9)):#不出九宫
                return True
        return False

class King(Piece):
    def legal_move(self, x, y):
        if (abs(self.chess.x-x) == 1 and self.chess.y == y) or (abs(self.chess.y-y) == 1 and self.chess.x == x):#帅(将)直走一格
            if 3<=x<=5 and ((self.chess.kind < 7 and 0<=y<=2) or (self.chess.kind > 6 and 7<=y<=9)):#不出九宫
                return True
        return False

class Pawn(Piece):
    def legal_move(self, x, y):
        if self.chess.kind < 7:
            if (self.chess.y<5 and self.chess.x==x and y-self.chess.y==1) or (self.chess.y>4 and ((self.chess.x==x and y-self.chess.y==1) or (self.chess.y==y and abs(self.chess.x-x)==1))):
                return True
        if self.chess.kind > 6:
            if (self.chess.y>4 and self.chess.x==x and self.chess.y-y==1) or (self.chess.y<5 and ((self.chess.x==x and self.chess.y-y==1) or (self.chess.y==y and abs(self.chess.x-x)==1))):
                return True
        return False

def right_move(Board, chess, x, y):
    if chess.kind % 7 == 4:#车
        piece = Rook(Board, chess)
    elif chess.kind % 7 == 3:#马
        piece = Knight(Board, chess)
    elif chess.kind % 7 == 5:#炮
        piece = Cannon(Board, chess)
    elif chess.kind % 7 == 2:#相 or 象
        piece = Bishop(Board, chess)
    elif chess.kind % 7 == 1:#士 or 仕
        piece = Ambassador(Board, chess)
    elif chess.kind % 7 == 0:#帅 or 将
        piece = King(Board, chess)
    elif chess.kind % 7 == 6:#兵 or 卒
        piece = Pawn(Board, chess)
    return piece.legal_move(x, y)
