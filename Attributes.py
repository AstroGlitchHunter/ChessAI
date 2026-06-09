from Utils import *
from Units import *

values = {King: 0, Queen: 1, Rook: 0.55, Knight: 0.33, Bishop: 0.33, Pawn: 0.11}
chess_hierarchy = {Pawn: 1, Knight: 2, Bishop: 3, Rook: 4, Queen: 5, King: 6}


def to_be_eaten(x, y, pieces, pieces_op, side):
    enemy_side = 'white' if side == 'black' else 'black'
    for piece_op in pieces_op.values():
        if piece_op.can_move_to(x, y, pieces_op, pieces, enemy_side):
            return 1
    return 0


def eat(x, y, pieces_op):
    return int(is_occupied(x, y, pieces_op))


def eat_higher(obj, captured_value):
    if captured_value is not None:
        return int(chess_hierarchy[type(obj)] < chess_hierarchy[type(captured_value)])
    return 0


def is_king(obj):
    return int(isinstance(obj, King))


def value(obj):
    return values[type(obj)]


def reach_end(y, obj, side):
    if isinstance(obj, Pawn):
        if side == 'white':
            return int(y == 750)
        return int(y == 50)
    return 0


def is_the_youngest(obj, pieces):
    return int(chess_hierarchy[type(obj)] == min(
        chess_hierarchy[type(i)] for i in pieces.values()))


def eaten_by_higher(x, y, obj, pieces, pieces_op, side):
    enemy_side = 'white' if side == 'black' else 'black'
    my_rank = chess_hierarchy[type(obj)]

    attacking_enemies_ranks = [
        chess_hierarchy[type(piece_op)]
        for piece_op in pieces_op.values()
        if piece_op.can_move_to(x, y, pieces_op, pieces, enemy_side)
    ]

    if not attacking_enemies_ranks:
        return 0

    min_attacking_enemy = min(attacking_enemies_ranks)

    return int(my_rank < min_attacking_enemy)


def global_balance(x, y, pieces, pieces_op, side):
    enemy_side = 'white' if side == 'black' else 'black'

    attacking_enemies = [
        chess_hierarchy[type(piece_op)]
        for piece_op in pieces_op.values()
        if piece_op.can_move_to(x, y, pieces_op, pieces, enemy_side)
    ]

    if not attacking_enemies:
        return 0

    min_enemy_rank = min(attacking_enemies)

    defending_partners = [
        chess_hierarchy[type(piece)]
        for piece in pieces.values()
        if piece.can_move_to(x, y, pieces, pieces_op, side)
    ]

    max_partner = max(defending_partners) if defending_partners else 0

    return int(min_enemy_rank > max_partner)


def make_checkmate(pieces, pieces_op, side):
    king = next((v for v in pieces_op.values() if isinstance(v, King)), None)
    if not king:
        return 0

    check = any(a.can_move_to(king.center_x, king.center_y, pieces, pieces_op, side) for a in pieces.values())

    enemy_side = 'black' if side == 'white' else 'white'
    has_moves = any(
        v.get_possible_moves(pieces_op, pieces, enemy_side) for v in pieces_op.values()
    )

    return int(check and not has_moves)


def binary_array(x, y, obj, pieces, pieces_op, side):
    old_x, old_y = obj.center_x, obj.center_y

    captured_key = next((k for k, v in pieces_op.items() if v.center_x == x and v.center_y == y), None)
    captured_value = pieces_op.pop(captured_key, None) if captured_key else None

    obj.center_x, obj.center_y = x, y

    arr = [
        int(captured_value is not None),
        eat_higher(obj, captured_value),
        to_be_eaten(x, y, pieces, pieces_op, side),
        eaten_by_higher(x, y, obj, pieces, pieces_op, side),
        is_the_youngest(obj, pieces),
        reach_end(y, obj, side),
        value(obj),
        is_king(obj),
        global_balance(x, y, pieces, pieces_op, side),
        make_checkmate(pieces, pieces_op, side)
    ]

    obj.center_x, obj.center_y = old_x, old_y
    if captured_key and captured_value:
        pieces_op[captured_key] = captured_value

    return arr
