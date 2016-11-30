# -*-coding:utf-8-*-
import unittest
import ChessLib.UI
import win32api
import win32con
from Tkinter import Tk
import threading
import time
import os


class TestGameMethod(unittest.TestCase):

    def setUp(self):
        os.chdir("TestSample")
        self.click_seq = []
        self.final_matrix = []
        f_seq = open(r"coord.txt", 'r')
        for row in f_seq.readlines():
            row = row.replace('\n', '')
            point = (int(row.split(' ')[0]), int(row.split(' ')[1]))
            self.click_seq.append(point)
        f_seq.close()
        f_matrix = open(r"final_matrix.txt", 'r')
        for row in f_matrix.readlines():
            row = row.replace('\n', '')
            tmp_list = []
            for element in row.split(' '):
                tmp_list.append(int(element))
            self.final_matrix.append(tmp_list)
        f_matrix.close()
        tk = Tk()
        self.game = ChessLib.UI.app(tk)
        self.game.root.geometry('%dx%d+%d+%d' % (600, 600, 0, 0))

        pass

    def click_from_seq(self):
        time.sleep(0.5)
        for point in self.click_seq:
            self.click(point[0], point[1])

        time.sleep(1)
        real_matrix = self.game.Board.state.state_no
        f_real_matrix = open(r"real_matrix.txt", 'w')
        for col in real_matrix:
            for elem in col:
                f_real_matrix.write("%d " % elem)
            f_real_matrix.write("\n")
        f_real_matrix.close()

    def run_game(self):
        self.game.run()

    def test_move(self):
        threads = []
        t1 = threading.Thread(target=self.run_game)
        threads.append(t1)
        t2 = threading.Thread(target=self.click_from_seq)
        threads.append(t2)
        for t in threads:
            t.setDaemon(True)
            t.start()
        time.sleep(5)

        self.assertEquals(self.game.Board.state.state_no, self.final_matrix)

        pass

    def tearDown(self):
        os.chdir("..")
        pass

    def click(self, x, y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

if __name__ == "__main__":
    unittest.main()

