from common import *


def mat_indexer(i_row: Tuple[int, List[int]]):
	i, row = i_row
	return Chainable(row) \
		.enumerate() \
		.map(lambda jn: (i, jn[0], jn[1])) \
		.collect()

def make_matrix(lines: List[str]):
	matrix = Chainable(lines) \
		.map(lambda l: Chainable(l).map(int).collect()) \
		.collect()
	nbrow = len(matrix)
	nbcol = len(matrix[0])
	return matrix, nbrow, nbcol

def part1(lines: List[str]):
	matrix, nbrow, nbcol = make_matrix(lines)
	perim = 2 * (nbrow + nbcol - 2)

	def is_visible(tup: Tuple[int, int, int]):
		i, j, n = tup
		u = Chainable(range(i)) \
			.map(lambda ii: matrix[ii][j])
		d = Chainable(range(i+1, nbrow)) \
			.map(lambda ii: matrix[ii][j])
		l = Chainable(range(j)) \
			.map(lambda jj: matrix[i][jj])
		r = Chainable(range(j+1, nbcol)) \
			.map(lambda jj: matrix[i][jj])
		return Chainable([u, d, l, r]) \
			.map(lambda ch: ch.filter(lambda x: x >= n)) \
			.map(len) \
			.reduce(lambda l1, l2: l1 * l2, True, 1) == 0

	return Chainable(matrix) \
		.enumerate() \
		.flat_map(mat_indexer) \
		.filter(lambda ijn : (
				(0 < ijn[0] < nbrow - 1) and \
				(0 < ijn[1] < nbcol - 1)
		)) \
		.map(is_visible) \
		.reduce(lambda a, b: a + b) + perim

def part2(lines: List[str]):
	matrix, nbrow, nbcol = make_matrix(lines)

	def get_visibility(tup: Tuple[int, int, int]):
		i, j, n = tup
		u = Chainable(range(i)) \
			.map(lambda ii: matrix[ii][j]) \
			.reverse()
		d = Chainable(range(i+1, nbrow)) \
			.map(lambda ii: matrix[ii][j])
		l = Chainable(range(j)) \
			.map(lambda jj: matrix[i][jj]) \
			.reverse()
		r = Chainable(range(j+1, nbcol)) \
			.map(lambda jj: matrix[i][jj])
		
		def visib_dir(dir: Chainable):
			init = (0, False)	# count, finish
			return dir.reduce(
				lambda prev, cur: prev if prev[1] else (prev[0] + 1, cur >= n),
				True, init
			)[0]

		return Chainable([u, d, l, r]) \
			.map(visib_dir) \
			.reduce(lambda d1, d2: d1 * d2, True, 1)

	return Chainable(matrix) \
		.enumerate() \
		.flat_map(mat_indexer) \
		.filter(lambda ijn : (
				(0 < ijn[0] < nbrow - 1) and \
				(0 < ijn[1] < nbcol - 1) )) \
		.map(get_visibility) \
		.reduce(lambda a, b: max(a, b))


if __name__ == '__main__':
	fname = "input.txt" if len(argv) == 1 else argv[1]
	lines = get_lines(fname, rstrip=True)

	print("Part 1:", part1(lines))
	print("Part 2:", part2(lines))
