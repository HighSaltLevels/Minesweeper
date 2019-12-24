import random
import sys
from exceptions import InvalidGameBoardException

class GameBoard(object):

    def __init__(self, rows, cols, mines):
        if mines >= (rows*cols):
            raise InvalidGameBoardException('Too many mines. You must have 1 less mine than the total number of spaces')
        self.rows = rows
        self.cols = cols
        self.size = rows*cols
        self.num_spaces = self.size - 1
        self.mines = mines
        self.game_board = None
        self.clear_board()

    def generate_board(self):
        mine_positions = random.sample(range(0, self.rows*self.cols), self.mines)
        for mine_position in mine_positions:
            self.game_board[mine_position] = -1

        for space in range(self.size):
            if not self.game_board[space]:
                self.game_board[space] = self.get_num_mines(space)

    def get_num_mines(self, space):
        num_mines = 0
        adjacent_space_values = self.get_adjacent_space_values(space)
        for adjacent_space_value in adjacent_space_values:
            if adjacent_space_value == -1:
                num_mines += 1

        return num_mines

    def get_adjacent_space_values(self, space):
        adjacent_space_values = []
        adjacent_space_values.append(self.get_top_left_value(space))
        adjacent_space_values.append(self.get_top_value(space))
        adjacent_space_values.append(self.get_top_right_value(space))
        adjacent_space_values.append(self.get_right_value(space))
        adjacent_space_values.append(self.get_bottom_right_value(space))
        adjacent_space_values.append(self.get_bottom_value(space))
        adjacent_space_values.append(self.get_bottom_left_value(space))
        adjacent_space_values.append(self.get_left_value(space))

        return [value for value in adjacent_space_values if value]

    def get_top_left_value(self, space):
        if self.is_left_border(space):
            return None

        value_pos = space - self.cols - 1
        if value_pos < 0:
            return None

        return self.game_board[value_pos]

    def get_top_value(self, space):
        value_pos = space - self.cols
        if value_pos < 0:
            return None

        return self.game_board[value_pos]

    def get_top_right_value(self, space):
        if self.is_right_border(space):
            return None

        value_pos = space - self.cols + 1
        if value_pos < 0:
            return None

        return self.game_board[value_pos]        

    def get_right_value(self, space):
        if self.is_right_border(space):
            return None

        value_pos = space + 1
        if value_pos > self.num_spaces:
            return None

        return self.game_board[value_pos]

    def get_bottom_right_value(self, space):
        if self.is_right_border(space):
            return None

        value_pos = space + self.cols + 1
        if value_pos > self.num_spaces:
            return None

        return self.game_board[value_pos]

    def get_bottom_value(self, space):
        value_pos = space + self.cols
        if value_pos > self.num_spaces:
            return None

        return self.game_board[value_pos]

    def get_bottom_left_value(self, space):
        if self.is_left_border(space):
            return None

        value_pos = space + self.cols - 1
        if value_pos > self.num_spaces:
            return None

        return self.game_board[value_pos]

    def get_left_value(self, space):
        if self.is_left_border(space):
            return None
        value_pos = space - 1
        if value_pos < 0:
            return None

        return self.game_board[value_pos]

    def is_left_border(self, space):
        return not space % self.cols

    def is_right_border(self, space):
        return (space % self.cols) == (self.cols - 1)

    def clear_board(self):
        self.game_board = [None for _ in range(self.size)]

    def display_board(self):
        space_num = 0
        for row in range(self.rows):
            sys.stdout.write('[')
            for col in range(self.cols):
                sys.stdout.write(' {} '.format(self.game_board[space_num]))
                space_num += 1
            sys.stdout.write(']\n')
        sys.stdout.flush()
