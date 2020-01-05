import sys
import time
from inputs import get_key
from inputs import UnpluggedError
from exceptions import NoKeyboardException

class GameRenderer(object):

    def __init__(self, game_board):
        self.game_board = game_board
        self.cursor_pos = 0
        self.event_dict = {'KEY_UP':         self.move_up,
                           'KEY_RIGHT':      self.move_right,
                           'KEY_DOWN':       self.move_down,
                           'KEY_LEFT':       self.move_left,
                           'KEY_ENTER':      self.make_guess,
                           'KEY_RIGHTSHIFT': self.set_flag,
                           'KEY_LEFTSHIFT':  self.set_flag} 

    def play_game(self):
        self.display_board()
        while self.check_game_status():
            time.sleep(0.1)

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
        try:
            events = get_key()
        except UnpluggedError:
            raise NoKeyboardException
        for event in events:
            if not event.state: # ignore button releases
                status = True
                continue
            try:
                status = self.event_dict[event.code]()
            except KeyError:
                status = True # Don't care about other keyboard presses
        return status

    def move_up(self):
        print('moving up')
        return True

    def move_left(self):
        print('moving left')
        return True

    def move_down(self):
        print('moving down')
        return True

    def move_right(self):
        print('moving right')
        return True

    def make_guess(self):
        print('making guess')
        return True

    def set_flag(self):
        print('setting flag')
        return True
