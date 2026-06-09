from Units import *


def get_start_pieces(game):
    white_pieces = {
        "Rook1": Rook(r"Chess pieces images\Rook.png", 50, 50),
        "Knight1": Knight(r"Chess pieces images\Knight.png", 150, 50),
        "Bishop1": Bishop(r"Chess pieces images\Bishop.png", 250, 50),
        "Queen": Queen(r"Chess pieces images\Queen.png", 350, 50),
        "King": King(r"Chess pieces images\King.png", 450, 50),
        "Bishop2": Bishop(r"Chess pieces images\Bishop.png", 550, 50),
        "Knight2": Knight(r"Chess pieces images\Knight.png", 650, 50),
        "Rook2": Rook(r"Chess pieces images\Rook.png", 750, 50),
        "Pawn1": Pawn(r"Chess pieces images\Pawn.png", 50, 150,game),
        "Pawn2": Pawn(r"Chess pieces images\Pawn.png", 150, 150, game),
        "Pawn3": Pawn(r"Chess pieces images\Pawn.png", 250, 150, game),
        "Pawn4": Pawn(r"Chess pieces images\Pawn.png", 350, 150, game),
        "Pawn5": Pawn(r"Chess pieces images\Pawn.png", 450, 150, game),
        "Pawn6": Pawn(r"Chess pieces images\Pawn.png", 550, 150, game),
        "Pawn7": Pawn(r"Chess pieces images\Pawn.png", 650, 150, game),
        "Pawn8": Pawn(r"Chess pieces images\Pawn.png", 750, 150, game)
    }
    black_pieces = {
    "Rook1": Rook(r"Chess pieces images\RookOp.png", 50, 750),
    "Knight1": Knight(r"Chess pieces images\KnightOp.png", 150, 750),
    "Bishop1": Bishop(r"Chess pieces images\BishopOp.png", 250, 750),
    "Queen": Queen(r"Chess pieces images\QueenOp.png", 350, 750),
    "King": King(r"Chess pieces images\KingOp.png", 450, 750),
    "Bishop2": Bishop(r"Chess pieces images\BishopOp.png", 550, 750),
    "Knight2": Knight(r"Chess pieces images\KnightOp.png", 650, 750),
    "Rook2": Rook(r"Chess pieces images\RookOp.png", 750, 750),
    "Pawn1": Pawn(r"Chess pieces images\PawnOp.png", 50, 650, game),
    "Pawn2": Pawn(r"Chess pieces images\PawnOp.png", 150, 650, game),
    "Pawn3": Pawn(r"Chess pieces images\PawnOp.png", 250, 650, game),
    "Pawn4": Pawn(r"Chess pieces images\PawnOp.png", 350, 650, game),
    "Pawn5": Pawn(r"Chess pieces images\PawnOp.png", 450, 650, game),
    "Pawn6": Pawn(r"Chess pieces images\PawnOp.png", 550, 650, game),
    "Pawn7": Pawn(r"Chess pieces images\PawnOp.png", 650, 650, game),
    "Pawn8": Pawn(r"Chess pieces images\PawnOp.png", 750, 650, game)
}
    return white_pieces, black_pieces