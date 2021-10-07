from enum import Enum
import pieces
import board
import view
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QLabel

exitApp = False

def leaveApp():
    global exitApp
    exitApp = True

def takeAction(args, view):
    switcher = {
        "m" : view.MovePiece,
        "q" : leaveApp
    }
    return switcher[args[0]]


def runConsole():
    cview = view.ConsoleView(board.Board())
    while(not exitApp):
        cview.UpdateDisplay()
        response = input("What would you like to do? (m)ove, (q)uit: ").split()

        action = takeAction(response[0], cview)
        if (len(response) == 3):
            action(response[1], response[2])
        else:
            action()

def runQtView():
    app = QtWidgets.QApplication(sys.argv)
    qtview = view.ChessBoardWidget()
    app.exec_()


def main():

    print('Argument List: %s' % str(sys.argv))

    if (len(sys.argv) > 1):
        if (sys.argv[1] == 'console'):
            runConsole()
        elif (sys.argv[1] == 'qt'):
            runQtView()
        else:
            runConsole()
    else:
        runConsole()
    
if __name__ == '__main__':
    main()

