import sys

class GameRenderer(object):

    def __init__(self, game_board):
        self.game_board = game_board
        self.cursor_pos = 0

    def play_game(self):
        self.display_board()
        while self.check_game_status():
            return

    def display_board(self):
        position = 0
        for _ in range(self.game_board.rows):
            for _ in range(self.game_board.cols):
                if position == self.cursor_pos:
                    sys.stdout.write('|#')
                    position += 1
                    continue

                value = self.game_board.game_board[position]
                if value == 'mine' or value >= 0:
                    sys.stdout.write('|_')
                elif value == 'flag':
                    sys.stdout.write('|?')
                else:
                    sys.stdout.write('|{}'.format(value * -1))

                position += 1
            sys.stdout.write('|\n')
        sys.stdout.flush()

    def check_game_status(self):
        pass
