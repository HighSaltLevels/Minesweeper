#!/usr/bin/python3
import sys
import argparse
from game_board import GameBoard

def main(args):
    if len(sys.argv) < 4:
        print('WARNING: Not all arguments specified. Defaulting to rows=20, columns=20, mines=40')
        board = GameBoard(rows=20, cols=20, mines=40)
    else:
        board = GameBoard(rows=args.rows, cols=args.columns, mines=args.mines)

    board.generate_board()
    board.display_board()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Terminal Minesweeper Game')
    parser.add_argument('-r', '--rows', help='The number of rows', type=int)
    parser.add_argument('-c', '--columns', '--cols', help='The number of columns', type=int)
    parser.add_argument('-m', '--mines', help='The number of mines', type=int)
    args = parser.parse_args()
    main(args)
