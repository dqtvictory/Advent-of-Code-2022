from common import *


def part1(lines: List[str]):
	return reduce(
		lambda prev, cur: (prev[0], prev[1] + cur) if cur is not None else (max(prev), 0),
		map(lambda l: int(l) if l else None, lines),
		(-1, 0)
	)[0]

def part2(lines: List[str]):
	return sum(sorted(
		reduce(
			lambda prev, cur: (prev[0], prev[1] + cur) if cur is not None else (prev[0] + [prev[1]], 0),
			map(lambda l: int(l) if l else None, lines),
			([], 0)
		)[0], reverse = True
	)[:3])


if __name__ == '__main__':
	fname = "input.txt" if len(argv) == 1 else argv[1]
	lines = get_lines(fname)

	print("Part 1:", part1(lines))
	print("Part 2:", part2(lines))
