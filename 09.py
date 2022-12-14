from common import *


EPS = 1e-2

def move_rope(
	prev: Tuple[List[Pos], Set[Pos]],
	cur: Tuple[str, int]
) -> Tuple[List[Pos], Set[Pos]]:
	rope, visit = prev
	dir, step = DIR[cur[0]], cur[1]

	def make_rope(prev: List[Pos], cur: Pos) -> List[Pos]:
		if not prev:	# head
			new_pos = cur + dir
		else:			# tail
			following = prev[-1]
			if following.distance(cur) < 2.0 - EPS:
				new_pos = cur
			else:
				dr = 0 if following.r == cur.r else 1 if following.r > cur.r else -1
				dc = 0 if following.c == cur.c else 1 if following.c > cur.c else -1
				new_pos = cur + Pos(dr, dc)
		return prev + [new_pos]

	for _ in range(step):
		rope = Chainable(rope) \
			.reduce(make_rope, True, [])
		visit = visit.union({rope[-1]})
	return rope, visit


def part1(lines: List[str]):
	init = [Pos(0, 0), Pos(0, 0)], {Pos(0, 0)}
	return Chainable(lines) \
		.map(str.split) \
		.map(lambda dn: (dn[0], int(dn[1]))) \
		.reduce(lambda prev, cur: move_rope(prev, cur), True, init)[1] \
		.__len__()

def part2(lines: List[str]):
	init = [Pos(0, 0) for _ in range(10)], {Pos(0, 0)}
	return Chainable(lines) \
		.map(str.split) \
		.map(lambda dn: (dn[0], int(dn[1]))) \
		.reduce(lambda prev, cur: move_rope(prev, cur), True, init)[1] \
		.__len__()


if __name__ == '__main__':
	fname = "input.txt" if len(argv) == 1 else argv[1]
	lines = get_lines(fname, rstrip=True)

	print("Part 1:", part1(lines))
	print("Part 2:", part2(lines))
	