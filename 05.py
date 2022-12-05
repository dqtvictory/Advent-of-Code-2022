from common import *


def build_stacks(lines: List[str]):
	nb_stacks = int(Chainable(lines) \
		.filter(lambda l: len(l) > 1 and l[1].isnumeric()) \
		.flat_map(str.split) \
		.collect()[-1])

	def reducer(prev: List[List[str]], cur: List[str]):
		return Chainable(prev) \
			.zip(cur) \
			.map(lambda ls_s: ls_s[0] + [ls_s[1]] if ls_s[1] != ' ' else ls_s[0]) \
			.collect()

	stack = [[] for _ in range(nb_stacks)]
	return Chainable(reversed(lines)) \
		.filter(lambda l: '[' in l) \
		.map(lambda l: enumerate(l)) \
		.map(lambda iter_ic: filter(lambda ic: ic[0] % 4 == 1, iter_ic)) \
		.map(lambda iter_ic: map(lambda ic: ic[1], iter_ic)) \
		.reduce(reducer, init=True, initial=stack)

def instruct(lines: List[str], stack: List[List[str]], rev: bool):
	def reducer(prev: List[List[str]], cur: Tuple[int, int, int]):
		nb, fr, to = cur
		moving = prev[fr][:-nb-1:-1] if rev else prev[fr][-nb:]
		
		def mapper(il: Tuple[int, List[str]]):
			i, l = il
			if i == fr:
				return l[:-nb]
			if i == to:
				return l + moving
			return l

		return Chainable(prev) \
			.enumerate() \
			.map(mapper) \
			.collect()

	return Chainable(lines) \
		.filter(lambda l: "move" in l) \
		.map(str.split) \
		.map(lambda l: (int(l[1]), int(l[3]) - 1, int(l[5]) - 1)) \
		.reduce(reducer, init=True, initial=stack)

def part1(lines: List[str]):
	stack = build_stacks(lines)
	return Chainable(instruct(lines, stack, rev=True)) \
		.flat_map(lambda l: l[-1]) \
		.reduce(lambda c1, c2: c1 + c2)

def part2(lines: List[str]):
	stack = build_stacks(lines)
	return Chainable(instruct(lines, stack, rev=False)) \
		.flat_map(lambda l: l[-1]) \
		.reduce(lambda c1, c2: c1 + c2)


if __name__ == '__main__':
	fname = "input.txt" if len(argv) == 1 else argv[1]
	lines = get_lines(fname, False)

	print("Part 1:", part1(lines))
	print("Part 2:", part2(lines))