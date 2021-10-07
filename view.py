import board
from pieces import Piece
from board import Position


class View:
    def __str__(self):
        return __name__.__str__

class ConsoleView(View):
    def __init__(self, board):
        self.board = board

    def UpdateDisplay(self):
        print("   a b c d e f g h ")
        letter = 8
        for x in self.board.squares:
            rowtxt = str(letter) + " |"
            for y in x:
                if isinstance(y, Piece):
                    rowtxt = rowtxt + y.getName() + '|'
                else:
                    rowtxt += ' |'
            letter -= 1
            print(rowtxt)

    def MovePiece(self, oldPos, newPos):
        oldPosAsEnum = board.Position[oldPos]
        newPosAsEnum = board.Position[newPos]
        self.board.movePiece(oldPosAsEnum, newPosAsEnum)


import PyQt5.QtWidgets
from PyQt5.QtGui import QPixmap

class ChessBoardWidget(PyQt5.QtWidgets.QWidget, View):
    BoardPosition = {}
    def InitBoardPosition(self):
        for i in range(8):
            for j in range(8):
                self.BoardPosition[Position(i + (j * 8))] = (85 + (105 * i), 85 + (105 * j))
    #0,0 is 85, 85
    #increment by 105.
    def __init__(self, parent = None):
        PyQt5.QtWidgets.QWidget.__init__(self, parent= parent)
        self.InitBoardPosition()
        self.initUI()

    def initUI(self):
        self.resize(1000,1000)
        #self.center()
        self.setWindowTitle('Chess')

        self.Board = PyQt5.QtWidgets.QLabel(self)
        self.Boardpixmap = QPixmap("ChessBoard.jpeg")
        self.Board.setPixmap(self.Boardpixmap)

        self.Board.resize(self.Boardpixmap.width(),
                        self.Boardpixmap.height())

        self.King = PyQt5.QtWidgets.QLabel(self)
        self.Kingpixmap = QPixmap("w_king.png")
        self.King.setPixmap(self.Kingpixmap)

        pos = self.BoardPosition[Position.h1]

        self.King.move(pos[0],pos[1])
        self.King.resize(self.Kingpixmap.width(),
                        self.Kingpixmap.height())

        self.show()