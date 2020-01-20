# Minesweeper
This is a simple little minesweeper game that you can play in the terminal. The only dependency is a python interpreter with version >= python3.6.0 as it uses only python builtins.

## To Install and Run the Binary
With 2 commands, you can download the most recent version of the binary (version 1.3.0). Please run these commands as root.
```bash
wget -O /usr/bin/minesweeper "https://github.com/HighSaltLevels/Minesweeper/releases/download/1.3.0/minesweeper-$(uname -s)-$(uname -m)"
chmod +x /usr/bin/minesweeper
```
If the above 2 commands work, then you should be able to play the game from anywhere in your terminal by typing `minesweeper`

**NOTE:** This will only work on linux. You're welcome to try running it on Windows, but it _probably_ won't work.

## To Play
To see the help message, you can just run:
```
minesweeper --help
```

You can specify how many rows, columns, and mines you want to generate by using the following commands (which are all equivalent).

**Note:** This game defaults to 20 rows, 20 columns, and 40 mines. If you leave out an argument, this game will use the default value for that argument.
```
minesweeper -r 20 -c 20 -m 40
```
```
minesweeper --rows 20 --cols 20 --mines 40
```
```
minesweeper -r 20
```
```
minesweeper -m 40
```
```
minesweeper
```

## To Modify and Release a Single Executable
If you would like to modify the source code and build your own version of minesweeper, you can generate a zipped executable by following these steps.

1. Create a release directory and copy all of the files into it.
```bash
mkdir release
cp app/* release
cp lib/* release
```

2. (Optional) Compile the files into binaries

See [this python3 docs link](https://docs.python.org/3/library/py_compile.html) for more information on compiling python files. If you are fealing really lucky, you can try using [the compileall python module](https://docs.python.org/3/library/compileall.html)

3. Create a zip file of all of the python files, tell bash how to execute it, and give it executable permissions.
```bash
cd release
zip -r minesweeper.zip *
echo '#!/usr/bin/env python3' | cat - minesweeper.zip > minesweeper
chmod +x minesweeper

```
