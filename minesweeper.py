#!/usr/bin/python3
import sys
import argparse
from exceptions import InvalidGameBoardException
from game_board import GameBoard
from game_renderer import GameRenderer

def main(args):
    try:
        if len(sys.argv) < 7:
            print('WARNING: Not all arguments specified. Defaulting to rows=20, columns=20, mines=40')
            board = GameBoard(rows=20, cols=20, mines=40)
        else:
            board = GameBoard(rows=args.rows, cols=args.columns, mines=args.mines)
    except InvalidGameBoardException as error:
        print(str(error))
        sys.exit(1)

    board.generate_board()

    game_renderer = GameRenderer(board)
    game_renderer.play_game()
    print('Thanks for playing :)')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Terminal Minesweeper Game')
    parser.add_argument('-r', '--rows', help='The number of rows', type=int)
    parser.add_argument('-c', '--columns', '--cols', help='The number of columns', type=int)
    parser.add_argument('-m', '--mines', help='The number of mines', type=int)
    args = parser.parse_args()
    try:
        main(args)
    except Exception as error:
        print('Unexpected Exception: {}'.format(error))
