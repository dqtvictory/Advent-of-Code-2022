from sys import argv
from typing import List, Set, Dict


def get_lines(fname: str):
	""" Return list of stripped lines from input file `fname` (without preceding)
	and trailing whitespace """
	with open(fname, 'r') as f:
		return list(map(lambda l: l.strip(), f.readlines()))


if __name__ == "__main__":
	print(argv)