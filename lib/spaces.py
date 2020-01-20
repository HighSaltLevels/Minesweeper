class SpaceValue(object):

    def __init__(self, value='blank'):
        self.FLAG_MODIFIER = 10
        self.BLANK = 0
        self.MINE = 9
        self._revealed = False
        self._space_value_dict = {'mine'  : self.MINE,
                                  'blank' : self.BLANK}

        self.SPACE_VALUE_RANGE = range(10)

        self.set_value(value)

    def set_flag(self):
        if not self.is_flag() and not self.is_revealed():
            self._value += self.FLAG_MODIFIER

    def remove_flag(self):
        if self.is_flag():
            self._value -= self.FLAG_MODIFIER

    def is_flag(self):
        return (self._value - self.FLAG_MODIFIER) in self.SPACE_VALUE_RANGE

    def reveal(self):
        self._revealed = True

    def set_value(self, value):
        # If it's not in the dict, it's a number (1-8)
        try:
            self._value = self._space_value_dict[value]
        except KeyError:
            self._value = value

    def get_value(self):
        return self._value

    def is_mine(self):
        if self.is_flag():
            return (self._value - self.FLAG_MODIFIER) == self.MINE
        return self._value == self.MINE

    def is_blank(self):
        return self._value == self.BLANK

    def is_revealed(self):
        return self._revealed

