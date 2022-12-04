from common import *


def part1(lines: List[str]):
	total = 0
	for line in lines:
		r1, r2 = line.split(",")
		r1 = tuple(map(int, r1.split("-")))
		r2 = tuple(map(int, r2.split("-")))
		total += (r1[0] <= r2[0] and r1[1] >= r2[1]) or \
			(r2[0] <= r1[0] and r2[1] >= r1[1])
	return total

def part2(lines: List[str]):
	total = 0
	subs = 0
	for line in lines:
		r1, r2 = line.split(",")
		r1 = tuple(map(int, r1.split("-")))
		r2 = tuple(map(int, r2.split("-")))
		total += 1
		# count nb of non-overlaps
		subs += (r1[1] < r2[0]) or (r2[1] < r1[0])
	return total - subs
	

if __name__ == '__main__':
	fname = "input" if len(argv) == 1 else argv[1]
	lines = get_lines(fname)

	print("Part 1:", part1(lines))
	print("Part 2:", part2(lines))
