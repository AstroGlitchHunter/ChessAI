import arcade
import torch

from Attributes import *
from data import get_start_pieces
from AI import ChessNet

WIDTH = 800
HEIGHT = 800
TITLE = 'Chess'

model = ChessNet()
model.load_state_dict(torch.load('chess_net_weights.pth'))

def ai_move(pieces, pieces_op, side):
    ways_dict = {}
    model.eval()
    with torch.no_grad():
        for name, obj in pieces.items():
            for m in obj.get_possible_moves(pieces, pieces_op, side) or []:
                feat = binary_array(m[0], m[1], obj, pieces, pieces_op, side)
                ways_dict[name, m] = model(torch.tensor([feat], dtype=torch.float32)).item()

    if not ways_dict:
        return False, None

    name, move = max(ways_dict, key=ways_dict.get)

    pieces[name].center_x, pieces[name].center_y = move[0], move[1]

    cap = next((k for k, v in pieces_op.items() if v.center_x == move[0] and v.center_y == move[1]), None)
    captured_piece_obj = None
    if cap:
        captured_piece_obj = pieces_op.pop(cap)

    return True, captured_piece_obj


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.pieces = arcade.SpriteList()
        self.bg = arcade.load_texture(r"Chess pieces images\ChessBoard.png")

        self.chosen = None
        self.no_capture_ticks = 0

        self.game_over = False

        self.white_pieces, self.black_pieces = get_start_pieces(self)

        self.my_rects = []
        for i in list(self.white_pieces.values()) + list(self.black_pieces.values()):
            self.pieces.append(i)

    def on_mouse_press(self, x, y, button, modifiers):
        x_val = x // 100 * 100 + 50
        y_val = y // 100 * 100 + 50

        pieces = self.white_pieces
        pieces_op = self.black_pieces

        side = 'white'

        if self.chosen is not None and not is_occupied(x_val, y_val, pieces):
            self.my_rects.clear()
            condition = self.chosen.can_move_to(x_val, y_val, pieces, pieces_op, side)
            if not condition:
                return

            self.chosen.center_x = x_val
            self.chosen.center_y = y_val

            for name, piece in list(pieces_op.items()):
                if piece.center_x == x_val and piece.center_y == y_val:
                    self.pieces.remove(piece)
                    self.no_capture_ticks = 0
                    del pieces_op[name]
                    break
            else:
                self.no_capture_ticks += 1

            self.chosen = None

            ai_pieces = self.black_pieces
            ai_pieces_op = self.white_pieces
            ai_side = 'black'

            ai_success, ai_captured_piece = ai_move(ai_pieces, ai_pieces_op, ai_side)

            if ai_success:
                if ai_captured_piece is not None:
                    self.pieces.remove(ai_captured_piece)
                    self.no_capture_ticks = 0
                else:
                    self.no_capture_ticks += 1
            else:
                print('Мат или пат!')


            if self.no_capture_ticks >= 100:
                print("Ничья по правилу 50 ходов!")
                self.game_over = True

            if len(self.white_pieces) == 1 and len(self.black_pieces) == 1:
                print("Ничья: на доске остались только Короли!")
                self.game_over = True

        else:
            if len(self.my_rects) != 0:
                self.my_rects.clear()
            for i in pieces.values():
                if i.center_x == x_val and i.center_y == y_val:
                    self.chosen = i

                    for j in self.chosen.get_possible_moves(pieces, pieces_op, side):
                        self.my_rects.append(arcade.XYWH(j[0], j[1], 100, 100))

                    break

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.bg, arcade.XYWH(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT))
        self.pieces.draw()

        for i in self.my_rects:
            arcade.draw_rect_filled(i, (27, 219, 24, 127))

    def on_update(self, delta_time: float) -> bool | None:
        pass


if __name__ == '__main__':
    game = Game(WIDTH, HEIGHT, TITLE)
    arcade.run()
