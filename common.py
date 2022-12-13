from sys import argv
from typing import List, Set, Dict, Tuple, Deque
from functools import reduce
from fp import Chainable
from dataclasses import dataclass
from collections import deque
from queue import PriorityQueue


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


@dataclass
class Pos:
	r: int
	c: int

	def __hash__(self) -> int:
		return hash((self.r, self.c))

	def __add__(self, other):
		if isinstance(other, self.__class__):
			return Pos(self.r + other.r, self.c + other.c)
		r, c = other
		return Pos(self.r + r, self.c + c)

	def __lt__(self, other):
		return False

	def __mul__(self, n: int):
		return Pos(self.r * n, self.c * n)

	def distance(self, other, L=2) -> float:
		r1, c1 = self.r, self.c
		r2, c2 = other.r, other.c
		return (abs(r1-r2)**L + abs(c1-c2)**L) ** (1/L)


DIR = dict(
	U = Pos(-1, 0),
	D = Pos( 1, 0),
	L = Pos( 0,-1),
	R = Pos( 0, 1),
)
