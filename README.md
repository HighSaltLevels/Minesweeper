# Minesweeper
This is a simple little minesweeper game that can be played in the terminal. This is still very much a WIP (like most everything in my GitHub)

## To build and play
_So far_ I haven't used any non-native python package, but I have a feeling that I'm going to have to at some point. You should be able to just... run it.

To see the help message, you can just run:
```
./minesweeper.py -h
```

You can specify how many rows, columns, and mines you want to generate by using the following commands (which are all equivalent)
```
./minesweeper.py -r 20 -c 20 -m 40
```
```
./minesweeper.py --rows 20 --columns 20 --mines 40
```
```
./minesweeper.py --rows 20 --cols 20 --mines 40
```

