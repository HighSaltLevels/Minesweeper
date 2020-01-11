import os
import sys
import tty
import termios
import time

class GameRenderer(object):

    def __init__(self, game_board):
        self.game_board = game_board
        self.cursor_pos = 0
        self.char_dict = {b'A'   : self.move_up,
                          b'B'   : self.move_down,
                          b'C'   : self.move_right,
                          b'D'   : self.move_left,
                          b'\r'  : self.make_guess,
                          b'\x7f': self.set_flag,
                          b'q'   : self.quit_game} 

    def play_game(self):
        self.display_board()
        keep_playing = 1
        while keep_playing:
            keep_playing = self.check_game_status()
            if keep_playing == 2:
                self.display_board()
            time.sleep(0.01)
        self.clear_board()

    def display_board(self):
        position = 0
        self.clear_board()
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
        sys.stdout.write('Press \'q\' at any time to quit')
        sys.stdout.flush()

    def clear_board(self):
        os.system('clear')

    def check_game_status(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            readable_char = ch.encode(encoding='UTF-8', errors='strict')
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        try:
            status = self.char_dict[readable_char]()
        except KeyError:
            status = 1 # Don't care about other keyboard presses
        return status

    def move_up(self):
        if not self.game_board.is_top_border(self.cursor_pos):
            self.cursor_pos -= self.game_board.cols
            return 2
        return 1

    def move_left(self):
        if not self.game_board.is_left_border(self.cursor_pos):
            self.cursor_pos -= 1
            return 2
        return 1

    def move_down(self):
        if not self.game_board.is_bottom_border(self.cursor_pos):
            self.cursor_pos += self.game_board.cols
            return 2
        return 1

    def move_right(self):
        if not self.game_board.is_right_border(self.cursor_pos):
            self.cursor_pos += 1
            return 2
        return 1

    def make_guess(self):
        return 2

    def set_flag(self):
        return 2

    def quit_game(self):
        return 0
