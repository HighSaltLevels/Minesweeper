#!/usr/bin/python3
import sys
import os

# Add lib to path
sys.path.append(os.path.join(sys.path[0], '../lib'))

import argparse
from game_board import GameBoard
from game_renderer import GameRenderer

def main(args):
    try:
        board = GameBoard(rows=args.rows, cols=args.cols, mines=args.mines)
    except RuntimeError as error:
        print(error)
        sys.exit(1)

    board.generate_board()

    game_renderer = GameRenderer(board)
    game_renderer.play_game()

    print('\n\nThanks for playing :)')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Terminal Minesweeper Game')
    parser.add_argument('-r', '--rows', help='Set the number of rows', type=int, default=20)
    parser.add_argument('-c', '--cols', help='Set the number of columns', type=int, default=20)
    parser.add_argument('-m', '--mines', help='Set the number of mines', type=int, default=40)
    args = parser.parse_args()

    try:
        main(args)
    except Exception as error:
       print('\nUnexpected Exception: {}'.format(error))

