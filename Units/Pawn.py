from arcade import Sprite
from Utils import is_occupied


class Pawn(Sprite):
    def __init__(self, img, center_x, center_y, game):
        super().__init__(img, scale=0.15)
        self.center_x = center_x
        self.center_y = center_y
        self.counter = 0
        self.game = game

    def can_move_to(self, x, y, pieces, pieces_op, side):
        king = pieces_op.get('King')
        if king.center_x == x and king.center_y == y:
            return False

        dx = x - self.center_x
        dy = y - self.center_y

        if side == 'white':

            if dx == 0 and dy == 100:
                return not is_occupied(x, y, pieces) and not is_occupied(x, y, pieces_op)

            if dx == 0 and dy == 200 and self.center_y == 150:
                return not is_occupied(x, 250, pieces) and not is_occupied(x, 250, pieces_op) and \
                    not is_occupied(x, 350, pieces) and not is_occupied(x, 350, pieces_op)

            if abs(dx) == 100 and dy == 100:
                return is_occupied(x, y, pieces_op)

        elif side == 'black':

            if dx == 0 and dy == -100:
                return not is_occupied(x, y, pieces) and not is_occupied(x, y, pieces_op)

            if dx == 0 and dy == -200 and self.center_y == 650:
                return (not is_occupied(x, 550, pieces) and not is_occupied(x, 550, pieces_op) and
                        not is_occupied(x, 450, pieces) and not is_occupied(x, 450, pieces_op))

            if abs(dx) == 100 and dy == -100:
                return is_occupied(x, y, pieces_op)
        return False

    def get_possible_moves(self, pieces, pieces_op, side):
        possible_moves = set()
        combinations = [(-100, 100), (0, 100), (100, 100), (0, 200)] if side == 'white' else [(100, -100), (0, -100),
                                                                                              (-100, -100), (0, -200)]
        for i in combinations:
            x, y = self.center_x + i[0], self.center_y + i[1]
            if 0 < x <= 750 and 0 < y <= 750 and self.can_move_to(x, y, pieces, pieces_op, side):
                possible_moves.add((x, y))
        return possible_moves
