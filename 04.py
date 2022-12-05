from common import *


def part1(lines: List[str]):
	return sum(
		map(
			lambda pair: pair[0][0] == pair[1][0] or pair[0][1] >= pair[1][1],
			map(
				lambda pairTuple: (min(pairTuple), max(pairTuple)),
				map(
					lambda pairList: (tuple(map(int, pairList[0])), tuple(map(int, pairList[1]))),
					map(
						lambda r: (r[0].split('-'), r[1].split('-')),
						map(lambda l: l.split(','), lines)
					)
				)
			)
		)
	)
	

def part2(lines: List[str]):
	return sum(
		reduce(
			lambda prev, cur: (prev[0] + cur[0], prev[1] - cur[1]),
			map(
				lambda pair: (1, pair[0][1] < pair[1][0]),
				map(
					lambda pairTuple: (min(pairTuple), max(pairTuple)),
					map(
						lambda pairList: (tuple(map(int, pairList[0])), tuple(map(int, pairList[1]))),
						map(
							lambda r: (r[0].split('-'), r[1].split('-')),
							map(lambda l: l.split(','), lines)
						)
					)
				)
			)
		)
	)


if __name__ == '__main__':
	fname = "input.txt" if len(argv) == 1 else argv[1]
	lines = get_lines(fname)

	print("Part 1:", part1(lines))
	print("Part 2:", part2(lines))
