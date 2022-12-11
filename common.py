from sys import argv
from typing import List, Set, Dict, Tuple, Deque
from functools import reduce
from fp import Chainable


def get_lines(fname: str, rstrip=True):
	""" Return a list from a map object mapping each line of the input
	file fname to its stripped version, preceding and trailing whitespace
	removed """
	if rstrip:
		strip_func = lambda l: l.rstrip()
	else:
		strip_func = lambda l: l
	
	with open(fname, 'r') as f:
		return list(map(strip_func, f.readlines()))
