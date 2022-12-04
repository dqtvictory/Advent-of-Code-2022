from sys import argv
from typing import List, Set, Dict, Tuple
from functools import reduce


def get_lines(fname: str):
	""" Return a list from a map object mapping each line of the input
	file fname to its stripped version, preceding and trailing whitespace
	removed """
	with open(fname, 'r') as f:
		return list(map(lambda l: l.strip(), f.readlines()))
