# -*- coding: cp936 -*-
from Tkinter import *

# class InitChoice:
#  ʹ�÷�����
#    choiceInstance = InitChoice(windows)
#    modeNumber = choiceInstance.get_mode()
#  ���ز���˵����
#    1������ģʽ
#    2�����ɰ���ģʽ


class InitChoice:
    def __init__(self, window):
        self._window = window
        self._var = IntVar()
        self._r1 = Radiobutton(window, text="Mode 1: Normal Mode", variable=self._var, value=1,
                               command=self._sel)
        self._r1.pack(anchor=W)
        self._r2 = Radiobutton(window, text="Mode 2: Free Mode", variable=self._var, value=2,
                               command=self._sel)
        self._r2.pack(anchor=W)

        self._label = Label(window)
        self._label.pack()

    def get_mode(self):
        self._window.mainloop()
        return self._var.get()

    def _sel(self):
        selection = "You selected the Mode " + str(self._var.get())
        self._label.config(text=selection)


def main():
    win = Tk()
    choice = InitChoice(win)
    print choice.get_mode()

if __name__ == '__main__':
    main()

'''
Դ���룺
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

���Դ��룺
print var.get()
raw_input()

'''
