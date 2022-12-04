from sys import argv
from typing import List, Set, Dict


def get_lines(fname: str):
	""" Return a map object that map each line of the input file
	fname to its stripped version, preceding and trailing whitespace
	removed """
	with open(fname, 'r') as f:
		return list(map(lambda l: l.strip(), f.readlines()))


if __name__ == "__main__":
	print(argv)