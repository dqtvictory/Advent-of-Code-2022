from common import *


def do(line: str, nb: int):
	return Chainable(range(len(line) - nb)) \
		.map(lambda i: (i , len(set(line[i : i + nb])))) \
		.filter(lambda i_len: i_len[1] == nb) \
		.collect()[0][0] + nb


if __name__ == '__main__':
	fname = "input.txt" if len(argv) == 1 else argv[1]
	lines = get_lines(fname, rstrip=True)

	print("Part 1:", do(lines[0], 4))
	print("Part 2:", do(lines[0], 14))
