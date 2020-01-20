# Minesweeper
This is a simple little minesweeper game that you can play in the terminal. The only dependency is a python interpreter with version >= python3.6.0 as it uses only python builtins.

## To build and play
_So far_ I haven't used any non-native python package, but I have a feeling that I'm going to have to at some point. You should be able to just... run it.

**ALSO NOTE:** This will only work on linux. You're welcome to try running it on Windows, but it probably won't work.

To see the help message, you can just run:
```
python3 app --help
```

You can specify how many rows, columns, and mines you want to generate by using the following commands (which are all equivalent). Note that if not all arguments are specified, this program will assume 20 rows, 20 columns and 40 mines.
```
python3 app -r 20 -c 20 -m 40
```
```
python3 app --rows 20 --columns 20 --mines 40
```
```
python3 app --rows 20 --cols 20 --mines 40
```

## To Modify and Release a single executable
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
