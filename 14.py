from common import *


def build_rocks(lines: List[str]) -> Set[Pos]:
	def reducer(prev: Set[Pos], cur: List[Pos]) -> Set[Pos]:
		to_add = set()
		for i, pstart in enumerate(cur[:-1]):
			pend = cur[i + 1]
			dr = pend.r - pstart.r
			dc = pend.c - pstart.c
			if dr:
				dir = Pos(dr // abs(dr), 0)
			else:
				dir = Pos(0, dc // abs(dc))
			while pstart != pend:
				to_add = to_add.union({pstart})
				pstart += dir
			to_add = to_add.union({pend})
		return prev.union(to_add)

	return Chainable(lines) \
		.map(lambda l: l.split(' -> ')) \
		.map(lambda l: list(map(lambda pt: pt.split(','), l))) \
		.map(lambda l: list(map(lambda ls: (int(ls[0]), int(ls[1])), l))) \
		.map(lambda lt: list(map(lambda t: Pos(t[1], t[0]), lt))) \
		.reduce(reducer, True, set())

def part1(obs: Set[Pos]):
	can_fall = lambda pos: pos not in obs
	total = 0
	while True:
		sand = start
		while True:
			if can_fall(sand + DIR['D']):
				sand += DIR['D']
				if sand.r >= floor_lv:
					return total
			elif can_fall(sand + DIR['D'] + DIR['L']):
				sand += DIR['D'] + DIR['L']
			elif can_fall(sand + DIR['D'] + DIR['R']):
				sand += DIR['D'] + DIR['R']
			else:
				obs = obs.union({sand})
				break
		total += 1

def part2(obs: Set[Pos]):
	can_fall = lambda pos: (pos.r < floor_lv + 2) and (pos not in obs)
	total = 0
	while True:
		sand = start
		while True:
			if can_fall(sand + DIR['D']):
				sand += DIR['D']
			elif can_fall(sand + DIR['D'] + DIR['L']):
				sand += DIR['D'] + DIR['L']
			elif can_fall(sand + DIR['D'] + DIR['R']):
				sand += DIR['D'] + DIR['R']
			elif sand == start:
				return total + 1
			else:
				obs = obs.union({sand})
				break
		total += 1


if __name__ == '__main__':
	fname = "input.txt" if len(argv) == 1 else argv[1]
	lines = get_lines(fname, rstrip=True)

	rocks = build_rocks(lines)
	floor_lv = max(rocks, key=lambda r: r.r).r

	start = Pos(0, 500)

	print("Part 1:", part1(rocks.copy()))
	print("Part 2:", part2(rocks.copy()))
