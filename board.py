from pieces import Rook, Knight, Bishop, Queen, King, Pawn, Piece
from functools import reduce
from enum import IntEnum

class Position(IntEnum):
    a8 = 0,
    b8 = 1,
    c8 = 2, 
    d8 = 3, 
    e8 = 4, 
    f8 = 5,
    g8 = 6,
    h8 = 7,
    a7 = 8,
    b7 = 9,
    c7 = 10, 
    d7 = 11, 
    e7 = 12, 
    f7 = 13,
    g7 = 14,
    h7 = 15,
    a6 = 16,
    b6 = 17,
    c6 = 18, 
    d6 = 19, 
    e6 = 20, 
    f6 = 21,
    g6 = 22,
    h6 = 23,
    a5 = 24,
    b5 = 25,
    c5 = 26, 
    d5 = 27, 
    e5 = 28, 
    f5 = 29,
    g5 = 30,
    h5 = 31,
    a4 = 32,
    b4 = 33,
    c4 = 34, 
    d4 = 35, 
    e4 = 36, 
    f4 = 37,
    g4 = 38,
    h4 = 39,
    a3 = 40,
    b3 = 41,
    c3 = 42, 
    d3 = 43, 
    e3 = 44, 
    f3 = 45,
    g3 = 46,
    h3 = 47,
    a2 = 48,
    b2 = 49,
    c2 = 50, 
    d2 = 51, 
    e2 = 52, 
    f2 = 53,
    g2 = 54,
    h2 = 55,
    a1 = 56,
    b1 = 57,
    c1 = 58, 
    d1 = 59, 
    e1 = 60, 
    f1 = 61,
    g1 = 62,
    h1 = 63

def convertToIndex(pos) -> tuple[int, int]:
    y = pos % 8
    x = (pos // 8)
    return (x, y)


def reverseList(lists):
    return reduce(lambda a, x: ( list(map (reverseList, [x]) if isinstance(x, list) else [x])) + a, lists, [])

def chessPieces(white):
    side = [[Rook(), Knight(), Bishop(), Queen(), King(), Bishop(), Knight(), Rook()],
    [Pawn(),Pawn(),Pawn(),Pawn(),Pawn(),Pawn(),Pawn(),Pawn()]]

    if (not white):
        side.reverse()
    
    return side

class Board:
    def newBoard(self):
        board = chessPieces(True)
        for x in range(4):
            board.append([None] * 8)
        
        blackset = chessPieces(False)
        for x in blackset:
            board.append(x)
        
        return board

    def __init__(self):
        self.squares = self.newBoard()

    def movePiece(self, oldPos, newPos):
        oldCoord = convertToIndex(oldPos)
        newCoord = convertToIndex(newPos)
        
        #check if there is a piece on the oldtile
        if (self.squares[oldCoord[0]][oldCoord[1]] == None):
            return
        #check to see if the move is valid

        #check to see if it takes an enemy piece
        
        #move the piece
        obj = self.squares[oldCoord[0]][oldCoord[1]]

        self.squares[newCoord[0]][newCoord[1]] = obj
        self.squares[oldCoord[0]][oldCoord[1]] = None
        