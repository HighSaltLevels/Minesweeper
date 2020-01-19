import os
import sys
import tty
import termios
import time

class GameRenderer(object):

    def __init__(self, game_board):
        self._game_board = game_board
        self._cursor_pos = 0
        self._char_to_command_dict = {b'A'   : self._move_up,
                                      b'B'   : self._move_down,
                                      b'C'   : self._move_right,
                                      b'D'   : self._move_left,
                                      b'\r'  : self._make_guess,
                                      b' ': self._set_flag,
                                      b'q'   : self._quit_game}

        self.IN_PROGRESS = 0
        self.LOSS = 1
        self.VICTORY = 2
        self.QUIT = 3
        self.IGNORE = 4

    def play_game(self):
        self._display_board() 
        while True:
            game_status = self._check_game_status()
            if game_status == self.IN_PROGRESS:
                self._display_board(mines=False)
            elif game_status == self.LOSS:
                self._display_board(mines=True)
                break
            elif game_status == self.VICTORY:
                self._display_board(mines=True)
                sys.stdout.write('\n\nVictory!\n\n')
                sys.stdout.flush()
                break
            elif game_status == self.QUIT:
                break

            time.sleep(0.01)

    def _display_board(self, mines=False):
        position = 0
        self._clear_board()
        for _ in range(self._game_board.rows()):
            for _ in range(self._game_board.cols()):
                if position == self._cursor_pos:
                    sys.stdout.write('|#')
                    position += 1
                    continue

                if self._game_board.spaces[position].is_flag():
                    sys.stdout.write('|?')
                elif self._game_board.spaces[position].is_mine():
                    sys.stdout.write('|*') if mines else sys.stdout.write('|_')
                elif self._game_board.spaces[position].is_revealed() and \
                    self._game_board.spaces[position].is_blank():
                    sys.stdout.write('| ')
                elif not self._game_board.spaces[position].is_revealed():
                    sys.stdout.write('|_')
                else:
                    value = self._game_board.spaces[position].get_value()
                    sys.stdout.write(f'|{value}')

                position += 1
            sys.stdout.write('|\n')
        self._print_instructions()
        sys.stdout.flush()

    def _clear_board(self):
        os.system('clear')

    def _print_instructions(self):
        sys.stdout.write('Your cursor is \'#\'\n')
        sys.stdout.write('Use the arrow keys to move around.\n')
        sys.stdout.write('Place a flag (?) by pressing the Space Bar.\n')
        sys.stdout.write('Make a guess by pressing Enter.\n')
        sys.stdout.write('Press \'q\' at any time to quit.')

    def _check_game_status(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            readable_char = ch.encode(encoding='UTF-8', errors='strict')
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        try:
            status = self._char_to_command_dict[readable_char]()
        # Ignore any other button presses
        except KeyError:
            status = self.IGNORE

        if self._game_board.all_revealed():
            status = self.VICTORY

        return status

    def _move_up(self):
        if not self._game_board.is_top_border(self._cursor_pos):
            self._cursor_pos -= self._game_board.cols()
        return self.IN_PROGRESS

    def _move_left(self):
        if not self._game_board.is_left_border(self._cursor_pos):
            self._cursor_pos -= 1
        return self.IN_PROGRESS

    def _move_down(self):
        if not self._game_board.is_bottom_border(self._cursor_pos):
            self._cursor_pos += self._game_board.cols()
        return self.IN_PROGRESS

    def _move_right(self):
        if not self._game_board.is_right_border(self._cursor_pos):
            self._cursor_pos += 1
        return self.IN_PROGRESS

    def _make_guess(self):
        if not self._game_board.spaces[self._cursor_pos].is_revealed() and \
            self._game_board.spaces[self._cursor_pos].is_blank():
            self._reveal_adjacent_blanks()
        elif self._game_board.spaces[self._cursor_pos].is_mine():
            return self.LOSS
        elif not self._game_board.spaces[self._cursor_pos].is_revealed():
            self._game_board.spaces[self._cursor_pos].reveal()
        return self.IN_PROGRESS

    def _reveal_adjacent_blanks(self):
        blanks_left = True
        self._game_board.spaces[self._cursor_pos].reveal()
        while blanks_left:
            blanks_left = False
            for space in range(self._game_board.size()):
                if self._game_board.has_adjacent_revealed_blank(space) and not \
                    self._game_board.spaces[space].is_revealed():
                    self._game_board.spaces[space].reveal()
                    blanks_left = True

    def _set_flag(self):
        if self._game_board.spaces[self._cursor_pos].is_flag():
            self._game_board.spaces[self._cursor_pos].remove_flag()
        else:
            self._game_board.spaces[self._cursor_pos].set_flag()

        return self.IN_PROGRESS

    def _quit_game(self):
        return self.QUIT
