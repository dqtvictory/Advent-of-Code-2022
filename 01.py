from common import *


def part1(lines: List[str]):
	maxi = -1
	current = 0
	for line in lines:
		if line:
			current += int(line)
		else:
			maxi = max(maxi, current)
			current = 0
	return maxi

def part2(lines: List[str]):
	current = 0
	res = []
	for line in lines:
		if line:
			current += int(line)
		else:
			res.append(current)
			current = 0
	res = sorted(res, reverse=True)[:3]
	return sum(res)
	

if __name__ == '__main__':
	fname = "input" if len(argv) == 1 else argv[1]
	lines = get_lines(fname)

	print("Part 1:", part1(lines))
	print("Part 2:", part2(lines))