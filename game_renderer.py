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
                self.display_board(mines=False)
            if keep_playing == 3:
                self.display_board(mines=True)
            time.sleep(0.01)
        self.clear_board()

    def display_board(self, mines=False):
        position = 0
        self.clear_board()
        for _ in range(self.game_board.rows):
            for _ in range(self.game_board.cols):
                if position == self.cursor_pos:
                    sys.stdout.write('|#')
                    position += 1
                    continue

                value = self.game_board.game_board[position]
                if 'flag' in value:
                    sys.stdout.write('|?')
                elif value == 'mine':
                    if mines:
                        sys.stdout.write('|*')
                    else:
                        sys.stdout.write('|_')
                elif int(value) <= 0:
                    sys.stdout.write('|_')
                else:
                    sys.stdout.write('|{}'.format(value))

                position += 1
            sys.stdout.write('|\n')
        self.print_instructions()
        sys.stdout.flush()

    def clear_board(self):
        os.system('clear')

    def print_instructions(self):
        sys.stdout.write('Your cursor is \'#\'\n')
        sys.stdout.write('Use the arrow keys to move around.\n')
        sys.stdout.write('Place a flag (?) by pressing Backspace.\n')
        sys.stdout.write('Make a guess by pressing Enter.\n')
        sys.stdout.write('Press \'q\' at any time to quit.')

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
        if self.game_board.game_board[self.cursor_pos] == '0':
            self.reveal_adjacent_blanks()
        elif self.game_board.game_board[self.cursor_pos] == 'mine':
            return 3
        else:
            original = self.game_board.game_board[self.cursor_pos]
            if 'flag' in original:
                original = original[4:]
            self.game_board.game_board[self.cursor_pos] = str(-1 * int(original))
        return 2

    def reveal_adjacent_blanks(self):
        pass

    def set_flag(self):
        if 'flag' in self.game_board.game_board[self.cursor_pos]:
            original = self.game_board.game_board[self.cursor_pos][4:]
            self.game_board.game_board[self.cursor_pos] = original
        else:
            original = self.game_board.game_board[self.cursor_pos]
            self.game_board.game_board[self.cursor_pos] = 'flag' + original
        return 2

    def quit_game(self):
        return 0
