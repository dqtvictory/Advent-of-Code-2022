from common import *


alpha = "qwertyuiopasdfghjklzxcvbnm"
alpha = set(alpha + str.upper(alpha))

a, A = ord('a'), ord('A')

def part1(lines: List[str]):
	return sum(
		map(
			lambda c: ord(c) - a + 1 if c.islower() else ord(c) - A + 27,
			map(
				lambda sets: sets[0].intersection(sets[1]).pop(),
				map(
					lambda l: (set(l[: len(l)//2]), set(l[len(l)//2 :])),
					lines
				)
			)
		)
	)

def part2(lines: List[str]):
	def line_reducer(prev: Tuple[int, Set[str]], cur: Tuple[int, Set[str]]):
		i, s = cur
		s = s.intersection(prev[1])
		if i % 3 == 2:
			c = s.pop()
			val = ord(c) - a + 1 if c.islower() else ord(c) - A + 27
			return val + prev[0], alpha
		return prev[0], s
	
	return reduce(
		line_reducer,
		map(
			lambda pair: (pair[0], set(pair[1])),
			enumerate(lines)
		)
	)[0]
	

if __name__ == '__main__':
	fname = "input.txt" if len(argv) == 1 else argv[1]
	lines = get_lines(fname)

	print("Part 1:", part1(lines))
	print("Part 2:", part2(lines))
