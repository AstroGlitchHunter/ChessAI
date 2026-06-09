def is_occupied(x, y, pieces):
    return any(p.center_x == x and p.center_y == y for p in pieces.values())


def find_match(x, y, pieces):
    for p in pieces.values():
        if p.center_x == x and p.center_y == y:
            return type(p)
    return None
