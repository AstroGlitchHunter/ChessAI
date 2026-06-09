from arcade import Sprite
from Utils import is_occupied
from itertools import product


class Rook(Sprite):
    def __init__(self, img, center_x, center_y):
        super().__init__(img, scale=0.2)
        self.center_x = center_x
        self.center_y = center_y

    def can_move_to(self, x, y, pieces, pieces_op, side=None):
        if any(v.center_x == x and v.center_y == y and v.__class__.__name__ == 'King' for v in
               pieces_op.values()):
            return False
        if is_occupied(x, y, pieces):
            return False
        if x == self.center_x:
            step = 100 if y > self.center_y else -100
            for current_y in range(int(self.center_y + step), int(y), int(step)):
                if is_occupied(self.center_x, current_y, pieces) or is_occupied(self.center_x, current_y, pieces_op):
                    return False
            return True
        elif y == self.center_y:
            step = 100 if x > self.center_x else -100
            for current_x in range(int(self.center_x + step), int(x), int(step)):
                if is_occupied(current_x, self.center_y, pieces) or is_occupied(current_x, self.center_y, pieces_op):
                    return False
            return True
        return False

    def get_possible_moves(self, pieces, pieces_op, side=None):
        possible_moves = set()
        nums = [i for i in range(0, 800, 100)] + [i for i in range(-700, 0, 100)]
        for i in product(nums, repeat=2):
            x1, y1 = self.center_x + i[0], self.center_y + i[1]
            if 0 in i and i != (0, 0) and 0 < x1 <= 750 and 0 < y1 <= 750 and self.can_move_to(x1, y1, pieces, pieces_op):
                possible_moves.add((x1, y1))
        return possible_moves
