from common import *


def build_matrix(lines: List[str]) -> Tuple[List[List[int]], Pos, Pos]:
	mat = Chainable(lines) \
		.map(lambda l: list(map(ord, l))) \
		.collect()
	rs, cs = Chainable(lines) \
		.enumerate() \
		.filter(lambda il: 'S' in il[1]) \
		.reduce(lambda _, il: (il[0], il[1].index('S')), True)
	re, ce = Chainable(lines) \
		.enumerate() \
		.filter(lambda il: 'E' in il[1]) \
		.reduce(lambda _, il: (il[0], il[1].index('E')), True)
	mat[rs][cs] = ord('a')
	mat[re][ce] = ord('z')
	return mat, Pos(rs, cs), Pos(re, ce)


def part1():
	def get_neighbors(org: Pos) -> Set[Pos]:
		return Chainable(DIR.values()) \
			.map(lambda p: org + p) \
			.filter(lambda des: (
				(0 <= des.r < nbrow) and \
				(0 <= des.c < nbcol) and \
				(mat[org.r][org.c] + 1 >= mat[des.r][des.c]))) \
			.collect(set)
		
	queue = PriorityQueue()
	queue.put((0, start))	# going from start -> end
	qset = set()

	while not queue.empty():
		dist, pos = queue.get()
		for nei in get_neighbors(pos):
			if nei == end:
				return dist + 1
			if nei not in qset:
				qset.add(nei)
				queue.put((dist+1, nei))

def part2():
	def get_neighbors(org: Pos) -> Set[Pos]:
		return Chainable(DIR.values()) \
			.map(lambda p: org + p) \
			.filter(lambda des: (
				(0 <= des.r < nbrow) and \
				(0 <= des.c < nbcol) and \
				(mat[org.r][org.c] - 1 <= mat[des.r][des.c]))) \
			.collect(set)
		
	queue = PriorityQueue()
	queue.put((0, end))		# going back from end to any 'a'
	qset = set()

	while not queue.empty():
		dist, pos = queue.get()
		for nei in get_neighbors(pos):
			if mat[nei.r][nei.c] == ord('a'):
				return dist + 1
			if nei not in qset:
				qset.add(nei)
				queue.put((dist+1, nei))


if __name__ == '__main__':
	fname = "input.txt" if len(argv) == 1 else argv[1]
	lines = get_lines(fname, rstrip=True)

	mat, start, end = build_matrix(lines)
	nbrow, nbcol = len(mat), len(mat[0])

	print("Part 1:", part1())
	print("Part 2:", part2())
