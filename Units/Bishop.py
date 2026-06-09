from arcade import Sprite
from Utils import is_occupied
from itertools import product

class Bishop(Sprite):
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

        dx = abs(x - self.center_x)
        dy = abs(y - self.center_y)

        if dx == dy:
            step_x = 100 if x > self.center_x else -100
            step_y = 100 if y > self.center_y else -100

            current_x = self.center_x + step_x
            current_y = self.center_y + step_y

            while current_x != x:
                if is_occupied(current_x, current_y, pieces) or is_occupied(current_x, current_y, pieces_op):
                    return False
                current_x += step_x
                current_y += step_y

            return True
        return False

    def get_possible_moves(self, pieces, pieces_op, side=None):
        possible_moves = set()
        nums = [i for i in range(0, 800, 100)] + [i for i in range(-700, 0, 100)]
        for i in product(nums, repeat=2):
            x, y = self.center_x + i[0], self.center_y + i[1]
            if i != (0, 0) and 0 < x <= 750 and 0 < y <= 750 and self.can_move_to(x, y, pieces, pieces_op):
                possible_moves.add((x, y))

        return possible_moves
