from arcade import Sprite
from Utils import is_occupied
from itertools import product


class Knight(Sprite):
    def __init__(self, img, center_x, center_y):
        super().__init__(img, scale=0.12)
        self.center_x = center_x
        self.center_y = center_y

    def can_move_to(self, x, y, pieces, pieces_op, side=None):
        king = pieces_op.get('King')
        if king.center_x == x and king.center_y == y:
            return False
        if abs(self.center_x - x) == 100 and abs(self.center_y - y) == 200 or abs(self.center_x - x) == 200 and abs(
                self.center_y - y) == 100:
            return not is_occupied(x, y, pieces)
        return False

    def get_possible_moves(self, pieces, pieces_op, side=None):
        possible_moves = set()
        nums = [200, 100, -100, -200]
        for i in product(nums, repeat=2):
            x, y = self.center_x + i[0], self.center_y + i[1]
            if i != (0, 0) and 0 < x <= 750 and 0 < y <= 750 and self.can_move_to(x, y, pieces, pieces_op):
                possible_moves.add((x, y))
        return possible_moves
