from common import *
from functools import cmp_to_key

def build_items(lines: List[str]) -> list:
	def item_reducer(prev: List[Tuple[list, list]], cur: Tuple[int, list]):
		i, item = cur
		if i % 3 == 0:
			return prev + [(item, )]
		if i % 3 == 1:
			return prev[:-1] + [prev[-1] + (item, )]
		return prev

	return Chainable(lines) \
		.map(lambda l: eval(l) if l else None) \
		.enumerate() \
		.reduce(item_reducer, True, [])

def cmp(left: list, right: list):
	def cmp_reducer(last_score:int, cur: tuple) -> int:
		if last_score != 0:
			return last_score	# only continue if last score is not determined
		l, r = cur
		tl, tr = type(l), type(r)
		if tl == tr == int:
			return l - r
		if tl == tr == list:
			return cmp(l, r)
		if tl == int:
			return cmp([l], r)
		return cmp(l, [r])

	res = Chainable(zip(left, right)) \
		.reduce(cmp_reducer, True, 0)
	return len(left) - len(right) if res == 0 else res

def part1(items: List[Tuple[list, list]]):
	return sum(Chainable(items) \
		.enumerate(1) \
		.filter(lambda iit: cmp(iit[1][0], iit[1][1]) <= 0) \
		.map(lambda iit: iit[0]))

def part2(items: List[Tuple[list, list]]):
	p2, p6 = [[2]], [[6]]
	packets = Chainable(items) \
		.flat_map(list) \
		.collect() + [p2, p6]
	return Chainable(packets) \
		.sort(key=cmp_to_key(cmp)) \
		.enumerate(1) \
		.filter(lambda il: il[1] == p2 or il[1] == p6) \
		.reduce(lambda p, il: p * il[0], True, 1) 

if __name__ == '__main__':
	fname = "input.txt" if len(argv) == 1 else argv[1]
	lines = get_lines(fname, rstrip=True)

	items = build_items(lines)

	print("Part 1:", part1(items))
	print("Part 2:", part2(items))
