from common import *

CHECKPOINTS = set(range(20, 221, 40))

def build_timeline(lines: List[str]) -> List[int]:
	return Chainable(lines) \
		.reduce(
			lambda prev, cur: prev + [0] if cur == "noop" else prev + [0, int(cur[5:])],
			True, []
		)

def part1(timeline: List[int]):
	def process_signal(prev: Tuple[int, int], cur: Tuple[int, int]) -> Tuple[int, int]:
		reg, sig = prev
		t, d = cur
		if t in CHECKPOINTS:
			return reg + d, sig + reg * t
		return reg + d, sig

	init = 1, 0		# register value, signal strength
	return Chainable(timeline) \
		.enumerate(1) \
		.reduce(process_signal, True, init)[1]

def part2(timeline: List[int]):
	def process_signal(
		prev: Tuple[int, List[str], List[List[str]]],
		cur: Tuple[int, int]
	) -> Tuple[int, List[str], List[List[str]]]:
		reg, row, crt = prev
		i, d = cur
		if abs(i - reg) <= 1:
			new_row = row + ['#']
		else:
			new_row = row + [' ']
		if i == 39:
			return reg + d, [], crt + [new_row]
		return reg + d, new_row, crt

	init = 1, [], []	# register value, current row, crt
	crt = Chainable(timeline) \
		.enumerate() \
		.map(lambda td: (td[0] % 40, td[1])) \
		.reduce(process_signal, True, init)[2]
	return Chainable(crt) \
		.map("".join) \
		.reduce(lambda s1, s2: f"{s1}\n{s2}")


if __name__ == '__main__':
	fname = "input.txt" if len(argv) == 1 else argv[1]
	lines = get_lines(fname, rstrip=True)

	timeline = build_timeline(lines)

	print("Part 1:", part1(timeline))
	print("Part 2:")
	