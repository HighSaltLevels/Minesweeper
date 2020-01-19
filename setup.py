import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="HighSaltLevels",
    version="1.0.1",
    author="David Greeson",
    author_email="swdrummer13@gmail.com",
    description="Terminal-based minesweeper game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/highsaltlevels/Minesweeper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',
)
