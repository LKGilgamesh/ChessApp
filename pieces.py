import abc

class Piece:
    @abc.abstractmethod
    def getName(self):
        pass
        
class Pawn(Piece):
    def getName(self):
        return "P"

class Rook(Piece):
    def getName(self):
        return "R"

class Bishop(Piece):
    def getName(self):
        return "B"

class Knight(Piece):
    def getName(self):
        return "N"

class Queen(Piece):
    def getName(self):
        return "Q"

class King(Piece):
    def getName(self):
        return "K"