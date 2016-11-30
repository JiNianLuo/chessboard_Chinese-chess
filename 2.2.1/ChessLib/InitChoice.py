# -*- coding: utf-8 -*-
from Tkinter import *

import UI
import FreeMode
import Keynote


# class InitChoice:
#  使用方法：
#    choiceInstance = InitChoice(windows)
#    modeNumber = choiceInstance.get_mode()
#  返回参数说明：
#    1：正常模式
#    2：自由摆棋模式


class InitChoice:
    def __init__(self, window):
        self._window = window
        self._var = IntVar()

        self._frame = Frame(self._window, width=520, height=610, relief='flat')
        self._frame.pack()

        self._r1 = Radiobutton(self._frame, text="Mode 1: Normal Mode", variable=self._var, value=1, \
                               command=self._sel)
        self._r1.pack(anchor=W)
        self._r2 = Radiobutton(self._frame, text="Mode 2: Free Mode", variable=self._var, value=2, \
                               command=self._sel)
        self._r2.pack(anchor=W)
        self._r2 = Radiobutton(self._frame, text="Mode 3: Display Mode", variable=self._var, value=3, \
                               command=self._sel)
        self._r2.pack(anchor=W)

        self._label = Label(self._frame)
        self._label.pack()

        self._button = Button(self._frame, text='Start', command=self.start)
        self._button.pack()

        self.mode = -1
        self._window.mainloop()

    '''
	def get_mode(self):
		self._frame.clear("All")
		return self._var.get()
	'''

    def _sel(self):
        selection = "You selected the Mode " + str(self._var.get())
        self._label.config(text=selection)

    def start(self):
        self._frame.destroy()
        self.mode = self._var.get()

        if self.mode == 1:
            ChineseChess = UI.app(self._window)
            ChineseChess.run()
        elif self.mode == 2:
            arbitaryChess = FreeMode.appArb(self._window)
            arbitaryChess.run()
        else:
            keynote = Keynote.Keynote(self._window)


def display():
    rootWindow = Tk()
    choice = InitChoice(rootWindow)


if __name__ == '__main__':
    display()

'''
源代码：
def sel():
	selection = "You selected the Mode " + str(var.get())
	label.config(text=selection)


root = Tk()

var = IntVar()
R1 = Radiobutton(root, text="Mode 1: Normal Mode", variable=var, value=1,
				 command=sel)
R1.pack(anchor=W)
R2 = Radiobutton(root, text="Mode 2: Free Mode", variable=var, value=2,
				 command=sel)
R2.pack(anchor=W)

label = Label(root)
label.pack()

root.mainloop()

测试代码：
print var.get()
raw_input()

'''
