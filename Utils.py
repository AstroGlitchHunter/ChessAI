def is_occupied(x, y, pieces):
    return any(p.center_x == x and p.center_y == y for p in pieces.values())


def find_match(x, y, pieces):
    for p in pieces.values():
        if p.center_x == x and p.center_y == y:
            return type(p)
    return None


def check_game_status(pieces, pieces_op, side):
    all_moves = []

    for p in pieces.values():
        moves = p.get_possible_moves(pieces, pieces_op, side)
        all_moves.extend(moves)

    if len(all_moves) > 0:
        return 'Играем дальше'

    king = pieces.get('King')
    king_pos = (king.center_x, king.center_y)

    op_side = 'black' if side == 'white' else 'white'
    is_check = False


    for p in pieces_op.values():
        moves = p.get_possible_moves(pieces, pieces_op, op_side)
        if king_pos in moves:
            is_check = True
            break


    if is_check:
        return 'Мат'
    return 'Пат'


